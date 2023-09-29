from random import randint


def get_array(n: int) -> list:
    """Функция генерирует n массивов случайных неповторяющихся размеров, заполненных случайными числами.
    Массивы с чётным порядковым номером сортируются по неубыванию. С нечётным - по убыванию.
    Возвращает массив с отсортированными массивами"""
    array = []
    
    while len(array) < n:
        len_subarrays = [len(i) for i in array] # длины всех подмассивов
        subarray_size = randint(1, n ** 2) # размер нового подмассива
        if subarray_size not in len_subarrays:
            subarray = [randint(-n ** 2, n ** 2) for i in range(subarray_size)]
            array.append(subarray)
    
    sorted_array = []
    
    for index, value in enumerate(array): # сортировка с учётом порядкового номера, начиная с 0
        if not index % 2:
            sorted_array.append(sorted(value))
        else:
            sorted_array.append(sorted(value, reverse=True))
    
    return sorted_array

