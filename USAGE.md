# Инструкции по экспорту из Figma в Qt

## Требования

1. **Figma Desktop** (последняя версия)
2. **Claude Desktop** с подключенными MCP серверами
3. **Qt5/Qt6** для тестирования результатов

## Настройка Figma Dev Mode MCP Server

1. Откройте **Figma Desktop**
2. Убедитесь что у вас последняя версия
3. Откройте или создайте файл дизайна
4. В меню Figma (левый верхний угол) → **Preferences**
5. Включите **"Enable Dev Mode MCP Server"**
6. Перезапустите **Claude Desktop**

## Процесс экспорта

### 1. Подготовка в Figma
- Откройте ваш дизайн файл
- Переключитесь в **Dev Mode** (справа вверху)
- Выберите компонент для экспорта

### 2. Экспорт через Claude
- В Claude напишите: "Экспортируй выбранный элемент в Qt форматы"
- Claude автоматически:
  - Получит данные из Figma
  - Сконвертирует в .ui и .qss форматы
  - Сохранит в соответствующие папки репозитория

### 3. Структура экспорта
```
src/
├── widgets/          # .ui файлы → для Qt Designer
├── styles/           # .qss файлы → стили для Qt
└── resources/        # изображения и иконки
```

## Поддерживаемые элементы

| Figma | Qt Widget | Описание |
|-------|-----------|----------|
| Frame | QWidget | Контейнеры и группы |
| Rectangle | QFrame | Прямоугольные блоки |
| Text | QLabel | Текстовые элементы |
| Button | QPushButton | Кнопки |
| Input | QLineEdit | Поля ввода |
| Component | QWidget | Кастомные компоненты |

## Что экспортируется

### Стили (.qss)
- ✅ Цвета фона и текста
- ✅ Границы и скругления
- ✅ Шрифты и размеры
- ✅ Отступы и размеры
- ✅ Тени и эффекты
- ✅ Состояния (hover, pressed, disabled)
- ✅ Темные и светлые темы

### Структура (.ui)
- ✅ Позиционирование элементов
- ✅ Размеры виджетов
- ✅ Иерархия компонентов
- ✅ Текстовое содержимое
- ✅ Object names для стилизации

## Использование в Qt проекте

### 1. Загрузка UI файла
```cpp
#include <QUiLoader>
#include <QFile>

QUiLoader loader;
QFile file(":/widgets/primary_button.ui");
file.open(QFile::ReadOnly);
QWidget *widget = loader.load(&file);
file.close();
```

### 2. Применение стилей
```cpp
#include <QFile>
#include <QTextStream>

QFile styleFile(":/styles/primary_button.qss");
styleFile.open(QFile::ReadOnly | QFile::Text);
QTextStream stream(&styleFile);
QString style = stream.readAll();
widget->setStyleSheet(style);
```

### 3. Интеграция в CMake
```cmake
qt_add_resources(APP_SOURCES
    "resources.qrc"
)
```

## Troubleshooting

### Figma MCP не подключается
1. Убедитесь что Figma Desktop обновлен
2. Проверьте что Dev Mode MCP включен в настройках
3. Полностью перезапустите Claude Desktop
4. Проверьте что выбран элемент в Figma

### Некорректный экспорт
1. Убедитесь что элемент правильно выбран
2. Проверьте что все стили применены в Figma
3. Для сложных компонентов используйте группировку

### Проблемы со стилями
1. Проверьте синтаксис QSS
2. Убедитесь что object names совпадают
3. Используйте Qt Designer для проверки .ui файлов
