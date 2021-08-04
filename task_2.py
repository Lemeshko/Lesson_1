time = int(input('Введите время в секундах: '))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print("Время в формате чч:мм:сс:  " f"{hours:02}:{minutes:02}:{seconds:02}")
