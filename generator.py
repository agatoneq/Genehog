import random

def display_list(list1, amount):
    numbers = set()
    while len(numbers) < int(amount):
        numbers.add(random.randint(1, len(list1)) - 1)

    for i in range(int(amount)):
        print(list1[list(numbers)[i]])


def make_list(file_name, amount):
    list1 = []
    with open(file_name, 'rt') as file:
        for line in file:
            list1.append(line.strip())
    display_list(list1, amount)


def get_from_user():
    choice_m = input('Ile chcesz wygenerować imion męskich? ')
    choice_d = input('Ile chcesz wygenerować imion damskich? ')
    file1 = 'imiona_damskie.txt'
    file2 = 'imiona_meskie.txt'
    print('Imiona meskie:')
    make_list(file2, choice_m)
    print('Imiona damskie:')
    make_list(file1, choice_d)