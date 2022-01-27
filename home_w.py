#exercise 1
c = input('what is your age:     ')
t = int(input('how old are you:   '))
mood_color = 'blue'
print(mood_color)

a = input('mood color:     ')


#exercise 2
time = int(input('enter time in sec:   '))
hour = t // 3600
min = t % 3600
sec = t % 60
if time < 60:
    print(f"time 00:00:{sec:02}")
elif t < 3600:
    print(f"time 00:{min:02}:{sec:02}")
else:
    print(f"time {hour:02}:{min//60:02}:{sec:02}")

#exercise 3
a = input('enter number:   ')
result = int(a) + int(a+a) + int(a+a+a)
print(f" total: {result}")


#exercise 4
n = int(input('enter number:   '))
max_n = 0
while n > 0:

    if n == 9:
        break
    if n % 10 > max_n:

         max_n = n % 10
    n //= 10
print(f'max number: {max_n}')

#exercise 5-6
p = int(input('enter profit:   '))
l = int(input('enter loss: '))
if p > l:
    print(f' profitability : {p // l}')
    k = int(input('enter numbers employees:   '))
    print(f'profit per person: {p // k}')
else:
    print(f'deficit: {l}')

#exercise 7

d = float(input('enter distance:   '))
tar = float(input('enter target distance:  '))
day = 1
while d < tar:
    d *= 1.1
    day += 1
print(f' summa days: { day}')

