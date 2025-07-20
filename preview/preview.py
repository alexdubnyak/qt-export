#!/usr/bin/env python3
"""
Qt Components Preview - Figma Export
Загружает form.ui и применяет style.qss для предпросмотра компонентов
Сгенерировано автоматически системой экспорта Figma → Qt
"""

import sys
import os
from pathlib import Path

if sys.version_info < (3, 6):
    print("❌ Требуется Python 3.6 или выше")
    sys.exit(1)

# Попытка импорта PyQt5/PyQt6
try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
    from PyQt5.QtCore import Qt
    from PyQt5 import uic
    print("✅ PyQt5 успешно импортирован")
    QT_VERSION = 5
except ImportError:
    try:
        from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
        from PyQt6.QtCore import Qt
        from PyQt6 import uic
        print("✅ PyQt6 найден, используем его")
        QT_VERSION = 6
    except ImportError:
        print("❌ Ни PyQt5, ни PyQt6 не найдены")
        print("Установите один из них:")
        print("   pip install PyQt5")
        print("   pip install PyQt6")
        input("Нажмите Enter для выхода...")
        sys.exit(1)

class FigmaPreviewWindow(QMainWindow):
    """Главное окно предпросмотра компонентов экспортированных из Figma"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_interactions()

    def init_ui(self):
        """Инициализация пользовательского интерфейса"""
        print("🔄 Инициализация UI...")
        
        current_dir = Path(__file__).parent
        ui_file = current_dir / "form.ui"
        qss_file = current_dir / "style.qss"
        
        # Проверка существования файлов
        if not ui_file.exists():
            print(f"❌ Файл {ui_file} не найден")
            self.show_error(f"UI файл не найден: {ui_file}")
            return
            
        # Загрузка UI файла
        try:
            uic.loadUi(str(ui_file), self)
            print("✅ UI файл загружен успешно")
        except Exception as e:
            print(f"❌ Ошибка загрузки UI: {e}")
            self.show_error(f"Ошибка загрузки UI: {e}")
            return

        # Применение стилей
        if qss_file.exists():
            try:
                with open(qss_file, "r", encoding="utf-8") as f:
                    stylesheet = f.read()
                    self.setStyleSheet(stylesheet)
                    print("✅ Стили применены успешно")
            except Exception as e:
                print(f"⚠️ Ошибка применения стилей: {e}")
        else:
            print("⚠️ Файл стилей не найден, используются стандартные стили")

        # Настройка окна
        self.setWindowTitle("🎨 Figma Qt Export - Components Preview")
        self.resize(1200, 800)
        self.center_window()

    def setup_interactions(self):
        """Настройка интерактивности компонентов"""
        print("🔧 Настройка интерактивности...")
        
        # Найти все кнопки для демонстрации интерактивности
        buttons = self.findChildren(QWidget)
        interactive_count = 0
        
        for widget in buttons:
            if hasattr(widget, 'clicked'):  # QPushButton, QToolButton
                widget.clicked.connect(
                    lambda checked, w=widget: self.on_button_clicked(w)
                )
                interactive_count += 1
        
        print(f"✅ Настроено {interactive_count} интерактивных элементов")

    def center_window(self):
        """Центрирование окна на экране"""
        if QT_VERSION == 5:
            from PyQt5.QtWidgets import QDesktopWidget
            screen = QDesktopWidget().screenGeometry()
        else:  # PyQt6
            screen = self.screen().geometry()
        
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) // 2,
            (screen.height() - size.height()) // 2
        )

    def on_button_clicked(self, widget):
        """Обработчик клика по кнопке"""
        button_name = widget.objectName()
        tooltip = widget.toolTip() if hasattr(widget, 'toolTip') else "No tooltip"
        
        print(f"🖱️ Клик по кнопке: {button_name}")
        print(f"   Информация: {tooltip}")
        
        # Показать информацию о кнопке
        self.show_button_info(widget)

    def show_button_info(self, widget):
        """Показать подробную информацию о кнопке"""
        info = []
        info.append(f"Object Name: {widget.objectName()}")
        
        if hasattr(widget, 'text') and widget.text():
            info.append(f"Text: {widget.text()}")
        
        if hasattr(widget, 'toolTip') and widget.toolTip():
            info.append(f"Tooltip: {widget.toolTip()}")
        
        info.append(f"Class: {widget.__class__.__name__}")
        info.append(f"Size: {widget.size().width()}×{widget.size().height()}")
        info.append(f"Position: ({widget.x()}, {widget.y()})")
        info.append(f"Enabled: {widget.isEnabled()}")
        
        message = "\\n".join(info)
        print(f"ℹ️ Информация о компоненте:\\n{message}")

    def show_error(self, message):
        """Показать сообщение об ошибке"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Ошибка загрузки")
        msg.setText(message)
        msg.exec_()

def check_environment():
    """Проверка окружения и зависимостей"""
    print("🔍 Проверка окружения...")
    
    current_dir = Path(__file__).parent
    
    # Проверка файлов
    required_files = ['form.ui', 'style.qss']
    missing_files = []
    
    for file_name in required_files:
        if not (current_dir / file_name).exists():
            missing_files.append(file_name)
    
    if missing_files:
        print(f"⚠️ Отсутствуют файлы: {', '.join(missing_files)}")
        return False
    
    print("✅ Все необходимые файлы найдены")
    
    # Проверка директории с иконками (опционально)
    icons_dir = current_dir / "icons"
    if icons_dir.exists():
        svg_files = list(icons_dir.glob("*.svg"))
        print(f"🎨 Найдено {len(svg_files)} SVG иконок")
    else:
        print("ℹ️ Директория icons не найдена (это нормально)")
    
    return True

def main():
    """Главная функция"""
    print("🚀 Запуск Qt Components Preview")
    print("📱 Система экспорта Figma → Qt")
    print("-" * 50)
    
    # Проверка окружения
    if not check_environment():
        print("❌ Проверка окружения не пройдена")
        input("Нажмите Enter для выхода...")
        return
    
    # Создание приложения
    app = QApplication(sys.argv)
    app.setApplicationName("Figma Qt Export Preview")
    app.setApplicationVersion("1.0.0")
    
    # Создание и показ главного окна
    try:
        window = FigmaPreviewWindow()
        window.show()
        
        print("✅ Окно предпросмотра открыто")
        print("ℹ️ Нажмите на любую кнопку для просмотра информации")
        print("-" * 50)
        
        # Запуск приложения
        if QT_VERSION == 5:
            result = app.exec_()
        else:  # PyQt6
            result = app.exec()
            
        sys.exit(result)
        
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
