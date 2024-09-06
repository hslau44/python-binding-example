// main.cpp
#include <pybind11/pybind11.h>
#include "calculations.h"

namespace py = pybind11;

double add(double a, double b) {
   Calculator c;
   return c.add(a, b) ;
}

double subtract(double a, double b) {
   Calculator c;
   return c.subtract(a, b) ;
}

PYBIND11_MODULE(SumFunction, m) {
   m.doc() = "pybind11 example module";
   m.def("suming_a_b", &add, "This function adds two input numbers");
   m.def("subtracting_a_b", &subtract, "This function subtract the first input by the second input");
}