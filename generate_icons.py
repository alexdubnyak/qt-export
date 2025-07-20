#!/usr/bin/env python3
"""
Icon Generator for Qt Export
Создает SVG иконки для всех состояний кнопок
"""

import os
from pathlib import Path

def create_icon_svg(name, state, color_scheme):
    """Создает SVG иконку с заданной цветовой схемой"""
    colors = {
        'active': {'bg': '#bbbbbb', 'circle': '#3f3f3f', 'center': '#efefef'},
        'hover': {'bg': '#a8a8a8', 'circle': '#2a2a2a', 'center': '#e0e0e0'},
        'pressed': {'bg': '#999999', 'circle': '#1a1a1a', 'center': '#d3d3d3'},
        'disabled': {'bg': '#cccccc', 'circle': '#8a8a8a', 'center': '#f5f5f5'}
    }
    
    scheme = colors.get(state, colors['active'])
    
    svg_content = f'''<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- {state.title()} state icon for {name} -->
  <rect x="2" y="2" width="12" height="12" rx="2" fill="{scheme['bg']}"/>
  <circle cx="8" cy="8" r="3" fill="{scheme['circle']}"/>
  <circle cx="8" cy="8" r="1.5" fill="{scheme['center']}"/>
</svg>'''
    
    return svg_content

def generate_all_icons():
    """Генерирует все иконки для компонентов"""
    icons_dir = Path("icons")
    icons_dir.mkdir(exist_ok=True)
    
    # Определяем компоненты
    components = [
        # QPushButton small
        ("qpushbutton_sm_active_0", "active"),
        ("qpushbutton_sm_hover_1", "hover"),
        ("qpushbutton_sm_pressed_2", "pressed"),
        ("qpushbutton_sm_disabled_3", "disabled"),
        
        # QToolButton small
        ("qtoolbutton_icon_sm_active_4", "active"),
        ("qtoolbutton_icon_sm_hover_5", "hover"),
        ("qtoolbutton_icon_sm_pressed_6", "pressed"),
        ("qtoolbutton_icon_sm_disabled_7", "disabled"),
        
        # QPushButton medium
        ("qpushbutton_md_active_8", "active"),
        ("qpushbutton_md_hover_9", "hover"),
        ("qpushbutton_md_pressed_10", "pressed"),
        ("qpushbutton_md_disabled_11", "disabled"),
        
        # QPushButton large
        ("qpushbutton_lg_active_12", "active"),
        ("qpushbutton_lg_hover_13", "hover"),
        ("qpushbutton_lg_pressed_14", "pressed"),
        ("qpushbutton_lg_disabled_15", "disabled"),
    ]
    
    print("🎨 Генерация иконок...")
    
    for component_name, state in components:
        svg_content = create_icon_svg(component_name, state, state)
        icon_path = icons_dir / f"{component_name}.svg"
        
        with open(icon_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        
        print(f"✅ Создана иконка: {icon_path}")
    
    print(f"🎉 Создано {len(components)} иконок в папке {icons_dir}")

if __name__ == "__main__":
    generate_all_icons()
