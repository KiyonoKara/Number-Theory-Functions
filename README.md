# Basic Number Theory Functions

This repository serves as a place where useful functions usually related to number theory are stored.  
Please feel free to improve upon these functions or propose them. 

## Main Function(s)
1. Applying Number Theory to programming.
2. Cryptography with Number Theory functions.
3. Useful for finding certain answers from sets of data.  


Side Note:  
>! You're probably better off using these for your Number Theory needs.

## Documentation
As a general overview, these functions primarily serve to be snippets which people can refer to.  
The documentation predominantly exists here since these functions can be confusing and most definitely need some background.

As seen below, there are some core functions that will be in the documentation.

### Greatest Common Divisor
This function returns the **Greatest Common Divisor** (GCD) based on two integers given which are `a` and `b`.
```python
gcd = gcd(10, 20)
# Returns 10
```
```python
gcd = gcd(20, 10)
# Returns 10
```
**Note:** The order of parameters do not matter.

### Euclidean Algorithm
Returns the **Greatest Common Divisor** (GCD) as `g`, `u` and `v` are also returned which correspond to the equation:  
```ua + vb = gcd(a, b)``` with two given integers, `a` and `b`. There are two separate functions that return the same values but are written differently.  

**Returns three callable values**
```python
g, u, v = euclideanAlgorithm1(20, 30)
# Returns 10, -1, 1
#         g,   u, v
```   

**Returns an array which can still be called upon, just differently**
```python
eu = euclideanAlgorithm2(20, 30)
# Returns (10, -1, 1)
#         (g,   u, v)
```
**Note:** The order of parameters do not matter.

**Documentation is still in progress, will add more to these.**

## Contributing
Pull requests are welcome. For bugs and/or flaws in the functions, please open an issue.

## License
[]()