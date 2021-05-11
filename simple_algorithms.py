# Данные примеры являются элементарными. Название "массив", применяемое в этих примерах, используется исключительно
# для наглядности. На самом же деле тип данных list() в  Python не является массивом в классическом понимании этого
# термина.

# Данный материал является конспектом видеолекций Тимофея Хирьянова 'Алгоритмы на Python 3'
# при этом код может отличаться от оригинального, так как я не тупо копипастил, а писал самостоятельно в процессе
# освоения материала.

# https://www.youtube.com/channel/UCQfwKTJdCmiA6cXAY0PNRJw   -ссылка на канал Тимофея Хирьянова

# создадим функцию, которая принимает массив, диапазон и искомое число. Ожидаемые типы укажем явно.
def array_search(a: list, n: int, x: int):
    """
    Алгоритм лнейного поиска в массиве.
    Осуществляет поиск числа х в массиве а от 0 до n-1 включительно
    Возвращает индекс элемента х в массиве а.
    """
    for i in range(n):  # запускаем цикл в диапазоне n, мы получим n итерраций, при этом временная переменная i
        # так же будет являться индексом, по которому далее мы будем обращаться к каждому элементу массива по порядку;
        if a[i] == x:  # проверяем совпадает ли элемент массива а по индексу i с искомым числом х;
            return i  # возвращаем индекс, если такое число находится


# array = [1, 2, 3, 4, 5]  # задаем массив;
# explicit_range = len(array)  # задаем диапазон (в данном случае это будет длинна всего массива);
# number = 3  # искомое число;
#
# print(f'Индекс числа {number} в массиве {array} равен {array_search(array, explicit_range, number)}')


