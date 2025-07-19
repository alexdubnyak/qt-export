# Qt Export Tool

Автоматический экспорт выделенных компонентов из Figma в Qt форматы (QSS стили и .ui файлы).

## Возможности

- 🎨 Экспорт Figma компонентов в QSS стили
- 🖼️ Генерация .ui файлов для Qt Designer
- 🔄 Автоматическое преобразование цветов, шрифтов и размеров
- 📱 Поддержка responsive дизайна

## Установка

```bash
npm install
# или
pip install -r requirements.txt
```

## Использование

```bash
# Экспорт выделенного компонента
node src/export.js --figma-url="your-figma-url" --output="./output"
```

## Требования

- Figma API token
- Node.js 16+ или Python 3.8+
- Qt5/Qt6 для тестирования результатов
