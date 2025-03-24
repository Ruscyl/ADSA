def add_school_method(i1, i2, base):
    # Implement school method addition
    result = []
    carry = 0
    i1 = list(map(int, reversed(i1)))
    i2 = list(map(int, reversed(i2)))
    
    max_len = max(len(i1), len(i2))
    
    for i in range(max_len):
        digit1 = i1[i] if i < len(i1) else 0
        digit2 = i2[i] if i < len(i2) else 0
        sum_digits = digit1 + digit2 + carry
        carry = sum_digits // base
        result.append(sum_digits % base)
    
    if carry:
        result.append(carry)
    
    return ''.join(map(str, reversed(result)))


def karatsuba_multiply(i1, i2, base):
    # Karatsuba multiplication in base 10
    if len(i1) == 1 and len(i2) == 1:
        return str(int(i1) * int(i2))
    
    n = max(len(i1), len(i2))
    half = n // 2
    
    # Split the numbers
    high1, low1 = i1[:-half], i1[-half:]
    high2, low2 = i2[:-half], i2[-half:]
    
    # Recursively compute three products
    z0 = karatsuba_multiply(low1, low2, base)
    z1 = karatsuba_multiply(str(int(low1) + int(high1)), str(int(low2) + int(high2)), base)
    z2 = karatsuba_multiply(high1, high2, base)
    
    # Combine the three parts
    product = int(z2) * base ** (2 * half) + (int(z1) - int(z2) - int(z0)) * base ** half + int(z0)
    
    return str(product)


def divide_integer(i1, i2, base):
    # Integer division
    return str(int(i1) // int(i2))


def to_base_b(num_str, base):
    # Convert a number string to base `b`
    num = int(num_str)
    if num == 0:
        return "0"
    result = []
    while num:
        result.append(str(num % base))
        num //= base
    return ''.join(reversed(result))


def main():
    i1, i2, base = input().split()
    base = int(base)
    
    # Step 1: Perform school method addition
    addition_result = add_school_method(i1, i2, base)
    
    # Step 2: Perform Karatsuba multiplication
    multiplication_result = karatsuba_multiply(i1, i2, base)
    
    # Step 3: Perform integer division (only for postgraduates)
    division_result = divide_integer(i1, i2, base)
    
    # Convert results to the correct base and print
    print(to_base_b(addition_result, base), to_base_b(multiplication_result, base), to_base_b(division_result, base))

if __name__ == "__main__":
    main()
