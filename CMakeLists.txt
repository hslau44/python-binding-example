# cmake_minimum_required(VERSION 3.15...3.29)
# project(example LANGUAGES CXX)

# set(PYBIND11_FINDPYTHON ON)
# find_package(pybind11 CONFIG REQUIRED)
# add_subdirectory(./extern/pybind11)

# pybind11_add_module(example example.cpp)
# install(TARGETS example DESTINATION .)

cmake_minimum_required(VERSION 3.0.0)
project(Projectpybind11 VERSION 0.1.0)

include(CTest)
enable_testing()

add_subdirectory(extern/pybind11)
pybind11_add_module(SumFunction main.cpp)

include_directories(${PROJECT_SOURCE_DIR}/inc)
add_subdirectory(src)
set_target_properties(cal PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_link_libraries(SumFunction PRIVATE cal)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)