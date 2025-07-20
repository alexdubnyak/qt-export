# 🎨 Qt Export Tool - Figma to Qt Bridge

Профессиональная система автоматического экспорта компонентов из Figma в Qt форматы с полноценным предпросмотром.

## ✨ Возможности

- 🎨 **Экспорт Figma компонентов** в QSS стили
- 🖼️ **Генерация .ui файлов** для Qt Designer
- 🔄 **Автоматическое преобразование** цветов, шрифтов и размеров
- 📱 **Поддержка responsive дизайна**
- 🔍 **Система предпросмотра** всех компонентов
- 🎯 **Pixel-perfect соответствие** дизайну
- 🆕 **Figma Component Set экспорт** - автоматический экспорт целых наборов компонентов

## 📁 Структура проекта

```
qt-export/
├── figma-exporter/       # 🆕 Новый Figma to Qt экспортер
│   ├── figma-to-qt.js   # Основной модуль экспорта
│   ├── example.js       # Примеры использования
│   ├── generated-components.qss # Готовые стили
│   ├── package.json     # NPM конфигурация
│   └── README.md        # Документация экспортера
├── src/
│   ├── widgets/          # .ui файлы (Qt Designer UI files)
│   ├── styles/           # .qss файлы (Qt Style Sheets)
│   └── resources/        # Ресурсы (изображения, иконки)
├── preview/              # Система предпросмотра
│   ├── form.ui          # UI с множеством компонентов
│   ├── style.qss        # Стили для всех состояний
│   ├── preview.py       # Python предпросмотр
│   ├── main.cpp         # C++ предпросмотр
│   └── CMakeLists.txt   # Система сборки
├── examples/             # Примеры использования
├── scripts/              # Скрипты автоматизации
└── docs/                 # Документация
```

## 🚀 Быстрый старт

### 🆕 Новый способ: Figma Component Set экспорт

1. **Подготовьте Component Set в Figma:**
   - Создайте компоненты с вариантами (Size: sm/md/lg, State: active/hover/pressed/disabled)
   - Настройте Design Variables для цветов и размеров

2. **Экспортируйте через Claude:**
   ```javascript
   // Выделите component set в Figma
   // Claude автоматически получит данные и сгенерирует QSS
   
   import { FigmaToQtExporter } from './figma-exporter/figma-to-qt.js';
   const exporter = new FigmaToQtExporter();
   const result = exporter.exportComplete(figmaData, designVariables);
   ```

3. **Используйте в Qt:**
   ```cpp
   QFile styleFile("generated-components.qss");
   styleFile.open(QFile::ReadOnly);
   app.setStyleSheet(styleFile.readAll());
   ```

### 🔄 Традиционный способ: Предпросмотр компонентов
```bash
# Python версия (рекомендуется)
cd preview/
python preview.py

# C++ версия
cd preview/
mkdir build && cd build
cmake .. && make
./figma_preview
```

## 🎯 Что экспортируется

### 📦 Компоненты:
- **QAbstractButton** - набор кнопок всех типов
- **QPushButton** - стандартные кнопки с текстом и иконками
- **QToolButton** - кнопки-инструменты (иконка, стрелка)

### 📏 Размеры:
- **Small (sm)** - 24px высота, 12px шрифт
- **Medium (md)** - 32px высота, 14px шрифт  
- **Large (lg)** - 40px высота, 16px шрифт

