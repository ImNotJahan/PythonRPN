# PythonRPN
A python implementation of [reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) designed for the TI-84 Plus CE Python.

Supports
* Basic arithmetic \(+, -, /, \*\)
* Logarithms \("log\(\)"\)
* Trigonometry functions \("sin\(\)", "cos\(\)", "tan\(\)", "asin\(\)", "acos\(\)", "atan\(\)"\)
* Radian degrees conversions \("radians\(\)", "degrees\(\)"\)
* Exponents and roots \("**", "**-", "**2", "**-1"\)
* ans, pi, e \("\_", "pi", "e"\)

## Examples
* `3 4 × 5 6 × +` returns `42.0`
* `100 10 log() 10 **` returns `1024.0`
* `3 2 /` returns `1.5`
