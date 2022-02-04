# 1

some_typs = [2, 2.3, [3,3,3,3], (123), 'oxana', {1 :'x', 3 :'z'}, 'me']

for a in some_typs:
    print(type(a))

#2

user_input = input('list: ')
input_list = user_input.split()
len_list = len(input_list)
i = 0
if len_list > 1:
    while i < len_list - 1:
        input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
        i += 2

print(input_list)


#3

x_month = input('enter num of month: ')
w,sp, su,  au = 'winter', 'spring', 'summer', 'autumn'
month_dict = {'1': w, '2': w,'3': sp, '4': sp, '5': sp, '6': su, '7': su, '8' : su, '9': au, '10': au, '11' : au, '12': w}
print(month_dict[x_month])

year = [w,w,sp,sp,sp,su,su,su,au,au,au,w]
print(year[int(x_month) - 1])

#4
abraca = input('sentence:  ')
words = abraca.split()
for n, word in enumerate(words):
    print((n + 1), (word[:10]))


#5
my_list = [8,8,8,7,6,5,5,4,3,2,1]
new_num = int(input('enter new_num:  '))
xx = False
for z, y in enumerate(my_list):
    if new_num > y:
        my_list.insert(z,new_num)
        xx = True
        break
if not xx:
    my_list.append(new_num)

print(my_list)

# 6 later