cmake_minimum_required(VERSION 3.12)
project(emulation_simulation)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(pybind11 REQUIRED)

pybind11_add_module(emulator_module
    src/cpp/bindings/emulator_bindings.cpp
    src/cpp/src/chip8_emulator.cpp
)

target_include_directories(emulator_module PRIVATE src/cpp/include)