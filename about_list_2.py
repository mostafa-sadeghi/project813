# slicing    برش زدن
# numbers = [1, 2, 3, 4, 5]

# print(numbers[0:2])
# print(numbers[:2])
# print()
# print(numbers[2:5])
# print(numbers[2:])

numbers = []

n = int(input('enter first number: '))
numbers.append(n)

n = int(input('enter second number: '))
numbers.append(n)

n = int(input('enter third number: '))
numbers.append(n)

n = int(input('enter forth number: '))
numbers.append(n)

print()
# print("my list:", numbers)

print(numbers[0] + numbers[1] + numbers[2] + numbers[3])
print("sum is:", sum(numbers))

# ex 1
# برنامه ای بنویسید که نام چهار دانش آموز را از ورودی دریافت نمایدو
# در یک لیست ذخیره نماید
# از لیست ایجاد شده یک برش ایجاد کنید که شامل دو نام اول باشد.


# ex 2 : numbers = ['a', 'b', 'c', 'd', 'e']

# از لیست بالا برش های زیر ر اایجاد کنید
# ['d', 'e']
# ['b', 'c']
# ['b', 'c','d]

# ex 3 : string='abcdefghi'
# از رشته بالا برش های زیر را ایجاد نمائید:
# abc
# cd
# def
# hi
# fgh
