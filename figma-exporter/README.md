# Figma to Qt Exporter

Автоматический инструмент для экспорта component set из Figma в Qt QSS стили и .ui файлы.

## Особенности

- 🎨 **Автоматический экспорт** из Figma component sets
- 🔄 **Поддержка всех состояний** (active, hover, pressed, disabled)
- 📏 **Множественные размеры** (small, medium, large)
- 🎯 **Точное соответствие** дизайну в Figma
- ⚡ **Быстрая интеграция** в Qt проекты
- 🛠️ **Настраиваемый маппинг** компонентов

## Поддерживаемые компоненты

- **QPushButton** - стандартные кнопки с текстом и иконками
- **QToolButton** - кнопки-инструменты (только иконка)
- **QToolButton с стрелкой** - выпадающие меню
- **QLabel** - текстовые метки

## Быстрый старт

### 1. Экспорт из Figma

```javascript
import { FigmaToQtExporter } from './figma-to-qt.js';

// Переменные дизайна из Figma
const designVariables = {
    "Theme/QAbstractButton/surface:active": "#e2e2e2",
    "Theme/QAbstractButton/border:active": "#bbbbbb",
    "Theme/QAbstractButton/surface:hover": "#dff4fa",
    "Theme/QAbstractButton/border:hover": "#85cfeb",
    // ... остальные переменные
};

// Создаем экспортер
const exporter = new FigmaToQtExporter();

// Экспортируем все стили
const result = exporter.exportComplete(figmaData, designVariables);

console.log(result.qss); // QSS стили
console.log(result.ui);  // UI файл
```

### 2. Использование в Qt

```cpp
// main.cpp
#include <QApplication>
#include <QFile>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    
    // Загружаем сгенерированные стили
    QFile styleFile("generated-components.qss");
    styleFile.open(QFile::ReadOnly);
    app.setStyleSheet(styleFile.readAll());
    
    // Ваше приложение готово!
    return app.exec();
}
```

## Структура файлов

```
figma-exporter/
├── figma-to-qt.js           # Основной модуль экспорта
├── example.js               # Примеры использования
├── generated-components.qss # Готовые стили из Figma
└── README.md               # Документация
```

## API Reference

### FigmaToQtExporter

#### `exportQSSFromFigma(figmaData, designVariables)`

Экспортирует QSS стили из данных Figma.

**Параметры:**
- `figmaData` - HTML/JSX код компонентов из Figma
- `designVariables` - объект с переменными дизайна

**Возвращает:** строку с QSS стилями

#### `generateUIFile(componentName, components)`

Генерирует .ui файл с компонентами.

**Параметры:**
- `componentName` - имя основного виджета
- `components` - массив компонентов для добавления

**Возвращает:** XML строку .ui файла

#### `exportComplete(figmaData, designVariables, componentName)`

Полный экспорт QSS + UI файлов.

**Возвращает:**
```javascript
{
    qss: "/* QSS styles */",
    ui: "<?xml version... ?>",
    timestamp: "2024-07-20T10:41:52.000Z"
}
```

## Workflow

### 1. Подготовка в Figma

1. Создайте **Component Set** с вариантами:
   - **Size**: sm, md, lg
   - **State**: active, hover, pressed, disabled  
   - **Type**: QPushButton, QToolButton_icon, QToolButton_arrow

2. Настройте **Design Variables** для:
   - Цветов (Theme/QAbstractButton/surface:*, border:*)
   - Размеров (Grid/Widgets Size/*, Grid/Font Size/*)
   - Отступов (Grid/Spacing/*)

### 2. Экспорт

Используйте Figma Dev Mode коннектор для получения данных:

```javascript
// Через Claude с Figma коннектором
const figmaData = await getFigmaComponentData();
const variables = await getFigmaVariables();

const exporter = new FigmaToQtExporter();
const result = exporter.exportComplete(figmaData, variables);
```

### 3. Интеграция

1. Сохраните `result.qss` как `components.qss`
2. Сохраните `result.ui` как `components.ui`  
3. Подключите стили в Qt приложении

## Маппинг компонентов

| Figma Type | Qt Class | Описание |
|------------|----------|----------|
| QPushButton | QPushButton | Стандартная кнопка |
| QToolButton_icon | QToolButton | Кнопка только с иконкой |
| QToolButton_arrow | QToolButton | Кнопка с выпадающим меню |

## Маппинг состояний

| Figma State | Qt Selector | Описание |
|-------------|-------------|----------|
| active | (default) | Обычное состояние |
| hover | :hover | При наведении мыши |
| pressed | :pressed | При нажатии |
| disabled | :disabled | Неактивное состояние |

## Размеры

| Figma Size | Min Height | Font Size | Padding |
|------------|------------|-----------|---------|
| sm | 24px | 12px | 4px 8px |
| md | 32px | 14px | 6px 12px |
| lg | 40px | 16px | 8px 16px |

## Примеры использования

### Базовый экспорт

```javascript
import { exportFromFigma } from './example.js';

const result = exportFromFigma();
// Автоматически генерирует QSS и UI файлы
```

### С Figma API

```javascript
import { exportFromFigmaAPI } from './example.js';

const result = await exportFromFigmaAPI('your-file-key', 'node-id');
// Напрямую из Figma через API
```

### Сохранение на диск

```javascript
import { saveExportToDisk } from './example.js';

saveExportToDisk(result, './output');
// Сохраняет files в папку ./output
```

## Расширение

### Добавление новых компонентов

```javascript
// В figma-to-qt.js
this.componentTypeMapping = {
    'QPushButton': 'QPushButton',
    'QToolButton_icon': 'QToolButton',
    'QToolButton_arrow': 'QToolButton',
    'QLineEdit': 'QLineEdit',  // Новый компонент
    // ...
};
```

### Кастомные стили

```javascript
// Переопределение стилей
getStylesFromVariables(qtClass, state, variables) {
    const styles = super.getStylesFromVariables(qtClass, state, variables);
    
    // Добавляем кастомные стили
    if (qtClass === 'QPushButton' && state === 'hover') {
        styles['box-shadow'] = '0 2px 4px rgba(0,0,0,0.1)';
    }
    
    return styles;
}
```

## Требования

- Node.js 16+ (для серверного использования)
- Современный браузер (для клиентского использования)
- Qt 5.12+ (для использования сгенерированных стилей)

## Лицензия

MIT License - используйте свободно в любых проектах.

## Поддержка

Если у вас есть вопросы или предложения:
1. Создайте Issue в репозитории
2. Отправьте Pull Request с улучшениями
3. Обсудите в Discussions

---

**Автоматизируйте свой дизайн-процесс с Figma to Qt Exporter!** 🚀
