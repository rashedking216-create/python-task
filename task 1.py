x = 30
if x > 30:
    print('it is a very hot day')
else:
    print('it is a hot day . stay hydrated')

x2 = 10 
if x2 > 29:
    print('x2 is less than 29')
elif x2 < 20:
    print("it is warm day . enjoy the weather ")
else:
    print('x2 is 29 or more')

x3 = 15
if x3 > 19:
    print('x3 is less than 19')
elif x3 > 10:
    print('it is a cool day . wear a jacket')
else:
    print('x3 is 19 or more')

x4 = 9
if x4 < 10:
    print('it is a cold day . stay warm')
else:
    print("it is cool")

for x5 in range(21):
    print(x5)
else:
    message = 'even' if x5 % 3 else 'odd'
    print(message)

for x6 in range(1, 21):
    if x6 % 3:
        continue
    print(x6)