#include "calculations.h"

double Calculator::add(double a, double b)
{
    return sumation(a, b);
}

double Calculator::subtract(double a, double b)
{
    return subtraction(a, b);
}

double Calculator::times(double a, double b)
{
    return a*b;
}

double Calculator::divide(double a, double b)
{
    if (b == 0) {
        throw "Division by zero is not allowed.";
    }
    return a / b;
}

double sumation(double a, double b)
{
    return a + b;
}

double subtraction(double a, double b)
{
    return a - b;
}
