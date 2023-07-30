word = str(input('Ведите слово:'))
user = word[::-1]
if word == user:
    print('True')
else:
    print('False')