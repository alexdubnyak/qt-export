cmake_minimum_required(VERSION 3.16)
project(QtExportFromFigma VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Qt6 components
find_package(Qt6 REQUIRED COMPONENTS Core Widgets UiTools Svg)

# Qt6 automatic MOC, UIC, RCC
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# Copy UI and QSS files to build directory
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

# Copy icons directory
file(COPY ${CMAKE_SOURCE_DIR}/icons
     DESTINATION ${CMAKE_BINARY_DIR})

# Main preview executable
add_executable(qt_preview
    main.cpp
)

target_link_libraries(qt_preview
    Qt6::Core
    Qt6::Widgets
    Qt6::UiTools
    Qt6::Svg
)

# Set target properties
set_target_properties(qt_preview PROPERTIES
    WIN32_EXECUTABLE TRUE
    MACOSX_BUNDLE TRUE
)

# Install targets
install(TARGETS qt_preview
    BUNDLE DESTINATION .
    RUNTIME DESTINATION bin
)

install(FILES form.ui style.qss
    DESTINATION bin
)

install(DIRECTORY icons
    DESTINATION bin
)

# Custom target for generating icons
add_custom_target(generate_icons
    COMMAND ${CMAKE_COMMAND} -E env python3 ${CMAKE_SOURCE_DIR}/generate_icons.py
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Generating SVG icons for components"
)

# Custom target for Python preview
add_custom_target(python_preview
    COMMAND ${CMAKE_COMMAND} -E env python3 ${CMAKE_SOURCE_DIR}/preview.py
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Running Python preview"
)

# Help target
add_custom_target(help
    COMMAND ${CMAKE_COMMAND} -E echo "Available targets:"
    COMMAND ${CMAKE_COMMAND} -E echo "  qt_preview      - Build and run C++ Qt preview"
    COMMAND ${CMAKE_COMMAND} -E echo "  python_preview  - Run Python Qt preview"
    COMMAND ${CMAKE_COMMAND} -E echo "  generate_icons  - Generate SVG icons"
    COMMAND ${CMAKE_COMMAND} -E echo ""
    COMMAND ${CMAKE_COMMAND} -E echo "Usage:"
    COMMAND ${CMAKE_COMMAND} -E echo "  mkdir build && cd build"
    COMMAND ${CMAKE_COMMAND} -E echo "  cmake .."
    COMMAND ${CMAKE_COMMAND} -E echo "  make qt_preview"
    COMMAND ${CMAKE_COMMAND} -E echo "  ./qt_preview"
)

# Print configuration info
message(STATUS "Project: ${PROJECT_NAME} v${PROJECT_VERSION}")
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "Install prefix: ${CMAKE_INSTALL_PREFIX}")
