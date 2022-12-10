#a = 123
#b# = 1.23
#value = None
# print(a) #
# print(b)#
# print(type(a)) #
# print(type(b)) #
# value = 34
#print(type(value))
#s = "'hello \nbaby'"
#print(a, '-', b, '-', s)
#print('{1} - {2} - {0}'.format(a, b, s))
#print(f'{a} - {b} - {s}')
#f = False
#print(f)
#list = [ '5', '6', '7', 'hello']
#print(list)
#
#print('Enter a')
#a = float(input())
#print('Enter b')
#b = float(input())
#print('Enter c')
#c = input()
#print(a, '-', b, '-', c)
#print('{1} - {2} - {0}'.format(a, b, c))
#print(f'{a} - {b} - {a+b}')
#
#a = 5
#b = 3
#c= a%b
#d = a** b
#print(c)
#print(d)
#f = 3
#g = 1.987654
#h = round(g*f, 5)
#print(h)
#fu = 1
#d = 34
#j= 78
  
#print(fu < d >j)
#f = 1 > 7 or 7>88
#print(f)

#g = [1,3, 5,6,7]
#print(g)
#print(not 3 in g)

#is_odd = g[0] % 2
#print(is_odd)
#a = int(input('a ='))
#b = int(input('b='))
#if a>b:
 #   print(a)
#else:
#    print(b)

#username = input('введите имя:')
#if username == 'Маша':
#    print('ура это же Маша')
#elif username == 'Марина':
#    print('Марина, я так Вас ждала')
#elif username == 'Ильнар':
#    print('Ильнар - топ')
#else:
#    print('Привет, ', username)

#original = 23
# inverted =0
# while original !=0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#    print(original)
#else:
#    print('Пожалуй, \nхватит)')
#print(inverted)
#list = [1,2,65, 33]
#r = range(10)
#for i in range(1,30, 5):
#    print(i)
#for i in 'qwert - uio':
#    print(i)
text = 'съешь еще этих мягкий французских булок'
print(len(text))
print('еще' in text)
print(text.isdigit)
print(text.lower)
print(text.replace('еще', 'ЕЩЁ'))
print(text[0])
print(text[len(text)-9])
print(text[-9])
print(text[:])
print(text[2:5])
print(text[2:-20])
print(text[::6])
# списки
numbers = [1, 4, 6, 88, 9]
ran = range(1, 6)
print(type(ran))
numbers = list(ran)
print(type(numbers))
print(numbers)
numbers[0] = 100
print(f'{len(numbers)}len')
print(numbers)
for i in numbers:
    i *=2
    print(i)
print(numbers)

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)
colors.append('gray')
for e in colors:
    print(e*2)
print(colors == ['red', 'green', 'blue', 'gray'])
colors.remove('red')
print(colors)
del colors[0]
print(colors)

def f(x):
    if x ==1:
        return 'Целое'
    elif x ==2.3:
        return 23
    else:
        return
arg = 1
print(f(arg))
print(type(f(arg)))
arg = 2.3
print(f(arg))
print(type(f(arg)))
arg = 2
print(f(arg))
print(type(f(arg)))