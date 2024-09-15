def number_to_roman(number):
    if number < 0:
        return "number can not be less than 0"
    
    roman_numerals = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 
        100: "C", 90: "XC", 50: "L", 40: "XL", 
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    num_text = ""
    for value in roman_numerals:
        while number >= value:
            num_text += roman_numerals[value]
            number -= value
    return num_text
print(number_to_roman(101))
print(number_to_roman(-1))