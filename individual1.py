#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    user_input = input("Введите элементы кортежа, разделенные пробелом: ")
    my_tuple = tuple(map(int, user_input.split()))

    index = 0
    while index < len(my_tuple) - 1 and my_tuple[index] == my_tuple[index + 1]:
        index += 1

    if index == len(my_tuple) - 1:
        print(f"Весь массив заполнен одинаковыми элементами ({len(my_tuple)} элементов)")
    else:
        print(f"Количество равных элементов в начале: {index + 1}")
        print(f"Элементы, следующие за последним равным элементом: {my_tuple[index + 1:]}")
