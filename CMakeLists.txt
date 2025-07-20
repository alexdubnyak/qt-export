cmake_minimum_required(VERSION 3.16)
project(QtExportFromFigma)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Qt6 components
find_package(Qt6 REQUIRED COMPONENTS Core Widgets UiTools Svg)

# Qt6 automatic MOC, UIC, RCC
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# Add the resource file
qt6_add_resources(RESOURCES resources.qrc)

# Example executable
add_executable(qabstract_button_example
    examples/qabstract_button_example.cpp
    ${RESOURCES}
)

target_link_libraries(qabstract_button_example
    Qt6::Core
    Qt6::Widgets
    Qt6::UiTools
    Qt6::Svg
)

# Copy example files for testing
configure_file(
    ${CMAKE_SOURCE_DIR}/src/widgets/qabstract_button.ui
    ${CMAKE_BINARY_DIR}/qabstract_button.ui
    COPYONLY
)

configure_file(
    ${CMAKE_SOURCE_DIR}/src/styles/qabstract_button.qss
    ${CMAKE_BINARY_DIR}/qabstract_button.qss
    COPYONLY
)

# Set target properties
set_target_properties(qabstract_button_example PROPERTIES
    WIN32_EXECUTABLE TRUE
    MACOSX_BUNDLE TRUE
)

# For development: copy resources to build directory
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    add_custom_command(TARGET qabstract_button_example POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory
        ${CMAKE_SOURCE_DIR}/src/resources
        ${CMAKE_BINARY_DIR}/resources
    )
endif()
