cmake_minimum_required(VERSION 3.16)
project(FigmaQtExportPreview)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Qt6 components
find_package(Qt6 REQUIRED COMPONENTS Core Widgets UiTools)

# Qt6 automatic MOC, UIC, RCC
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# Preview application executable
add_executable(figma_preview
    main.cpp
)

target_link_libraries(figma_preview
    Qt6::Core
    Qt6::Widgets
    Qt6::UiTools
)

# Copy UI and style files to build directory
configure_file(
    ${CMAKE_SOURCE_DIR}/form.ui
    ${CMAKE_BINARY_DIR}/form.ui
    COPYONLY
)

configure_file(
    ${CMAKE_SOURCE_DIR}/style.qss
    ${CMAKE_BINARY_DIR}/style.qss
    COPYONLY
)

# Set target properties
set_target_properties(figma_preview PROPERTIES
    WIN32_EXECUTABLE TRUE
    MACOSX_BUNDLE TRUE
)

# Install targets
install(TARGETS figma_preview
    BUNDLE DESTINATION .
    RUNTIME DESTINATION bin
)

install(FILES
    form.ui
    style.qss
    DESTINATION bin
)

# For development: copy files post-build
add_custom_command(TARGET figma_preview POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
    ${CMAKE_SOURCE_DIR}/form.ui
    $<TARGET_FILE_DIR:figma_preview>/form.ui
)

add_custom_command(TARGET figma_preview POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
    ${CMAKE_SOURCE_DIR}/style.qss
    $<TARGET_FILE_DIR:figma_preview>/style.qss
)

# Python script convenience (optional)
if(Python3_FOUND OR PYTHON_EXECUTABLE)
    message(STATUS "Python найден - можно использовать preview.py")
    configure_file(
        ${CMAKE_SOURCE_DIR}/preview.py
        ${CMAKE_BINARY_DIR}/preview.py
        COPYONLY
    )
endif()

message(STATUS "=== Figma Qt Export Preview ===")
message(STATUS "Сборка: ${CMAKE_BUILD_TYPE}")
message(STATUS "Qt версия: ${Qt6_VERSION}")
message(STATUS "C++ стандарт: ${CMAKE_CXX_STANDARD}")
message(STATUS "================================")
