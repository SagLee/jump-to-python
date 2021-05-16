food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)
print(food+","+say)

multiline = "Life is too short\nYou need python"
print(multiline)

a = "abc"
print(a*2)

a = "Life is too short, You need Python"
print(a[0]+a[1])

print(a[-1]) #뒤에서 첫번째

print(a[0:3]) #0 <= a < 3
print(a[:10])
print(a[11:])

a="20210508Cloudy"
date=a[:8]
year=a[:4]
day=a[4:8]
wether=a[8:]
print(date)
print(wether)
print(year)
print(day)

print("I eat %d apples" %3)
print("I eat %s apples" %"five")

print("I eat {0} apples".format(12738779))

num=10
d=3
print("I ate {number} apples. so I was sick for {day} days.".format(number=num, day=d))

print("{0:<10}".format("hi")) #왼쪽정렬
print("{0:^10}".format("hi")) #가운데정렬
print("{0:>10}".format("hi")) #오른쪽정렬

name = "sac"
age = 39
print(f"My name is {name}, age is {age}")

abc = "abcdefgabccccaaaacc"
print(abc.count('b'))
print(abc.count("cc"))
print(abc.find('e')) #처음 찾은 e의 위치


