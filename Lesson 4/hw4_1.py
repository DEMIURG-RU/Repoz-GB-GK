from sys import argv

def income():
    try:
        time_w, bet, bonus = map(float, argv[1:])
        return(f"Ваш доход за указанное время составит: {time_w * bet + bonus}")
    except ValueError:
        return("Введите только сколько времени вы отрбаотали, ставку и бонус")

income()