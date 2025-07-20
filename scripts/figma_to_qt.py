#!/usr/bin/env python3
"""
Figma to Qt Converter
Автоматический конвертер дизайна из Figma в Qt форматы (.ui и .qss)
"""

import json
import re
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class FigmaNode:
    """Структура узла Figma"""
    id: str
    name: str
    type: str
    x: float
    y: float
    width: float
    height: float
    fills: List[Dict]
    strokes: List[Dict]
    effects: List[Dict]
    characters: Optional[str] = None
    style: Optional[Dict] = None


class FigmaToQtConverter:
    """Конвертер из Figma в Qt форматы"""
    
    def __init__(self):
        self.qt_widgets_map = {
            'FRAME': 'QWidget',
            'RECTANGLE': 'QFrame',
            'TEXT': 'QLabel',
            'BUTTON': 'QPushButton',
            'INPUT': 'QLineEdit',
            'COMPONENT': 'QWidget'
        }
    
    def convert_color(self, figma_color: Dict) -> str:
        """Конвертирует цвет из Figma формата в Qt"""
        if 'color' in figma_color:
            color = figma_color['color']
            r = int(color.get('r', 0) * 255)
            g = int(color.get('g', 0) * 255)
            b = int(color.get('b', 0) * 255)
            a = color.get('a', 1.0)
            
            if a < 1.0:
                return f"rgba({r}, {g}, {b}, {int(a * 255)})"
            else:
                return f"#{r:02x}{g:02x}{b:02x}"
        return "#000000"
    
    def convert_font(self, figma_style: Dict) -> Dict[str, str]:
        """Конвертирует шрифт из Figma в Qt формат"""
        font_props = {}
        
        if 'fontFamily' in figma_style:
            font_props['font-family'] = f'"{figma_style["fontFamily"]}"'
        
        if 'fontSize' in figma_style:
            font_props['font-size'] = f'{figma_style["fontSize"]}px'
        
        if 'fontWeight' in figma_style:
            weight = figma_style['fontWeight']
            if weight >= 700:
                font_props['font-weight'] = 'bold'
            elif weight >= 600:
                font_props['font-weight'] = '600'
            elif weight >= 500:
                font_props['font-weight'] = '500'
        
        if 'letterSpacing' in figma_style:
            font_props['letter-spacing'] = f'{figma_style["letterSpacing"]}px'
        
        return font_props
    
    def generate_qss_styles(self, node: FigmaNode, widget_type: str) -> str:
        """Генерирует QSS стили для виджета"""
        selector = f"{widget_type}#{self._safe_name(node.name)}"
        styles = []
        
        # Фон
        if node.fills:
            for fill in node.fills:
                if fill.get('type') == 'SOLID':
                    bg_color = self.convert_color(fill)
                    styles.append(f"background-color: {bg_color};")
        
        # Границы
        if node.strokes:
            for stroke in node.strokes:
                if stroke.get('type') == 'SOLID':
                    border_color = self.convert_color(stroke)
                    border_width = stroke.get('strokeWeight', 1)
                    styles.append(f"border: {border_width}px solid {border_color};")
        
        # Размеры
        styles.append(f"min-width: {int(node.width)}px;")
        styles.append(f"min-height: {int(node.height)}px;")
        
        # Шрифт (для текстовых элементов)
        if node.style:
            font_props = self.convert_font(node.style)
            for prop, value in font_props.items():
                styles.append(f"{prop}: {value};")
        
        # Скругления
        if 'cornerRadius' in node.__dict__:
            radius = getattr(node, 'cornerRadius', 0)
            if radius > 0:
                styles.append(f"border-radius: {radius}px;")
        
        # Эффекты тени
        if node.effects:
            for effect in node.effects:
                if effect.get('type') == 'DROP_SHADOW':
                    offset = effect.get('offset', {})
                    blur = effect.get('radius', 0)
                    color = self.convert_color(effect.get('color', {}))
                    x = offset.get('x', 0)
                    y = offset.get('y', 0)
                    styles.append(f"box-shadow: {x}px {y}px {blur}px {color};")
        
        style_content = "\\n    ".join(styles)
        return f"{selector} {{\\n    {style_content}\\n}}"
    
    def generate_ui_file(self, node: FigmaNode) -> str:
        """Генерирует .ui файл для виджета"""
        widget_type = self.qt_widgets_map.get(node.type, 'QWidget')
        class_name = self._pascal_case(node.name)
        object_name = self._safe_name(node.name)
        
        ui_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>{class_name}</class>
 <widget class="QWidget" name="{class_name}">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>{int(node.width)}</width>
    <height>{int(node.height)}</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>{node.name}</string>
  </property>
  <widget class="{widget_type}" name="{object_name}">
   <property name="geometry">
    <rect>
     <x>{int(node.x)}</x>
     <y>{int(node.y)}</y>
     <width>{int(node.width)}</width>
     <height>{int(node.height)}</height>
    </rect>
   </property>'''
        
        # Добавляем текст для текстовых элементов
        if node.characters:
            ui_content += f'''
   <property name="text">
    <string>{node.characters}</string>
   </property>'''
        
        ui_content += f'''
   <property name="objectName">
    <string>{object_name}</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>'''
        
        return ui_content
    
    def _safe_name(self, name: str) -> str:
        """Создает безопасное имя для Qt"""
        # Убираем недопустимые символы и заменяем пробелы
        safe = re.sub(r'[^a-zA-Z0-9_]', '_', name)
        safe = re.sub(r'_+', '_', safe).strip('_')
        if safe and safe[0].isdigit():
            safe = f"widget_{safe}"
        return safe or "widget"
    
    def _pascal_case(self, name: str) -> str:
        """Конвертирует в PascalCase"""
        words = re.findall(r'[a-zA-Z0-9]+', name)
        return ''.join(word.capitalize() for word in words)


def main():
    """Основная функция для тестирования"""
    converter = FigmaToQtConverter()
    
    # Пример использования с тестовыми данными
    test_node = FigmaNode(
        id="test_button",
        name="Primary Button",
        type="BUTTON",
        x=0, y=0, width=200, height=48,
        fills=[{"type": "SOLID", "color": {"r": 0, "g": 0.48, "b": 1, "a": 1}}],
        strokes=[],
        effects=[],
        characters="Click Me",
        style={"fontFamily": "Inter", "fontSize": 14, "fontWeight": 600}
    )
    
    # Генерируем файлы
    qss_content = converter.generate_qss_styles(test_node, "QPushButton")
    ui_content = converter.generate_ui_file(test_node)
    
    print("=== Generated QSS ===")
    print(qss_content)
    print("\\n=== Generated UI ===")
    print(ui_content)


if __name__ == "__main__":
    main()
