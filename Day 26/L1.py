#list or sequence comprahenstion
#syntax - new_list = [new_item for item in list]
#syntax - new_list = [new_item for item in list if test]


#finding square numbbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n*n for n in numbers]
print(squared_numbers)

#even numbers from above list
even_number = [n for n in numbers if n%2 == 0]
print(even_number)

