'''for x in range(0, 100, 10):#print values from 0 to 100 in range of 10, 100 is excluded
    print(x)

print('\n')

range = [0, 100, 10]
for x in range:
    print(x)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


guest_list = ['juma','ally','seif','noya','jose','fau','aneth','Rajab','bahati']
for guest in guest_list: #This line tells Python to pull a name from the list guest_list , and store it in the variable guest
    print(guest) #we tell Python to print the name that was just stored in magicia
print('\n')

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

#most of codes in trial file can be simplified by for loop
guest_list = ['juma','ally','seif','noya','jose','fau','aneth','Rajab','bahati']
for guest in guest_list:
    print (guest)
    print("you are welcome for dinner" '\n')
print("THANK YOU")

#EXCERCISE 4.1
foods = ['ugali', 'wali','pilau', 'uji',]
for food in foods:
    print(food.title())
print("I like pilau compared to all other kind of foods")
print("I REALY LOVE PILAU")

#range() to make list
numbers = list(range(1,6))
print(numbers)

squares = []
for value in range(1,11):

    square = value**2

    squares.append(square)
print(squares)

squares = []
for value in range(1,11):

    square = value**2

    squares.append(square)
    print(squares)

for value in range(1,21):
    print(value)

for number in range(1,21):
    print(number)

numbers = list(range(1,1000000))
for number in numbers:
    print(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

for number in range(1,21,2):#odd
    print(number)

print('\n')
for mult in range(3,30,3):#multiples of 3
    print(mult)'''

'''for number in range((1,10)**2):#wrong
    print(number)

cubes = []
for number in range(1, 11):
    cube = number**2
    cubes.append(cube)

for cube in cubes:
    print(cube)'''

list = ['juma','ally','seif','noya','jose','fau','aneth','Rajab','bahati']
first_three = list[0:3]
message = 'The first three items in the list are '
print(message + str(first_three))
print('\n')
