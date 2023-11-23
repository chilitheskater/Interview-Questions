# Given an integer, convert it to a roman numeral.

def int_to_roman(num): #The function `int_to_roman` takes an integer `num` as input and converts it to its Roman numeral representation.
    # List of tuples containing Roman numeral and its value 
    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]

    result = "" #The variable result is initialized as an empty string. This variable will store the final Roman numeral representation

    for roman, value in roman_numerals:
        while num >= value:
            result += roman
            num -= value

    return result

 


# Example usage:
number = 27
roman_numeral = int_to_roman(number)
print(f"The Roman numeral representation of {number} is: {roman_numeral}")
