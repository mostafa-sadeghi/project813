# age = 13

# if age >= 19:
#     print("you are adult...")
#     print('...............')
# elif age >= 13 and age < 19:
#     print("You are teenager...")

# elif age <= 8:
#     print('you are kid...')
# elif age > 8 and age < 13:
#     print("you are junior...")

# برنامه ای بنویسید که سه عدد از ورودی دریافت نماید و
# اگر هر یک از اعداد زوج بودند، آن عدد را در داخل لیست اضافه کند
# لیست را پرینت نمائید.
# NOTE 4 % 2

# even_numbers = []

# n1 = int(input('enter a number:> '))
# n2 = int(input('enter a number:> '))
# n3 = int(input('enter a number:> '))

# if n1 % 2 == 0:
#     even_numbers.append(n1)
# if n2 % 2 == 0:
#     even_numbers.append(n2)
# if n3 % 2 == 0:
#     even_numbers.append(n3)
# print("even numbers are: ", even_numbers)

# exercise 1 :
# برنامه ای بنویسید که چهار عدد را از ورودی دریافت نماید
# و اعداد زوج را در یک لیست و اعداد فرد را در لیست دیگری ذخیره نماید
# مجموع اعداد زوج و نیز مجموع اعداد فرد را از لیست ها محاسبه نمائید و پرینت کنید.


even_numbers = []
odd_numbers = []
n1 = int(input('enter a number:> '))
n2 = int(input('enter a number:> '))
n3 = int(input('enter a number:> '))
if n1 % 2 == 0:
    even_numbers.append(n1)
else:
    odd_numbers.append(n1)
if n2 % 2 == 0:
    even_numbers.append(n2)
else:
    odd_numbers.append(n2)
if n3 % 2 == 0:
    even_numbers.append(n3)
else:
    odd_numbers.append(n3)
print("sum of even numbers are: ", sum(even_numbers))
print("sum of odd numbers are: ", sum(odd_numbers))
