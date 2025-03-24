def convert_to_base_10(num_str, base):
    """ Convert a number from base `base` to base 10 """
    return int(num_str, base)

def convert_from_base_10(num, base):
    """ Convert a number from base 10 to the given base `base` """
    if num == 0:
        return "0"
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return ''.join(str(x) for x in digits[::-1])

def is_valid_digit_for_base(digit, base):
    """ Checks if a digit is valid for the given base """
    return 0 <= int(digit) < base

def school_method_addition(a, b, base):
    """ Add two numbers in base `base` using the school method """
    a_str, b_str = str(a), str(b)
    
    # Check that all digits are valid for the base
    for digit in a_str + b_str:
        if not is_valid_digit_for_base(digit, base):
            raise ValueError(f"Invalid digit '{digit}' for base {base}")
    
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    
    result = []
    carry = 0
    
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(a_str[i], base) + int(b_str[i], base) + carry
        result.append(str(digit_sum % base))
        carry = digit_sum // base
    
    if carry:
        result.append(str(carry))
    
    result.reverse()
    return convert_from_base_10(int(''.join(result), base), base)

def karatsuba(x, y):
    """ Perform Karatsuba multiplication for two integers x and y """
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    
    high1, low1 = divmod(x, 10**half)
    high2, low2 = divmod(y, 10**half)
    
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)
    
    return (z2 * 10**(2 * half)) + ((z1 - z2 - z0) * 10**half) + z0

def perform_operations(I1, I2, B):
    """ Perform the required operations: sum, product, and division """
    I1_base_10 = convert_to_base_10(I1, B)
    I2_base_10 = convert_to_base_10(I2, B)
    
    # 1. School Method Addition
    sum_result = school_method_addition(I1_base_10, I2_base_10, B)
    
    # 2. Karatsuba Multiplication
    product_result = karatsuba(I1_base_10, I2_base_10)
    
    # 3. Integer Division (rounded down)
    division_result = I1_base_10 // I2_base_10
    
    # Convert results to base B
    sum_result_base_B = convert_from_base_10(sum_result, B)
    product_result_base_B = convert_from_base_10(product_result, B)
    division_result_base_B = convert_from_base_10(division_result, B)
    
    return f"{sum_result_base_B} {product_result_base_B} {division_result_base_B}"

# Main function to process input and output the results
if __name__ == "__main__":
    # Read the input
    I1, I2, B = input().split()
    B = int(B)
    
    # Perform operations and print results
    result = perform_operations(I1, I2, B)
    print(result)
