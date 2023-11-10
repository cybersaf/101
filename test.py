memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:       
        result = fibonacci(n - 1) + fibonacci(n - 2)
        memo[n] = result
        return result
    
n = 10
print(f"Fibonacci({n}) = {fibonacci(n)}")