### 🎭 Состояния:
- **Active** - обычное состояние (#e2e2e2)
- **Hover** - при наведении (#dff4fa)
- **Pressed** - при нажатии (#b1e2f2)
- **Disabled** - неактивное состояние (серый)

## 📋 Требования

### Для Figma экспорта:
- **Claude Desktop** с Figma Dev Mode MCP Server
- **Node.js 16+** (для серверного использования)
- **Современный браузер** (для клиентского использования)

### Для предпросмотра:
- **Python 3.6+** + PyQt5/PyQt6 или
- **Qt6** (Core, Widgets, UiTools) + CMake 3.16+

## 🎨 Форматы экспорта

### 🆕 Figma Component Set → QSS
Автоматический экспорт всего набора компонентов:
- **Все состояния** (active, hover, pressed, disabled)
- **Все размеры** (sm, md, lg) 
- **Все типы** (QPushButton, QToolButton)
- **Design Variables** интеграция
- **Pixel-perfect** соответствие Figma

### Qt UI Files (.ui)
Файлы пользовательского интерфейса для Qt Designer:
- Описание структуры виджетов
- Позиционирование и размеры
- Иерархия компонентов
- Базовые свойства

### Qt Style Sheets (.qss)
CSS-подобные стили для Qt приложений:
- Цвета и фоны из Figma Design Variables
- Шрифты и размеры из типографики Figma
- Отступы и границы с точными размерами
- Интерактивные состояния (:hover, :pressed, :disabled)
- Поддержка размерных вариантов

## 🔄 Workflow экспорта

### 🆕 Новый автоматизированный workflow:

1. **Component Set в Figma** → создание библиотеки компонентов
2. **Design Variables** → настройка цветов, размеров, отступов
3. **Выделение Component Set** → активация в Dev Mode
4. **Claude экспорт** → автоматическая конвертация всех вариантов
5. **Генерация QSS** → полный файл стилей для всех состояний
6. **Один клик интеграция** → подключение в Qt проект

### Традиционный workflow:
1. **Дизайн в Figma** → создание отдельных компонентов
2. **Выбор элемента** → активация в Dev Mode
3. **Экспорт через Claude** → ручная конвертация
4. **Генерация файлов** → .ui + .qss + ресурсы
5. **Предпросмотр** → проверка результата
6. **Интеграция** → использование в Qt проекте

## 📖 Примеры использования

### 🆕 Figma Component Set экспорт
```javascript
// figma-exporter/example.js
import { FigmaToQtExporter } from './figma-to-qt.js';

const exporter = new FigmaToQtExporter();

// Экспорт полного набора компонентов
const result = exporter.exportComplete(figmaData, designVariables);

// Сохранение на диск
saveExportToDisk(result, './output');
```

### Загрузка через QUiLoader
```cpp
#include <QUiLoader>
#include <QFile>

QUiLoader loader;
QFile file(":/widgets/qabstract_button.ui");
QWidget *widget = loader.load(&file);

// Загрузка сгенерированных стилей из Figma
QFile styleFile(":/figma-exporter/generated-components.qss");
widget->setStyleSheet(styleFile.readAll());
```

### Python интеграция
```python
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

app = QApplication([])
widget = uic.loadUi('qabstract_button.ui')

# Использование стилей, экспортированных из Figma
with open('figma-exporter/generated-components.qss', 'r') as f:
    widget.setStyleSheet(f.read())

widget.show()
```

## 🛠️ Поддерживаемые компоненты

### ✅ Текущие (Figma экспорт):
- **QPushButton** - все состояния и размеры
- **QToolButton** (icon) - кнопки только с иконками
- **QToolButton** (arrow) - кнопки с выпадающими меню
- **QLabel** - текстовые элементы с правильными цветами

### ✅ Текущие (традиционный экспорт):
- **QAbstractButton** - базовые кнопки
- **Контейнеры** (QWidget, QFrame)
- **Текстовые элементы** (QLabel)

### 🔄 Планируемые:
- **QLineEdit, QTextEdit** - поля ввода
- **QListWidget, QComboBox** - списки и выпадающие меню
- **QSlider, QProgressBar** - слайдеры и прогресс-бары
- **QMenuBar, QMenu** - меню и навигация
- **QCheckBox, QRadioButton** - чекбоксы и радиокнопки

## 📚 Документация

- **[figma-exporter/README.md](figma-exporter/README.md)** - 🆕 Подробная документация Figma экспортера
- **[USAGE.md](USAGE.md)** - Подробные инструкции по использованию
- **[preview/README.md](preview/README.md)** - Документация системы предпросмотра
- **[EXPORT_SUMMARY.md](EXPORT_SUMMARY.md)** - Отчет о последнем экспорте
- **[examples/](examples/)** - Примеры кода интеграции

## 🎯 Преимущества

### 🆕 Figma Component Set экспорт:
- **Полная автоматизация** - от component set до готового QSS
- **Design System интеграция** - использование Figma Variables
- **Массовый экспорт** - все варианты компонентов одновременно
- **Консистентность** - единая система стилей
- **Масштабируемость** - легкое добавление новых компонентов

### Общие преимущества:
- **Pixel-perfect результаты** - точное соответствие дизайну
- **Профессиональное качество** - готовые к production компоненты
- **Полная интерактивность** - все состояния UI
- **Кроссплатформенность** - работает на всех Qt платформах
- **Живая документация** - предпросмотр как дизайн-система

## 🔧 Кастомизация

### 🆕 Figma экспортер поддерживает:
- **Кастомный маппинг** Figma компонентов → Qt классы
- **Расширяемые состояния** (добавление новых состояний)
- **Настраиваемые размеры** через Design Variables
- **Темная/светлая тема** через переменные цветов

### Система позволяет настраивать:
- Цветовые схемы
- Размеры компонентов  
- Состояния интерактивности
- Анимации и переходы

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта:
- 🐛 Сообщения об ошибках
- 💡 Предложения новых функций  
- 🔧 Улучшения кода
- 📝 Улучшения документации
- 🎨 Новые компоненты для экспорта

## 📄 Лицензия

Проект распространяется под открытой лицензией MIT. Детали в файле LICENSE.

---

**🎨 Цель проекта:** Устранить разрыв между дизайном и разработкой, обеспечив seamless workflow от Figma к Qt

**🚀 Результат:** Высококачественные Qt компоненты, точно соответствующие дизайну, готовые к использованию в production

**🆕 Новинка:** Полностью автоматизированный экспорт Component Set из Figma в готовые Qt стили одним кликом!