# создадим функцию, которая принимает массив и диапазон. Ожидаемые типы укажем явно.
def invert_array(a: list, n: int):
    """
    Обращение массива (поворот задом-наперёд)
    в рамках индексов от 0 до n-1
    """
    for i in range(n // 2):  # запускаем цикл в диапазоне n//2, мы получим n//2 итерраций, дальше станет понятно почему;
        a[i], a[n - 1 - i] = a[n - 1 - i], a[i]  # а вот тут уже используем одну из фишек Python - множественное
        # присваивание;

        #  вот очень важно понимать почему range(n//2), а не range(n). А дело все в том, что если мы используем
        #  range(n), то мы получим избыточное количество итераций. Это приведет к тому, что мы сначала перевернем
        #  массив, а затем переверне его еще раз, приведя тем самым к первоначальному виду. Вот что бы этого
        #  не произошло, мы и используем range(n//2), тем самым останавливаемся как бы на середине процесса.
        return a


# array = [1, 2, 3, 4, 5]  # задаем массив;
# explicit_range = len(array)  # задаем диапазон (в данном случае это будет длинна всего массива)
# print(invert_array(array, explicit_range))

# создадим функцию, которая принимает массив, диапазон и направление влево или вправо. Ожидаемые типы укажем явно.
def cyclic_shift_in_an_array(a: list, n: int, d: str):
    """
    Циклический сдвиг в массиве.
    Возвращает преобразованный массив сдвинутый влево или вправо.
    """
    # Проще говоря: берем элемент с индексом 0 и переставляем его в конец, при этом элемент с индексом 1 становится
    # на место элемента с индексом 0 и тд - это циклический сдвиг влево. А если мы возьмем последний элемен и
    # переставим его на место элемента с индексом 0, при этом предпоследний элемент становится на место последнего
    # и тд - это циклический сдвиг вправо.

    # алгоритмы циклического сдвига влево или вправо несколько отличаются между собой, так что сделаем условие проверки
    # значения переменной d, которая будет являться нашим маркером направления.
    if d == 'left':  # для d == 'left'
        tmp = a[0]  # создаем новую переменную и кладем в нее первый элемент массива;
        for i in range(n - 1):  # запускаем цикл как раньше, но количество итераций уменьшаем на 1;
            a[i] = a[i + 1]  # переприсваиваем элементу с индексом i значение элемента с индексом i + 1,
            # то есть следующего;
        a[n - 1] = tmp  # ну а последний элемент мы меняем на первый.

    elif d == 'right':  # для d == 'right'
        tmp = a[n - 1]  # создаем новую переменную и кладем в нее последний элемент массива
        for i in range(n - 2, -1, -1):  # запускаем цикл, но в это раз в range явно указываем, что пойдем мы от
            # предпоследнего элемента до 0, с шагом -1, кторый как раз явно указывает, что пойдем мы в обратнои порядке;
            a[i + 1] = a[i]  # переприсваиваем каждому следующему элементу значение текущего;
        a[0] = tmp  # ну а первый элемент меняем на последний, который заранее сохранили в отдельной переменной.

    return a


# array = [1, 2, 3, 4, 5]  # задаем массив;
# explicit_range = len(array)  # задаем диапазон (в данном случае это будет длинна всего массива);
# direction = 'right'  # указываем направление
# print(cyclic_shift_in_an_array(array, explicit_range, direction))


def the_sieve_of_eratosthenes(n: int):
    """
    Решето Эратосфена.
    Возвращает все простые числа до некоторого числа n.
    """
    # По классике данный алгоритм возвращает простые числа из некоторой последовательности, но мы сделаем несколько
    # интереснее. Наша функция не будет что-либо возвращать, она буде просто печатать последовательность чисел
    # с комментариями по каждому числу. Более того, мы притворимся, что list() сам не умеет как бы контролировать
    # заполненность и используем переменную n в качестве  контроллера этой заполненности.

    # создадим массив, заполненный bool значениями True, с колличеством элементов равным количеству
    # элементов нашей последовательности. Делаем мы это потому что: 1) мы изначально предполагаем, что все элементы
    # последовательности- простые. 2) не будем забывать, что в данном случае индексы элементов массива так же являются
    # элементами нашей последовательности.
    a = [True] * n
    for i in range(2, n):  # так как мы помним, что простым число является число, которое имеет только 2 делителя-
        # 1 и самого себя, мы явно исключаем 0 и 1.
        if a[i]:  # теперь самое интересное. Проверяем элементы созданного массива, но мы то явно указали, что все
            # элементы == True
            for k in range(2 * i, n, i):  # мы записали такое выражение в range что бы как бы 'отловить' те числа в
                # последовательности, которые получаются в результате 2 * i;
                a[k] = False  # вот мы их и помечаем как False, так как эти числа являются составными.
    # напишем еще один цикл, что бы напечатать все элементы последовательности n, печатаем с проверкой
    # тернарным оператором.
    for i in range(2, n):
        print(i, '-', 'простое' if a[i] else 'составное')


# the_sieve_of_eratosthenes(20)

# далее будем называть вещи своими именами, а не массивами :)

"""Квадратичные сортировки (O(n**2))"""


def insert_sort(a: list):
    """Сортировка списка a вставками"""
    # Идея данного алгоритма в том, что предыдущий элемент списка мы как бы считаем отсортированным, покуда рядом с ним
    # не обнаруживаем элемент меньше. Далее мы проходим с этим элементом по всему отсортированному сегменту и проверяем,
    # куда б его вставить. Мы как бы вставляем элементы, от сюда и название.
    for top in range(1, len(a)):  # запускаем цикл и пробегаемся по списку от 2го элемента до последнего. Начинаем
        # именно со 2го элемента потому, что в дальнейшем мы будем сравнивать и менять местами текущий элемент, то есть
        # с индексом k и элемент с индексом k-1. Если мы пробежимся просто по range(len(a)), то в какой-то момент мы
        # выйдем за пределы последовательности, что приведет либо к ошибке, либо начисто сломает логику алгоритма.
        # временную переменную называем top, так как каждый элемент считаем самым большим.
        k = top  # создадим копию временной переменной, которая является индексом списка, для наглядности
        while k > 0 and a[k - 1] > a[k]:  # в цикле задаем нужное условие
            a[k], a[k - 1] = a[k - 1], a[k]  # просто меняем местами элементы, используя множественное присваивание
            k -= 1  # уменьшаем k дабы не зациклиться
    return a


# lst = [3, 5, 2, 1, 4]
# print(insert_sort(lst))


def choice_sort(a: list):
    """Сортировка списка a выбором"""
    # Идея данного алгоритма в том, что мы сначала берем самый первый элемент и сравниваем его с другими и как только
    # находим самый первый элемент, который меньше исходного, меняем их местами, и так далее, пока не найдем реально
    # самвй меньший. После чего мы как бы закрываем эту позицию для изменений и переходим к следующей по порядку.
    # От сюда и название. Мы как бы вставляем элементы.
    # Логика первого for вт том, что мы как бы пробегаем по всем элементам не включая последний потому, что мы будем
    # делать вставки ка бы вправо (pos + 1 во вложенном for), иначе мы просто выйдем за предел последовательности.
    for pos in range(len(a) - 1):
        for i in range(pos + 1, len(a)):
            if a[i] < a[pos]:  # вот само сравнение элементов, и если оно True, меняем их местами
                a[i], a[pos] = a[pos], a[i]
    return a


# lst = [3, 5, 2, 1, 4]
# print(choice_sort(lst))

def bubble_sort(a: list):
    """Сортировка списка a методом пузырька"""
    # Сортировка пузырьком очень похожа на сортировку выбором, но есть небольшой нюанс, в пузырьковой сортировке
    # сам сортировщик является близоруким. То есть он не ориентируется по позиции, он берет элемент и тянет его на верх,
    # то есть вправо. Как бы ориентируется по количеству проходов.
    # Такое название потому, что элемент всплывает как пузырек.
    for bypass in range(1, len(a)):
        for i in range(len(a) - bypass):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

    return a


# lst = [3, 5, 2, 1, 4]
# print(bubble_sort(lst))


"""Сортировки O(n)"""


def count_sort(a: list):
    """ Сортировка подсчетом """
    # Сортирвка подсчетом- очень быстрый алгоритм если речь идет об очень большом количестве данных, при этом
    # диапазон значений каждого элемента не очень велик. Алгоритм не требует запоминания всех чисел в потоке данных.
    # Является однопроходным.

    # Заведем список счетчиков, по размеру он будет равен диапазону возможных  значений элементов исходного списка,
    # но заполнен будет нулями. Для этого алгоритма очень важно если мы будем знать в диапзаон значений, иначе он
    # не сработает.
    counters = [0 for _ in range(min(a), max(a) + 1)]
    max_value = max(a) + 1  # в эту переменную положим максимальное значение элемента исходного списка, понадобится
    # нам далее.
    for i in a:  # проходим по списку и записываем counters[i] количесво чисел, которые равны i.
        # Эта чать называется частотный анализ.
        counters[i] += 1
    del a[:]  # внезапно очищаем наш список)))
    for n in range(max_value):  # а вот тут как раз и понадобилась наша переменная заполнения списка а по новой
        a += [n] * counters[n]
    return a


# Что бы не заплнять руками воспользуемся модулем random и сгенерируем список спомощью него
# from random import randint
#
# lst = [randint(0, 20) for _ in range(100)]
# print(count_sort(lst))


"""Рекурсия"""

# По сути рекурсия- это вызов функции самой себя внутри себя.
# Для создания рекурсии на необходимо 2 фактора: 1) Рекурентный случай. 2) Крайний случай.
# Мы как бы разбиваем задачу на более мелкие подзадачи и решаем их этой же функцией. Пример из фольклора-
# сказка "Репка", где дед не мог вытянуть репку и звал на помощь бабку, внучку, жучку, кошку и мышку. Бабка, внучка,
# Жучка, кошка -  решали рекурентные случаи, а вот мышка- это крайний случай. Но в компьютерной интерпретации всесь стек
# вызовов формируется одной функцией. Другой пример- матрешка. Уровни вложенности матрешки- рекурентный случай, а одна
# единственная матрешка, которая не содержит в себе других матрешек, является крайним случаем. Не трудно догадаться,
# что мы перед изготовлением матрешки мы должны знать ее уровень вложенности и каков будет крайний случай.
# Это два важнейших вопроса, которые мы должны решить перед написанием рекурсии, в противном случае писать рекурсию
# нельзя. Ну и как можно было еще раз догадаться, рекурсия бывает нужна далеко не всегда и, собственно,
# далеко не все задачачи можно решить рекурсией.


def matryoshka(n):
    if n == 1:  # определяем крайний случай
        print('Последняя матрешка')
    else:  # иначе будем вызавать функцию вновь и вновь
        print(f'верх матрешки n= {n}')
        matryoshka(n - 1)
        print(f'низ матрешки n= {n}')


# matryoshka(7)

# или другой пример графического характера из векторной шеометрии, импортируем кое-что для этого

# from graphics import GraphWin, Point, Line
#
# window = GraphWin('Russian game', 700, 700)
# ALPHA = 0.2
#
#
# def fractal_rectangle(a, b, c, d, deep=10):  # deep- это аргумент по умолчанию указывающий на глубину рекурсии
#     if deep < 1:
#         return
#     for m, n in (a, b), (b, c), (c, d), (d, a):
#         Line(Point(*m), Point(*n).draw(window))
#     a1 = (a[0] * (1 - ALPHA) + b[0] * ALPHA, a[1] * (1 - ALPHA) + b[1] * ALPHA)
#     b1 = (b[0] * (1 - ALPHA) + c[0] * ALPHA, b[1] * (1 - ALPHA) + c[1] * ALPHA)
#     c1 = (c[0] * (1 - ALPHA) + d[0] * ALPHA, c[1] * (1 - ALPHA) + d[1] * ALPHA)
#     d1 = (d[0] * (1 - ALPHA) + a[0] * ALPHA, d[1] * (1 - ALPHA) + a[1] * ALPHA)
    # fractal_rectangle(a1, b1, c1, d1, deep-1)  # вот тот самый рекурсивный вызов нашей функции внутри себя же


# fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))

# есть и более понятные классические примеры рекурсии
# например нахождение факториала
# за основу возьмем формулу n! = (n - 1)! * n
# но у нас возникает один момент, если мы будем находить факториал рекурсивно, то если в параметр функции попадет
# отрицательное число- мы натыкаемся на бесконечную рекурсию. В принципе факториал для отрицательных чисел то же
# возможен, но расчитывается он несколько иначе. В нашем же примере мы с помощью assert исключим возможность передачи
# отрицательных числел как параметры функции.

def factorial(n):
    assert n >= 0, 'Факториал отрицательного числа неопределен'
    if n == 0:
        return 1
    return factorial(n - 1) * n

# или еще пример, алгоритм Евклида. То есть нахождение наибольшего общего делителя для некоторых чисел.
# например у нас есть 2 целых числа и нам нужно найти для них наибольший общий делитель. Нюанс в том, что числа у нас 2,
# а при a < b и b < a алгоритм отличается, значит на понадобится еще доп условие, ну а при a == b наибольшим общем
# делителем будет являться само число, это и есть крайний случай.


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

# но можно и не выделять 2 подслучая а сделать все более элегантно. Прикол в том что, если a > b и попробовать поделить
# со взятием остатка a % b, и внезапно остаток будет 0, это будет означать, что b и есть максимальный общий делитель,
# да и к тому же остаток от деления всегда будет меньше делителя. Но что если a < b, да ничего, просто добавляется еще
# один рекурентный вызов, остаток просто переедет на место а.


def gcd_modified(a, b):
    if b == 0:  # если мы зашли внутрь функции и оказалось, что b == 0, то наибольший общий делитель равен a
        return a
    else:  # а если нет, продолжаем проверять дальше
        return gcd_modified(b, a % b)


# ну или еще более просто с использованием тернарного опрератора
def gcd_modified_new(a, b):
    return a if b == 0 else gcd_modified_new(b, a % b)


# быстрое возведение в степень. В данном примере будем ориентироваться на формулу a**n = a**(n - 1) * n
# но этот вариант будет работать довольно медленно O(n).
def pow(a, n):
    return 1 if n == 0 else pow(a, n - 1) * a


# в варианте, который работает быстрее мы просто раздлим наши вычисления на 2 подслучая для четных и нечетных степеней.
# данный вариант работает по времени О(log_n)
def pow_modified(a, n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return pow(a, n - 1) * a
    else:
        return pow(a ** 2, n // 2)


# Ханойские башни. Классическая задача и из математеки и из программирования. Про условия можно подробнее почитать
# в интернете.

def transfer(start, finish, n):  # функция принимает 3 аргумента, начальный стержень и конечный, а так же количество
    # дисков
    if n == 1:
        print(f'Диск 1 переносится со стержня {start} на стержень {finish}')
    else:
        tmp = (6 - start) - finish  # tmp- это как бы 3й штырь, являющийся буфером обмена
        transfer(n - 1, start, tmp)
        print(f'Диск {n} переносится со стержня {start} на стержень {finish}')
        result = (n - 1, tmp, finish)
        print(result)


# Генерация всех перестановок

# Напишем функцию, которая генерирует все числа (с лидирующими незначащими нулями) в N-ричной системе счисления при
# n <= 10 длины m
def generate_numbers(n: int, m: int, prefix=None):  # где n- это основание числа, m- это длина числа, то есть
    # количество цифр, a prefix- это с чего начинать генерацию, по умолчанию с ничего.
    # Но нужно будет явно указать в когда именно нам считать prefix за None, а когда пустым списком
    prefix = prefix or []
    if m == 0:  # крайним случаем будет ситуация, когда цифр нам больше не надо, то есть когда m = 0
        print(*prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m - 1, prefix)  # да да, рекурентный случай внутри цикла ))
        prefix.pop()


# generate_numbers(2, 4)


# а вот теперь напише функцию, генерирующую все перестановки n чисел в m позициях, с префиксом prefix
# но для начала напишем функцию поиска числа в списке (однопроходный алгоритм) она нам понадобится в нашей основной
# функции. Вообще это не обязательно, так как у списков есть метод поиска элемента, но для наглядности она будет нам
# полезна.
def find(number, a):
    for x in a:
        if number == x:
            return True
    return False


# вообще все очень похоже на то, что мы делали в генерации чисел
def generate_permutations(n: int, m: int = -1, prefix=None):
    m = n if m == -1 else m  # по умолчанию n чисел в n позициях
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep='')
        return
    for number in range(1, n + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()


generate_permutations(6)




