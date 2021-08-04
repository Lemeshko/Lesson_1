your_num = int(input('Введите целое положительное число:  '))
greatest_digit = 0
num = your_num
while num > 0:
    digit = num % 10
    if digit > greatest_digit:
        greatest_digit = digit
        if greatest_digit == 9:
            break
    num = num // 10

print (f"Наибольшая цифра в числе {your_num} равна {greatest_digit}")
