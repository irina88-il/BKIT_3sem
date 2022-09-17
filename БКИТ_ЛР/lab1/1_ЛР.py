import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''

    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        while True:
            try:
                # Вводим с клавиатуры
                print(prompt)
                coef_str = input()
                # Переводим строку в действительное число
                coef = float(coef_str)
                break
            except ValueError:
                print("Вы ввели не число. Попробуйте снова. ")
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней ,биквадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        y = -b / (2.0*a)
        if y >= 0:
            root_1 = math.sqrt(y)
            root_2 = -math.sqrt(y)
            result.append(root_1)
            result.append(root_2)      
    elif D > 0.0:
        sqD = math.sqrt(D)
        y1 = (-b + sqD) / (2.0*a)
        y2 = (-b - sqD) / (2.0*a)
        if (y1 >= 0):
            root1_1 = math.sqrt(y1)
            root1_2 = -math.sqrt(y1)
            result.append(root1_1)
            result.append(root1_2)
        if (y2 >= 0):
            root2_1 = math.sqrt(y2)
            root2_2 = -math.sqrt(y2)
            result.append(root2_1)
            result.append(root2_2)
    return result
    
def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0 or a == 0 :
        print('Нет корней')
    elif len_roots == 2:
        print('Два корня: {:.2f} и {:.2f}'.format(roots[0], roots[1]))
    elif len_roots == 4:
        print('Четыре корня: {:.2f}, {:.2f}, {:.2f} и {:.2f}'.format(roots[0], roots[1], roots[2], roots[3]))
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
