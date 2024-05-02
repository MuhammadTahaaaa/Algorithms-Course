import time

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def test_factorial_functions(values):
    results = []
    for n in values:
        # Testing the iterative function with high-resolution timer
        start_time = time.perf_counter()
        result_iterative = factorial_iterative(n)
        time_iterative = time.perf_counter() - start_time

        # Testing the recursive function with high-resolution timer
        start_time = time.perf_counter()
        try:
            result_recursive = factorial_recursive(n)
            time_recursive = time.perf_counter() - start_time
            overflow = False
        except RecursionError:
            result_recursive = 'Stack Overflow'
            time_recursive = 'N/A'
            overflow = True

        # Store the results
        results.append({
            'n': n,
            'iterative_result': result_iterative,
            'iterative_time': time_iterative,
            'recursive_result': result_recursive,
            'recursive_time': time_recursive,
            'overflow': overflow
        })

    return results

# List of values to test
test_values = [5, 10, 20, 30, 40, 50, 100]

# Execute the test
results = test_factorial_functions(test_values)

# Print the results
for result in results:
    print(f"n={result['n']}:")
    print(f"  Iterative: Result = {result['iterative_result']}, Time = {result['iterative_time']:.6f} sec")
    print(f"  Recursive: Result = {result['recursive_result']}, Time = {result.get('recursive_time', 'N/A')} sec")
    if result['overflow']:
        print("  Stack Overflow occurred in recursive calculation")
