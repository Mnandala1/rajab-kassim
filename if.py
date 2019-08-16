'''guest_list = ['juma','ally','seif','noya','jose','fau','aneth','Rajab','bahati']
for guest in guest_list:
    if guest == 'jose':
        print(guest.upper())
    else:
        print(guest.title())
print('\n')

name = ['alli', 'john','hafsa']
if name != 'john':
    print ("you are not welcome")
print('\n')

names = ['alli', 'john','hafsa']
for name in names:
    if name != 'john':
        print(name +" you are not welcome")
        print('\n')
banned_users = ['juma','ally','seif','noya','jose','fau','aneth','Rajab','bahati']
user = 'chausiku'
if user not in banned_users:
    print(user + ", you can post your feedback")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age = 23
if age` > 3:
    print("you are infant")
elif 4 < age < 5:
    print("you are todler")
elif 6<= age < 10:
    print("you are kid")
elif 11<= age < 19:
    print("you are teen")
else:
    print("you are adult")'''

message = input("Tell me something, and I will repeat it back to you: ")
print(message)
