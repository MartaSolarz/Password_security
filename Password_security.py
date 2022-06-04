# Project - 6.04.2022
# Is your password secure enough?

password = input('Podaj hasło: ')

alpha_lower = []
alpha_upper = []
digit = []
space = []
other_char = []

for char in password:
    if char.isalpha():
        if char.islower():
            alpha_lower.append(char)
        else:
            alpha_upper.append(char)
    elif char.isdigit():
        digit.append(char)
    elif char.isspace():
        space.append(char)
    else:
        other_char.append(char)

too_short = len(password) < 8
no_alpha_lower = alpha_lower == []
no_alpha_upper = alpha_upper == []
no_digit = digit == []
contains_space = space != []
no_special_char = other_char == []

no_secure_enough = too_short or no_alpha_lower or no_alpha_upper or no_digit or contains_space or no_special_char

report = ''

if no_secure_enough:
    report += 'Twoje hasło nie jest wystarczająco bezpieczne.' '\n' 'Rekomendacje: ' '\n'
    if too_short:
        report += '- Twoje hasło powinno składać się z przynajmniej 8 znaków.' '\n'
    if no_alpha_lower:
        report += '- Twoje hasło powinno zawierać przynajmniej jedną małą literę.' '\n'
    if no_alpha_upper:
        report += '- Twoje hasło powinno zawierać przynajmniej jedną wielką literę.' '\n'
    if no_digit:
        report += '- Twoje hasło powinno zawierać przynajmniej jedną cyfrę.' '\n'
    if contains_space:
        report += '- Twoje hasło NIE może zawierać spacji.' '\n'
    if no_special_char:
        report += '- Twoje hasło powinno zawierać przynajmniej jeden znak specjalny.'
else:
    report += 'Twoje hasło jest bezpieczne.'

print() 
print(report)
