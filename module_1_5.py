immutable_var=tuple[(1,2,3,'Break',True)]
print(immutable_var)
immutable_var[0]=24         #Изменить значение элемента в кортеже нельзя, так как кортеж не поддерживает обращение по элементам. Но можно поменять элемент через обращение по индексу.
print(immutable_var)

mutable_list=[1,2,3,4, True, 'Mood']
print(mutable_list)
mutable_list[0]=5
print(mutable_list)


