import random
def generate_random_number():
    min_value = int(input("Введите наименьшее значение: "))
    max_value = int(input("Введите наибольшее значение: "))
    if min_value > max_value:
        min_value, max_value = max_value, min_value
    random_number = random.randint(min_value, max_value)
    return random_number
result = generate_random_number()
print(f"Случайное число из заданного диапазона: {result}")