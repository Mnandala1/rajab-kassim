'''
#EXCERCISE 1
message = 'hi my name is Rajab learning python'
print(message)

print('\n')
mylist = message.split()
print(mylist)
mylist.sort()
print(mylist)
print('\n')

message = 'I hope I can master it'
print(message.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = 'Rajab'
second_name = 'Kassim'
full_name = first_name + " " + second_name  #CONCATENATE
print(full_name)

#EXCERCISE 2
name = 'john pombe magufuli'
print("Hello"" " + name +" " "would you like to learn some Python today?")

print(name.title())
print(name.lower())
print(name.upper())
print('\n')

name = 'Albert Eistein'
message = 'once said, “A person who never made amistake never tried anything new.”'
print(name+" "+message)

age = '23'
message ='happy ' +age+ 'rd Birthday'
print(message)

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

print(5+3)
print(11-3)
print(4*2)
print(8/1)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())
print('\n')
print(bicycles[-1].title()) #return the last value
print(bicycles[-2].title()) #return the second from last value
print(bicycles[-3].title()) #return the 3rd fromlast value
print(bicycles[-4].title()) #return the first value

message = 'my first bcycle was a bicycles[0]'
print(message)

#EXCERCISE 3

friends = ['juma','ally','seif','noya','jose','fau','aneth','bahati']
print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())
print(friends[4].title())
print(friends[5].title())
print(friends[6].title())
print(friends[7].title())
print('\n')
message = 'Hello how are you '
print(message + friends[0].title(), '\n')
print(message + friends[1].title(), '\n')
print(message + friends[2].title(), '\n')
print(message + friends[3].title(), '\n')
print(message + friends[4].title(), '\n')
print(message + friends[5].title(), '\n')
print(message + friends[6].title(), '\n')
print(message + friends[7].title(), '\n')

friends[0] = 'waziri' #modify the list
friends[1] = 'mrisho'
print(friends)

friends.append('nasri') #adds new item
friends.insert(7,'Rajab')
print(friends)
del friends[2] #delete item
print(friends)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('honda')
print(motorcycles)

#EXCERCISE 3-4

guest_list = ['juma','ally','seif','noya','jose','fau','aneth','Rajab','bahati']
message = ' you are welcome for dinner on 23rd'
print( guest_list[0] + message, '\n')
print( guest_list[1] + message, '\n')
print( guest_list[2] + message, '\n')
print( guest_list[3] + message, '\n')
print( guest_list[4] + message, '\n')
print( guest_list[5] + message, '\n')
print( guest_list[6] + message, '\n')
print( guest_list[7] + message, '\n')
print( guest_list[8] + message, '\n')

message_1 = 'the following guest wont attend '
print(message_1 + guest_list[0]+ ", " +guest_list[4]+ ", " +guest_list[6] )
print('\n')
guest_list = ['asha','ally','seif','noya','zai','fau','mariam','Rajab','bahati']

message_2 = 'new guests are '
print( guest_list[0] + message, '\n')
print( guest_list[1] + message, '\n')
print( guest_list[2] + message, '\n')
print( guest_list[3] + message, '\n')
print( guest_list[4] + message, '\n')
print( guest_list[5] + message, '\n')
print( guest_list[6] + message, '\n')
print( guest_list[7] + message, '\n')
print( guest_list[8] + message, '\n')

print("we have found bigger table and decided to add new guests")
guest_list.insert(0,'shabani')
guest_list.insert(5,'ramadhani')
guest_list.append('pinde')
print(guest_list)
message = ' you are welcome for dinner on 23rd'
print( guest_list[0] + message, '\n')
print( guest_list[1] + message, '\n')
print( guest_list[2] + message, '\n')
print( guest_list[3] + message, '\n')
print( guest_list[4] + message, '\n')
print( guest_list[5] + message, '\n')
print( guest_list[6] + message, '\n')
print( guest_list[7] + message, '\n')
print( guest_list[8] + message, '\n')
print( guest_list[9] + message, '\n')
print( guest_list[10] + message, '\n')
print( guest_list[11] + message, '\n')

guest_list = ['juma','ally','seif','noya','jose','fau','aneth','Rajab','bahati']
guest_list.sort()
print(guest_list)
print(len(guest_list))'''
