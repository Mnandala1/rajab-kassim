
#!/usr/bin/Python3
import sys

def numbers(string):
    string = '2.2, 1.3, 8.8, 5.5, 3.4, 12.5, 9.9, 2.7, 7.1, 1.1'
    num_list = string.split()
    print(num_list)
    num_list_float = []
    for numbers in num_list:
        num_list_float.append(float(string))

    '''num_list.sort()
    print(num_list)'''

if __name__ == '__main__':
    numbers(sys.argv[1])
