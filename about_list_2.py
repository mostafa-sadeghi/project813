# slicing    برش زدن
# numbers = [1, 2, 3, 4, 5]

# print(numbers[0:2])
# print(numbers[:2])
# print()
# print(numbers[2:5])
# print(numbers[2:])

# numbers = []

# n = int(input('enter first number: '))
# numbers.append(n)

# n = int(input('enter second number: '))
# numbers.append(n)

# n = int(input('enter third number: '))
# numbers.append(n)

# n = int(input('enter forth number: '))
# numbers.append(n)

# print()
# print("my list:", numbers)

# print(numbers[0] + numbers[1] + numbers[2] + numbers[3])
# print("sum is:", sum(numbers))

# ex 1
# برنامه ای بنویسید که نام چهار دانش آموز را از ورودی دریافت نمایدو
# در یک لیست ذخیره نماید
# از لیست ایجاد شده یک برش ایجاد کنید که شامل دو نام اول باشد.
# students = []

# n1 = input('enter first name: ')
# n2 = input('enter second name: ')
# n3 = input('enter third name: ')
# n4 = input('enter forth name: ')

# students.append(n1)
# students.append(n2)
# students.append(n3)
# students.append(n4)
# print(students)
# print()
# print('************************************')
# print(students[0:2])

# ex 2 : numbers = ['a', 'b', 'c', 'd', 'e']
# numbers = ['a', 'b', 'c', 'd', 'e']
# از لیست بالا برش های زیر ر اایجاد کنید
# ['d', 'e']
# print(numbers[3:])
# ['b', 'c']
# print(numbers[1:3])
# ['b', 'c','d]
# print(numbers[1:4])

# ex 3 : string='abcdefghi'
# از رشته بالا برش های زیر را ایجاد نمائید:
string = 'abcdefghi'
# abc
print(string[:3])
# cd
print(string[2:4])
# def
print(string[3:6])
# hi
print(string[7:])
# fgh
print(string[5:8])
