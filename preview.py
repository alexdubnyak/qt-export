#!/usr/bin/env python3
"""
Qt Components Preview - QAbstractButton Export from Figma
Загружает form.ui и применяет style.qss для предпросмотра компонентов
Автоматически сгенерирован через Figma Qt Export
"""

import sys
import os
from pathlib import Path

if sys.version_info < (3, 6):
    print("❌ Требуется Python 3.6 или выше")
    sys.exit(1)

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
    from PyQt5.QtCore import Qt
    from PyQt5 import uic
    print("✅ PyQt5 успешно импортирован")
    using_pyqt6 = False
except ImportError as e:
    print("❌ PyQt5 не найден. Пытаемся использовать PyQt6...")
    try:
        from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
        from PyQt6.QtCore import Qt
        from PyQt6 import uic
        print("✅ PyQt6 найден, используем его")
        using_pyqt6 = True
    except ImportError:
        print("❌ Ни PyQt5, ни PyQt6 не найдены")
        print("Установите PyQt командой:")
        print("   pip install PyQt5")
        print("   или")
        print("   pip install PyQt6")
        input("Нажмите Enter для выхода...")
        sys.exit(1)

class PreviewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        print("🔄 Инициализация UI...")
        
        current_dir = Path(__file__).parent
        ui_file = current_dir / "form.ui"
        qss_file = current_dir / "style.qss"
        icons_dir = current_dir / "icons"
        
        # Проверка наличия файлов
        if not ui_file.exists():
            print(f"❌ Файл {ui_file} не найден")
            QMessageBox.critical(None, "Ошибка", f"UI файл не найден: {ui_file}")
            return
            
        try:
            uic.loadUi(str(ui_file), self)
            print("✅ UI файл загружен успешно")
        except Exception as e:
            print(f"❌ Ошибка загрузки UI: {e}")
            QMessageBox.critical(None, "Ошибка", f"Не удалось загрузить UI: {e}")
            return

        # Загрузка стилей
        if qss_file.exists():
            try:
                with open(qss_file, "r", encoding="utf-8") as f:
                    stylesheet = f.read()
                    self.setStyleSheet(stylesheet)
                    print("✅ Стили применены успешно")
            except Exception as e:
                print(f"⚠️ Ошибка применения стилей: {e}")
        else:
            print(f"⚠️ Файл стилей не найден: {qss_file}")

        # Проверка иконок
        if icons_dir.exists():
            svg_files = list(icons_dir.glob("*.svg"))
            if svg_files:
                print(f"🎨 Найдено {len(svg_files)} иконок SVG")
            else:
                print("⚠️ SVG иконки не найдены в папке icons/")
        else:
            print("⚠️ Папка icons/ не найдена")

        self.setWindowTitle("Qt Components Preview - QAbstractButton Export from Figma")
        print("📊 Компоненты:")
        print("   - QPushButton (sm, md, lg)")
        print("   - QToolButton_icon (sm)")
        print("   - Состояния: active, hover, pressed, disabled")
        
        self.show()
        print("🚀 Предпросмотр запущен успешно")

def main():
    print("=" * 60)
    print("🎨 Qt Components Preview - QAbstractButton from Figma")
    print("=" * 60)
    
    app = QApplication(sys.argv)
    
    # Установка стиля приложения
    app.setStyle('Fusion')
    
    window = PreviewWindow()
    
    try:
        if using_pyqt6:
            result = app.exec()
        else:
            result = app.exec_()
    except KeyboardInterrupt:
        print("\\n⏹️ Приложение закрыто пользователем")
        result = 0
    
    print("👋 Предпросмотр завершен")
    sys.exit(result)

if __name__ == "__main__":
    main()
