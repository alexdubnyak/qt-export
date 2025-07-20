# 🎨 Qt Export Tool - Figma to Qt Bridge

Профессиональная система автоматического экспорта компонентов из Figma в Qt форматы с полноценным предпросмотром.

## ✨ Возможности

- 🎨 **Экспорт Figma компонентов** в QSS стили
- 🖼️ **Генерация .ui файлов** для Qt Designer
- 🔄 **Автоматическое преобразование** цветов, шрифтов и размеров
- 📱 **Поддержка responsive дизайна**
- 🔍 **Система предпросмотра** всех компонентов
- 🎯 **Pixel-perfect соответствие** дизайну

## 📁 Структура проекта

```
qt-export/
├── src/
│   ├── widgets/          # .ui файлы (Qt Designer UI files)
│   ├── styles/           # .qss файлы (Qt Style Sheets)
│   └── resources/        # Ресурсы (изображения, иконки)
├── preview/              # 🆕 Система предпросмотра
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

### 1. Предпросмотр компонентов
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

### 2. Экспорт из Figma
1. Выберите элемент в Figma
2. Запустите экспорт через Claude MCP
3. Получите готовые .ui и .qss файлы
4. Импортируйте в ваш Qt проект

## 🎯 Что экспортируется

### 📦 Компоненты:
- **QAbstractButton** - набор кнопок всех типов

### 🔧 Типы виджетов:
- **QPushButton** - стандартные кнопки с текстом
- **QToolButton_icon** - кнопки только с иконками  
- **QToolButton_arrow** - кнопки с выпадающими меню

### 📏 Размеры:
- **Small (sm)** - 24-32px высота
- **Medium (md)** - 32-40px высота
- **Large (lg)** - 40-48px высота

### 🎭 Состояния:
- **Active** - обычное состояние
- **Hover** - при наведении мыши
- **Pressed** - при нажатии
- **Disabled** - неактивное состояние

## 📋 Требования

### Для предпросмотра:
- **Python 3.6+** + PyQt5/PyQt6 или
- **Qt6** (Core, Widgets, UiTools) + CMake 3.16+

### Для экспорта:
- **Figma Desktop** app с включенным Dev Mode MCP Server
- **Claude Desktop** с настроенными MCP подключениями

## 🎨 Форматы экспорта

### Qt UI Files (.ui)
Файлы пользовательского интерфейса для Qt Designer:
- Описание структуры виджетов
- Позиционирование и размеры
- Иерархия компонентов
- Базовые свойства

### Qt Style Sheets (.qss)
CSS-подобные стили для Qt приложений:
- Цвета и фоны из Figma
- Шрифты и размеры текста
- Отступы и границы
- Интерактивные состояния
- Эффекты и тени

## 🔄 Workflow экспорта

1. **Дизайн в Figma** → создание компонентов
2. **Выбор элемента** → активация в Dev Mode
3. **Экспорт через Claude** → автоматическая конвертация
4. **Генерация файлов** → .ui + .qss + ресурсы
5. **Предпросмотр** → проверка результата
6. **Интеграция** → использование в Qt проекте

## 📖 Примеры использования

### Загрузка через QUiLoader
```cpp
#include <QUiLoader>
#include <QFile>

QUiLoader loader;
QFile file(":/widgets/qabstract_button.ui");
QWidget *widget = loader.load(&file);

QFile styleFile(":/styles/qabstract_button.qss");
widget->setStyleSheet(styleFile.readAll());
```

### Программное создание
```cpp
QWidget *button = new QWidget;
button->setObjectName("QAbstractButtonWidget");

// Загрузка стилей из экспорта
QFile styleFile(":/styles/qabstract_button.qss");
button->setStyleSheet(styleFile.readAll());
```

### Python интеграция
```python
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

app = QApplication([])
widget = uic.loadUi('qabstract_button.ui')

with open('qabstract_button.qss', 'r') as f:
    widget.setStyleSheet(f.read())

widget.show()
```

## 🛠️ Поддерживаемые компоненты

### Текущие:
- ✅ Кнопки (QPushButton, QToolButton)
- ✅ Контейнеры (QWidget, QFrame)
- ✅ Текстовые элементы (QLabel)

### Планируемые:
- 🔄 Поля ввода (QLineEdit, QTextEdit)
- 🔄 Списки (QListWidget, QComboBox)
- 🔄 Слайдеры (QSlider, QProgressBar)
- 🔄 Меню (QMenuBar, QMenu)

## 📚 Документация

- **[USAGE.md](USAGE.md)** - Подробные инструкции по использованию
- **[preview/README.md](preview/README.md)** - Документация системы предпросмотра
- **[EXPORT_SUMMARY.md](EXPORT_SUMMARY.md)** - Отчет о последнем экспорте
- **[examples/](examples/)** - Примеры кода интеграции

## 🎯 Преимущества

- **Pixel-perfect результаты** - точное соответствие дизайну
- **Автоматизация процесса** - от дизайна до кода одним кликом
- **Профессиональное качество** - готовые к production компоненты
- **Полная интерактивность** - все состояния UI
- **Кроссплатформенность** - работает на всех Qt платформах
- **Живая документация** - предпросмотр как дизайн-система

## 🔧 Кастомизация

Система позволяет легко настраивать:
- Цветовые схемы
- Размеры компонентов
- Состояния интерактивности
- Анимации и переходы
- Темную/светлую тему

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта:
- 🐛 Сообщения об ошибках
- 💡 Предложения новых функций  
- 🔧 Улучшения кода
- 📝 Улучшения документации

## 📄 Лицензия

Проект распространяется под открытой лицензией. Детали в файле LICENSE.

---

**🎨 Цель проекта:** Устранить разрыв между дизайном и разработкой, обеспечив seamless workflow от Figma к Qt

**🚀 Результат:** Высококачественные Qt компоненты, точно соответствующие дизайну, готовые к использованию в production
