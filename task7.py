#Как мы говорили ранее, в программировании часто приходится писать код исходя из результата, который требует заказчик.
#В этот раз заказчику нужно получить вот такой двумерный список:
# #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#Напишите программу, которая генерирует такой список и выводит его на экран. Используйте только list comprehensions.

cols = 3
rows = 4
list1 = [list(range(x, x + rows * (cols - 1) + 1, rows)) for x in range(1, rows + 1) ]
print(list1)