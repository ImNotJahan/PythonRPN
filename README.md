# PythonRPN
A python implementation of [reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) designed for the TI-84 Plus CE Python.

Supports
* Basic arithmetic \(+, -, /, \*\)
* Logarithms \("log\(\)"\)
* Trigonometry functions \("sin\(\)", "cos\(\)", "tan\(\)", "asin\(\)", "acos\(\)", "atan\(\)"\)
* Radian degrees conversions \("radians\(\)", "degrees\(\)"\)
* Exponents and roots \("\*\*", "\*\*-", "\*\*2", "\*\*-1"\)
* ans, pi, e \("\_", "pi", "e"\)
* Comparisons \("==", "!=", "<", "<=", ">", ">="\)
* Boolean operators \("and", "or", "not"\)
* Variables
* Modulus \("%"\)

## Examples
* `3 4 × 5 6 × +` returns `42.0`
* `100 10 log() 10 **` returns `1024.0`
* `3 2 /` returns `1.5`

## Variables
To use a variable, just the name is typed, but to modify or create a variable () + variable name is typed

The variable operators and functions are =, +=, -=, *=, /=, %=, **=, ++, --

Example:
```
()x 0 =
()x += 100
()x --
x + 5
104
```