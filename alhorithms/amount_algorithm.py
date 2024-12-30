'''
рекурсивный алгоритм нахождения числа разбиения числа X на слагаемые не превосходящие K,
следовательно для нахождения числа разбиений для N нам нужно nf(N,N)
Ассимптотика алгоритма: O(N^2)
Источник: https://neerc.ifmo.ru/wiki/index.php?title=Нахождение_количества_разбиений_числа_на_слагаемые&mobileaction=toggle_view_mobile
'''

def nf(x,k):
    if x == 0:
        return 1
    res = 0
    for i in range(min(x,k),0,-1):
        res += nf(x-i,i)
    return res
