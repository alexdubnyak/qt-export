# Styles Directory

Централизованное хранение всех QSS стилей для Qt компонентов.

## Структура

```
styles/
├── components/           # Стили компонентов
│   ├── buttons.qss      # Все стили кнопок (QPushButton, QToolButton)
│   ├── inputs.qss       # Поля ввода (QLineEdit, QTextEdit)
│   ├── containers.qss   # Контейнеры (QWidget, QFrame, QGroupBox)
│   └── navigation.qss   # Навигация (QMenuBar, QTabWidget)
├── themes/              # Цветовые темы
│   ├── light.qss       # Светлая тема
│   ├── dark.qss        # Темная тема
│   └── figma.qss       # Тема из Figma Design System
├── generated/           # Автогенерированные стили
│   └── figma-export.qss # Экспорт из Figma
└── main.qss            # Основной файл стилей
```

## Использование

### В C++
```cpp
QFile styleFile(":/styles/main.qss");
styleFile.open(QFile::ReadOnly);
app.setStyleSheet(styleFile.readAll());
```

### В Python
```python
with open('styles/main.qss', 'r') as f:
    app.setStyleSheet(f.read())
```

## Figma интеграция

Стили автоматически синхронизируются с Figma Design System через:
- CSS переменные в `themes/figma.qss`
- Автогенерированные стили в `generated/figma-export.qss`
- Компонентные стили в `components/`
