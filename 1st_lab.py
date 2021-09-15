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
        # Вводим с клавиатуры
        tester = False
        coef = 0.0
        while (tester != True):
            print(prompt)
            coef_str = input()
            try:
                coef = float(coef_str)
                tester = True
            except ValueError:
                tester = False
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root > 0:
        	root1 = math.sqrt(root)
        	root2 = -1 * math.sqrt(root)
        	result.append(root1)
        	result.append(root2)
        elif root == 0:
            results.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        if root1 > 0:
            rooter1 = math.sqrt(root1)
            rooter2 = -1 * math.sqrt(root1)
            result.append(rooter1)
            result.append(rooter2)
        elif root1 ==0:
            result.append(root1)
        root2 = (-b - sqD) / (2.0 * a)
        if root2 > 0:
            rooter1 = math.sqrt(root2)
            rooter2 = -1 * math.sqrt(root2)
            result.append(rooter1)
            result.append(rooter2)
        elif root2 ==0:
            result.append(root2)
    return result
    
def linar(b,c):
    result = []
    root = 0.0
    root = -1 * c / b
    if root > 0:
    	root1 = math.sqrt(root)
    	root2 = -1 * math.sqrt(root)
    	result.append(root1)
    	result.append(root2)
    elif root == 0:
    	result.append(root)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots =[]
    if a == 0:
    	if c ==0:
    	    if b ==0:
    	    	roots = [3,3,3,3,3]
    	    else:
    	    	roots = 0
    	elif b ==0:
    	    roots = []
    	else:
    	    roots = linar(b, c)
    # Вычисление корней
    else:
        roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} , {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} , {} , {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    elif len_roots == 5:
        print('х - любое число')


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
