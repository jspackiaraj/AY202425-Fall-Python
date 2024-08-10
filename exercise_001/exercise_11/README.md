In the program, `num**0.5` is used to compute the square root of `num`. The `**` operator in Python is the exponentiation operator, which raises a number to the power of another number. 

Here's how it works in the context of the program:

- `num**0.5` calculates the square root of `num`. For example, if `num` is 25, then `25**0.5` results in 5.0.

### Why Use `num**0.5`?

The program is designed to find and print prime numbers between 2 and 100. For each number (`num`), it checks if it is a prime number by testing for divisibility:

1. **Optimisation:** Instead of checking divisibility up to `num-1`, it’s sufficient to check up to the square root of `num`. This is because if `num` can be factored into two factors, one of them must be less than or equal to the square root of `num`. If `num` is divisible by any number greater than its square root, then it must also be divisible by a number smaller than or equal to the square root.

2. **Efficiency:** By checking divisibility only up to `int(num**0.5) + 1`, the program reduces the number of iterations, making it more efficient.

### Example

For `num = 36`:
- `36**0.5` gives `6.0`.
- The program checks divisibility up to `6` (i.e., integers from 2 to 6).

This optimisation significantly reduces the number of iterations required to determine if a number is prime.