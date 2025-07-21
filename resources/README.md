# Resources Directory

Ресурсы приложения: иконки, изображения, шрифты.

## Структура

```
resources/
├── icons/              # SVG иконки по категориям
│   ├── buttons/       # Иконки для кнопок
│   │   ├── close.svg
│   │   ├── minimize.svg
│   │   └── maximize.svg
│   ├── navigation/    # Навигационные иконки
│   │   ├── menu.svg
│   │   ├── back.svg
│   │   └── forward.svg
│   └── actions/       # Иконки действий
│       ├── save.svg
│       ├── open.svg
│       └── delete.svg
├── images/            # Растровые изображения
│   ├── logos/
│   ├── backgrounds/
│   └── screenshots/
├── fonts/             # Шрифты
│   ├── Roboto/
│   └── custom/
└── resources.qrc      # Qt resource file
```

## Использование

### В C++
```cpp
// Загрузка иконки
QIcon icon(":/icons/buttons/close.svg");
button->setIcon(icon);

// Загрузка изображения
QPixmap pixmap(":/images/logos/app-logo.png");
label->setPixmap(pixmap);
```

### В Python
```python
from PyQt5.QtGui import QIcon, QPixmap

# Иконка
icon = QIcon(":/icons/buttons/close.svg")
button.setIcon(icon)

# Изображение
pixmap = QPixmap(":/images/logos/app-logo.png")
label.setPixmap(pixmap)
```

## Иконки

### Категории иконок:
- **buttons/** - иконки для кнопок (close, minimize, maximize)
- **navigation/** - навигационные элементы (menu, back, forward)
- **actions/** - действия пользователя (save, open, delete, edit)

### Стандарты:
- **Формат**: SVG (векторные, масштабируемые)
- **Размеры**: 16x16, 24x24, 32x32 пиксели
- **Стиль**: соответствует Figma Design System
- **Цвета**: используют переменные из `styles/themes/figma.qss`

## Qt Resource System

Все ресурсы интегрированы в Qt Resource System через `resources.qrc`:

```xml
<RCC>
    <qresource prefix="/">
        <file>icons/buttons/close.svg</file>
        <file>icons/navigation/menu.svg</file>
        <file>images/logos/app-logo.png</file>
    </qresource>
</RCC>
```

## Генерация иконок

Иконки можно генерировать автоматически с помощью:
```bash
cd tools/generators
python icon-generator.py --style figma --size 24
```

Это создаст иконки в соответствии с текущей темой Figma Design System.
