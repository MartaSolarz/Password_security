# UPDATE: 5/08/2022

from string import punctuation
import sys

import click

def check_password_lenght(password:str)->tuple:
    comment = ''
    if len(password) < 8:
        flag = False
        comment = '- Twoje hasło musi składać się z przynajmniej 8 znaków.'
    else:
        flag = True

    return flag, comment


def check_whitespace(password:str)->tuple:
    comment = ''
    flag = True
    for char in password:
        if char.isspace():
            flag = False
            comment = '- Twoje hasło NIE może zawierać spacji.'
            break
    
    return flag, comment


def check_upper_char(password:str)->tuple:
    flag = False
    for char in password:
        if char.isupper():
            flag = True
            break

    comment = ''
    if flag == False:
        comment = '- Twoje hasło musi zawierać conajmniej jedną dużą literę.'

    return flag, comment


def check_lower_char(password:str)->tuple:
    flag = False
    for char in password:
        if char.islower():
            flag = True
            break

    comment = ''
    if flag == False:
        comment = '- Twoje hasło musi zawierać conajmniej jedną małą literę.'

    return flag, comment


def check_special_char(password:str)->tuple:
    flag = False
    for char in password:
        if char in punctuation:
            flag = True
            break
    
    comment = ''
    if flag == False:
        comment = '- Twoje hasło musi zawierać conajmniej jeden znak specjalny.'

    return flag, comment


def check_digit(password:str)->tuple:
    flag = False
    for char in password:
        if char.isdigit():
            flag = True
            break
    
    comment = ''
    if flag == False:
        comment = '- Twoje hasło musi zawierać conajmniej jedną cyfrę.'

    return flag, comment


def ask_for_raport()->None:

    while True:
        ask_for_raport = input('Czy wyświetlić rekomendacje? [t/n] ')
        if ask_for_raport.lower() == 't':
            break
        elif ask_for_raport.lower() == 'n':
            sys.exit(1)
        else:
            print('Niedozowolona wartość. Podaj [t/n].')


def prepare_raport(checking:tuple[bool, str])->None:

    if checking[0] == False:
        print(checking[1])


@click.command()
@click.argument('password')

def main(password):

    operations_to_check = [
        check_password_lenght(password), 
        check_upper_char(password),
        check_lower_char(password),
        check_digit(password),
        check_special_char(password),
        check_whitespace(password)
        ]
    
    flag = True
    comment = 'Twoje hasło jest bezpieczne.'
    for operation in operations_to_check:
        if operation[0] == False:
            flag = False
            comment = 'Twoje hasło nie jest wystarczająco bezpieczne.'
            break
    
    print(comment)

    if flag == False:
        ask_for_raport()

        for operation in operations_to_check:
            prepare_raport(operation)


if __name__ == '__main__':
    main()
