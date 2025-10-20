"""

Tartiblangan kvadratlar
Bo‘sh bo‘lmagan va o‘sish tartibida saralangan butun sonlar arrayini qabul qiluvchi funksiya yozing. Funksiya har bir sonning kvadratini hisoblablasin. Natija ham o‘sish tartibida qaytarilsin.

Misol uchun
array = [1, 2, 3, 5, 6, 8, 9]
Kutilgan natija
[1, 4, 9, 25, 36, 64, 81]
"""


def sortedSquaredArray(array):
     new = []

     for value in array:
         n = value ** 2
         new.append(n)
         new.sort()

     return new
