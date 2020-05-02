person_name_1 = "   Albert Einstein   "
person_name_2 = '     Albus Donbledore   '
print(person_name_1.lstrip())
print(person_name_1.rstrip())
print(person_name_1.strip())
person_name_1 = person_name_1.strip()
print(person_name_2.lstrip())
print(person_name_2.rstrip())
print(person_name_2.strip())
person_name_2 = person_name_2.strip()
print('\t' + person_name_1 + '\n\t' + person_name_2)
