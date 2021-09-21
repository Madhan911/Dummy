list = [1,"nani","madhan",3,32,2,]
str = "hello"


print(list[2])
print(list[-2])
print(list[-4:])#last four

print(set(list))


print(tuple(list))

# a = list[0]
list[0]=float(list[0])
print(list)



print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='\n')


print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))

x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %1.4f' %x)

#
# a = input("enter the number  :")
# print(type(a))


# a = int(input("enter the number  :"))
#
# print('number is {0} and {1}'.format(type(a),a))
# print('number is {0} and {1}'.format(type(a),a))


# Note: You may get different values for the id

a = 2
print('id(2) =', id(2))

print('id(a) =', id(a))


# Note: You may get different values for the id

a = 2
print('id(a) =', id(a))

a = a+1
print('id(a) =', id(a))

print('id(3) =', id(3))

b = 2
print('id(b) =', id(b))
print('id(2) =', id(2))




a = 5
a = 'Hello World!'
a = [1,2,3]
print(a)


a = "nanimadhanmohan"
print(id(a))







