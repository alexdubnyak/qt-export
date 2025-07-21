# Layouts Directory

UI макеты и формы для Qt приложений.

## Структура

```
layouts/
├── components/          # Компоненты UI по категориям
│   ├── buttons/        # Демонстрация кнопок
│   │   ├── showcase.ui # Все типы кнопок
│   │   └── groups.ui   # Группы кнопок
│   ├── inputs/         # Поля ввода
│   │   ├── text.ui     # Текстовые поля
│   │   └── selection.ui # Выбор (combobox, listbox)
│   └── containers/     # Контейнеры
│       ├── frames.ui   # QFrame примеры
│       └── groups.ui   # QGroupBox примеры
├── dialogs/            # Диалоговые окна
│   ├── settings.ui     # Настройки
│   ├── about.ui        # О программе
│   └── preferences.ui  # Предпочтения
├── windows/            # Основные окна приложения
│   ├── main.ui         # Главное окно
│   └── preview.ui      # Окно предпросмотра
└── demo.ui             # Демонстрационная форма (бывший form.ui)
```

## Использование

### В C++
```cpp
QUiLoader loader;
QFile file(":/layouts/demo.ui");
QWidget *widget = loader.load(&file);
widget->show();
```

### В Python
```python
from PyQt5 import uic

widget = uic.loadUi('layouts/demo.ui')
widget.show()
```

## Компоненты

Каждый UI файл демонстрирует определенный набор компонентов:
- **demo.ui** - полная демонстрация всех компонентов
- **components/buttons/showcase.ui** - все типы кнопок
- **components/inputs/text.ui** - текстовые поля ввода
- **dialogs/settings.ui** - пример диалога настроек

## Стили

Все UI файлы используют стили из папки `styles/`:
- Основные стили подключаются через `styles/main.qss`
- Специфичные стили для компонентов в `styles/components/`
