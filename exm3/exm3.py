def number_to_thai_text(number):
    if number < 0:
        return "number can not be less than 0"
    if number > 10_000_000:
        return "number can not be more than 10,000,000"

    num_texts = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    unit_texts = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

    if number == 0:
        return "ศูนย์"

    num_text = ""
    digits = list(str(number))  
    num_len = len(digits)

    for i in range(num_len):
        digit = int(digits[i])
        position = num_len - i - 1

        if digit == 0:
            continue

        if position == 1 and digit == 1:
            num_text += "สิบ"
        elif position == 1 and digit == 2:
            num_text += "ยี่สิบ"
        elif position == 0 and digit == 1 and num_len > 1:
            num_text += "เอ็ด"
        else:
            num_text += num_texts[digit] + unit_texts[position]

    return num_text

print(number_to_thai_text(101))  
print(number_to_thai_text(-1))   
