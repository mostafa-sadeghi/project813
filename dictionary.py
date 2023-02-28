# favorite_sports = ["football", "basketball", "baseball","tennis"]

# favorite_sports = {}
# print(type(favorite_sports))

# favorite_sports = {
#     'taha': 'football',
#     'alireza': 'basketball',
#     'negar': 'pingpong',
#     'sadra': 'tennis'
# }

# print("taha likes", favorite_sports['taha'])
# print("negar likes", favorite_sports['negar'])
# favorite_sports['ramtin'] = 'football'
# print("new favorite sports dictionary:", favorite_sports)

# del favorite_sports['ramtin']
# print("our favorite sports dictionary after delete:", favorite_sports)

# برنامه ای بنویسید که نام و معدل 4 دانش آموز را از ورودی دریافت نماید
# و در یک دیکشنری ذخیره نماید
# یک نام و معدل جدید از ورودی بگیرد و به دیکشنری اضافه نماید
# یک نام از ورودی بگیرد و از دیکشنری حذف

students = {}
name1 = input('enter student name: ')
ave = float(input('enter student average: '))
students[name1] = ave
name1 = input('enter student name: ')
ave = float(input('enter student average: '))
students[name1] = ave
name1 = input('enter student name: ')
ave = float(input('enter student average: '))
students[name1] = ave
name1 = input('enter student name: ')
ave = float(input('enter student average: '))
students[name1] = ave

print(students)
name1 = input('enter student name: ')
ave = float(input('enter student average: '))
students[name1] = ave

print('enter a name to remove from dictionary:')
name = input('> ')
del students[name]

print(f"our dictionary after deleting {name}")
print(students)
