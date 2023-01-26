# Задача 2.
# Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
# Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, которая
# отстоит в алфавите на некоторое фиксированное число позиций.
# В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша
# функция кодирует сдвиг алфавита на 3 позиции.
#
# Все символы, кроме русских букв должны остаться неизменными. Маленькие буквы должны
# превращаться в маленькие, большие — в большие.
# Напишите также функцию декодирования decrypt_caesar(msg, shift), также
# использующую сдвиг по умолчанию. При написании функции декодирования используйте
# вашу функцию кодирования.


def encrypt_caesar(msg, shift):
    if shift == '':
        shift = 3
    else:
        shift = int(shift)
    encripted = ''
    for el in msg:
        if ord(el) > 1039 and ord(el) < 1072:
            el_encr = chr(ord(el) + shift)
            if ord(el) + shift > 1071:
                el_encr = chr(ord(el) + shift - 32)
            elif ord(el) + shift < 1040:
                el_encr = chr(ord(el) + shift + 32)
        elif ord(el) > 1071 and ord(el) < 1104:
            el_encr = chr(ord(el) + shift)
            if ord(el) + shift > 1103:
                el_encr = chr(ord(el) + shift - 32)
            elif ord(el) + shift < 1072:
                el_encr = chr(ord(el) + shift + 32)
        else:
            el_encr = el
        encripted += el_encr
    return encripted


print(encrypt_caesar(input('Введите сообщение: '), input('Задайте N - величину сдвига\n\
(для декодирования введите тоже значение, что и для кодирования, но с обратным знаком): ')))
