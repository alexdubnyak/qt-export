# 🎨 Figma Qt Export - Preview System

Система предпросмотра компонентов, экспортированных из Figma в Qt форматы.

## 📁 Структура файлов

```
preview/
├── form.ui          # UI файл с компонентами
├── style.qss        # Стили для всех компонентов
├── preview.py       # Python скрипт предпросмотра
├── main.cpp         # C++ приложение предпросмотра
├── CMakeLists.txt   # Система сборки
└── README.md        # Данный файл
```

## 🚀 Быстрый старт

### Python версия (Рекомендуется)
```bash
cd preview/
python preview.py
```

### C++ версия
```bash
cd preview/
mkdir build && cd build
cmake ..
make
./figma_preview
```

## 📋 Требования

### Для Python версии:
- Python 3.6+
- PyQt5 или PyQt6
```bash
pip install PyQt5
# или
pip install PyQt6
```

### Для C++ версии:
- Qt6 (Core, Widgets, UiTools)
- CMake 3.16+
- C++17 компилятор

## 🎯 Что показывает предпросмотр

### 📦 Наборы компонентов:
- **QAbstractButton** - основной набор кнопок

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

## 🎨 Как это работает

### 1. **form.ui**
Qt Designer UI файл содержит:
- Все варианты компонентов
- Правильное позиционирование
- Уникальные ID для каждого виджета
- Tooltip с информацией о компоненте

### 2. **style.qss**
Файл стилей определяет:
- Индивидуальные стили для каждого ID
- Цвета из дизайн-системы Figma
- Шрифты и размеры
- Состояния интерактивности

### 3. **preview.py / main.cpp**
Приложения предпросмотра:
- Загружают UI файл
- Применяют стили
- Обеспечивают интерактивность
- Показывают информацию о компонентах

## 📖 Использование в проектах

### Копирование стилей
```cpp
// Скопировать нужный стиль из style.qss
QPushButton *button = new QPushButton("Label");
button->setObjectName("qpushbutton_md_active_8");
// Применить соответствующий QSS стиль
```

### Загрузка через QUiLoader
```cpp
QUiLoader loader;
QFile file("form.ui");
QWidget *widget = loader.load(&file);

QFile styleFile("style.qss");
QString styles = styleFile.readAll();
widget->setStyleSheet(styles);
```

### Извлечение отдельных компонентов
```python
# В Python с PyQt
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
widget = uic.loadUi('form.ui')

# Найти нужный компонент
button = widget.findChild(QPushButton, 'qpushbutton_lg_active_12')
```

## 🔧 Кастомизация

### Изменение цветов
Отредактируйте `style.qss`:
```css
#qpushbutton_sm_active_0 {
  background-color: #your-color;
  color: #your-text-color;
}
```

### Добавление новых состояний
1. Добавьте виджет в `form.ui`
2. Создайте стиль в `style.qss`
3. Дайте уникальный `objectName`

### Интеграция новых компонентов
1. Экспортируйте из Figma
2. Добавьте в `form.ui`
3. Конвертируйте стили в QSS формат
4. Обновите предпросмотр

## 🐛 Решение проблем

### Python скрипт не запускается
```bash
# Проверьте версию Python
python --version  # должно быть 3.6+

# Установите PyQt
pip install PyQt5
```

### C++ приложение не компилируется
```bash
# Проверьте Qt6
cmake --find-package -DNAME=Qt6 -DCOMPILER_ID=GNU -DLANGUAGE=CXX

# Убедитесь что установлены все компоненты Qt6
sudo apt install qt6-base-dev qt6-tools-dev  # Ubuntu
brew install qt6  # macOS
```

### Файлы не найдены
Убедитесь что все файлы находятся в одной директории:
- `form.ui`
- `style.qss`
- `preview.py` или скомпилированное приложение

### Стили не применяются
1. Проверьте кодировку файла `style.qss` (должна быть UTF-8)
2. Убедитесь что `objectName` в UI соответствуют селекторам в QSS
3. Проверьте синтаксис QSS

## 📝 Дополнительные возможности

### Экспорт в изображения
```bash
# Скриншоты компонентов (требует дополнительной настройки)
python screenshot_components.py
```

### Генерация документации
```bash
# Автоматическая генерация документации по компонентам
python generate_docs.py
```

### Интеграция с дизайн-системой
Этот предпросмотр может служить живой документацией дизайн-системы, 
показывая точно как компоненты выглядят в реальном Qt приложении.

---

**🎯 Цель:** Обеспечить pixel-perfect соответствие между дизайном в Figma и реализацией в Qt

**🔄 Автоматизация:** Весь процесс от Figma до Qt может быть полностью автоматизирован

**📱 Результат:** Готовые к использованию Qt компоненты с профессиональным дизайном
