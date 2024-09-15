def count_trailing_zeros(number):
    if number < 0:
        return "number can not be negative"
    count = 0 
    i = 5

    while number // i > 0:
        count += number // i
        i *= 5

    return count
print(count_trailing_zeros(7))
print(count_trailing_zeros(-10))