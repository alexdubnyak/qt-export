// Complete Figma to Qt QSS Exporter
class FigmaToQtExporter {
    constructor() {
        // Маппинг типов компонентов Figma в Qt классы
        this.componentTypeMapping = {
            'QPushButton': 'QPushButton',
            'QToolButton_icon': 'QToolButton',
            'QToolButton_arrow': 'QToolButton'
        };
        
        // Маппинг состояний Figma в Qt селекторы
        this.stateMapping = {
            'active': '',
            'hover': ':hover',
            'pressed': ':pressed', 
            'disabled': ':disabled'
        };
        
        // Маппинг размеров
        this.sizeMapping = {
            'sm': 'small',
            'md': 'medium', 
            'lg': 'large'
        };
    }
    
    // Главная функция экспорта QSS из данных Figma
    exportQSSFromFigma(figmaData, designVariables) {
        let qssOutput = "/* Generated QSS from Figma Component Set */\n";
        qssOutput += "/* Auto-generated on " + new Date().toISOString() + " */\n\n";
        
        // Извлекаем все уникальные комбинации состояний из Figma данных
        const componentVariants = this.extractComponentVariants(figmaData);
        
        // Генерируем QSS для каждого типа компонента
        for (const [qtClass, variants] of Object.entries(componentVariants)) {
            qssOutput += this.generateQSSForComponent(qtClass, variants, designVariables);
        }
        
        return qssOutput;
    }
    
    // Извлечение вариантов компонентов из данных Figma
    extractComponentVariants(figmaData) {
        const componentVariants = {};
        
        // Парсим код компонентов для получения всех вариантов
        const componentCode = figmaData.toString();
        
        // Ищем все варианты в data-name атрибутах
        const variantRegex = /data-name="([^"]*Size=([^,]*), State=([^,]*), Type=([^"]*))"[^>]*>/g;
        let match;
        
        while ((match = variantRegex.exec(componentCode)) !== null) {
            const [, fullName, size, state, type] = match;
            const qtClass = this.componentTypeMapping[type] || 'QPushButton';
            
            if (!componentVariants[qtClass]) {
                componentVariants[qtClass] = [];
            }
            
            componentVariants[qtClass].push({
                size: size.trim(),
                state: state.trim(),
                type: type.trim(),
                originalName: fullName
            });
        }
        
        // Удаляем дубликаты
        for (const qtClass in componentVariants) {
            componentVariants[qtClass] = componentVariants[qtClass].filter((variant, index, arr) => 
                arr.findIndex(v => v.size === variant.size && v.state === variant.state && v.type === variant.type) === index
            );
        }
        
        return componentVariants;
    }
    
    // Генерация QSS для конкретного компонента
    generateQSSForComponent(qtClass, variants, variables) {
        let qss = `/* ${qtClass} Styles */\n`;
        
        // Группируем варианты по состояниям
        const stateGroups = {};
        variants.forEach(variant => {
            if (!stateGroups[variant.state]) {
                stateGroups[variant.state] = [];
            }
            stateGroups[variant.state].push(variant);
        });
        
        // Генерируем стили для каждого состояния
        for (const [state, stateVariants] of Object.entries(stateGroups)) {
            const selector = qtClass + (this.stateMapping[state] || '');
            qss += `${selector} {\n`;
            
            // Получаем стили из переменных дизайна
            const styles = this.getStylesFromVariables(qtClass, state, variables);
            
            for (const [property, value] of Object.entries(styles)) {
                qss += `    ${property}: ${value};\n`;
            }
            
            // Добавляем размеры для разных размеров компонентов
            const sizeStyles = this.getSizeStyles(stateVariants, variables);
            for (const [property, value] of Object.entries(sizeStyles)) {
                qss += `    ${property}: ${value};\n`;
            }
            
            qss += `}\n\n`;
        }
        
        return qss;
    }
    
    // Получение стилей из переменных дизайна
    getStylesFromVariables(qtClass, state, variables) {
        const styles = {};
        const componentPrefix = qtClass.replace('Q', '');
        
        // Цвет фона
        const surfaceKey = `Theme/${componentPrefix}/surface:${state}` || `Theme/QAbstractButton/surface:${state}`;
        if (variables[surfaceKey]) {
            styles['background-color'] = variables[surfaceKey];
        }
        
        // Цвет границы
        const borderKey = `Theme/${componentPrefix}/border:${state}` || `Theme/QAbstractButton/border:${state}`;
        if (variables[borderKey]) {
            styles['border'] = `1px solid ${variables[borderKey]}`;
        }
        
        // Скругление углов
        if (variables['Grid/Radius/radius-sm']) {
            styles['border-radius'] = `${variables['Grid/Radius/radius-sm']}px`;
        }
        
        // Цвет текста для лейблов
        if (qtClass === 'QLabel' || qtClass.includes('Label')) {
            const textColorKey = `Theme/QLabel/label:${state}`;
            if (variables[textColorKey]) {
                styles['color'] = variables[textColorKey];
            }
        }
        
        // Шрифт
        if (variables['Grid/Font Size/small']) {
            styles['font-size'] = `${variables['Grid/Font Size/small']}px`;
        }
        styles['font-family'] = "'Roboto', sans-serif";
        
        return styles;
    }
    
    // Получение стилей размеров
    getSizeStyles(stateVariants, variables) {
        const styles = {};
        
        // Отступы по умолчанию
        if (variables['Grid/Spacing/spacing-xxs'] && variables.small) {
            styles['padding'] = `${variables['Grid/Spacing/spacing-xxs']}px ${variables.small}px`;
        }
        
        // Минимальная высота базируется на малом размере
        if (variables['Grid/Widgets Size/Small']) {
            styles['min-height'] = `${variables['Grid/Widgets Size/Small']}px`;
        }
        
        return styles;
    }
    
    // Генерация .ui файла
    generateUIFile(componentName = "MainWindow", components = []) {
        let uiContent = `<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>${componentName}</class>
 <widget class="QWidget" name="${componentName}">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>${componentName}</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">`;
  
        // Добавляем компоненты в UI
        components.forEach((component, index) => {
            uiContent += `
   <item>
    <widget class="${component.qtClass}" name="${component.name || component.qtClass.toLowerCase() + index}">
     <property name="text">
      <string>${component.text || "Label"}</string>
     </property>
    </widget>
   </item>`;
        });
        
        uiContent += `
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>`;
        
        return uiContent;
    }
    
    // Экспорт полного пакета (QSS + UI)
    exportComplete(figmaData, designVariables, componentName = "MainWindow") {
        const qssContent = this.exportQSSFromFigma(figmaData, designVariables);
        
        // Создаем базовые компоненты для UI файла
        const sampleComponents = [
            { qtClass: 'QPushButton', name: 'pushButton', text: 'Button' },
            { qtClass: 'QToolButton', name: 'toolButton', text: 'Tool' },
            { qtClass: 'QLabel', name: 'label', text: 'Label Text' }
        ];
        
        const uiContent = this.generateUIFile(componentName, sampleComponents);
        
        return {
            qss: qssContent,
            ui: uiContent,
            timestamp: new Date().toISOString()
        };
    }
}

// Экспорт для использования
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { FigmaToQtExporter };
} else if (typeof window !== 'undefined') {
    window.FigmaToQtExporter = FigmaToQtExporter;
}
