
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cube = [number * number * number for number in numbers if number % 2 != 0]
print(f"Oto sześciany licz niepodzielnych przez 2: {cube}")


list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
'''zeros = [number for number in list if number == 0]
rest = [number for number in list if number != 0]
print(f"Oto wszystkie zera w zbiorze: {zeros}")
print(f"Oto liczby różne od zera w zbiorze: {rest}") 
# żle zrozumiałem zadanie i zamiast slicingu próbowałem to posegregować poprzednią metodą
'''
zeros = (list[1:4], list[5:10], list[-2:])
rest = list[:1], list[4:5], list[10:12]
print(f"Oto wszystkie zera w zbiorze: {zeros}")
print(f"Oto liczby różne od zera w zbiorze: {rest}")


print("Kolega")