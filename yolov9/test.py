def factorial(n):
    # Calculate the factorial of a number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_S2():
    S2 = 0
    for i in range(1, 21):
        S2 += factorial(i)
    return S2

# Calculate S2
result = calculate_S2()

# Print the result
print(f"S2 = {result}")

