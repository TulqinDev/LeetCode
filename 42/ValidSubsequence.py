"""
Ikkita butun sonlardan iborat array beriladi. Ikkinchi array birinchining ketma-ket qismi ekanini aniqlovchi funksiya yozing.

Ketma-ket qism — bu elementlari tartib bilan uchraydigan, lekin yonma-yon bo‘lishi shart bo‘lmagan qator.

Masalan, [1, 3, 4] sonlari [1, 2, 3, 4] arrayining ketma-ket qismi hisoblanadi, [2, 4] ham shunday. Shuningdek, bitta son yoki arrayning o‘zi ham ketma-ket qism bo‘lishi mumkin.

Misol uchun
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

"""


def isValidSubsequence(array, sequence):
    seq_index = 0

    for value in array:
        if seq_index == len(sequence):
            break

        if value == sequence[seq_index]:
            seq_index += 1

    return seq_index == len(sequence)
