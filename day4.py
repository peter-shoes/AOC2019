from re import match

list2 = []
list1 = []
increase_list = []
for i in range(134792,675810):
    i = str(i)
    tf = True
    for x in range(len(i)-1):
        if int(i[x])>int(i[x+1]):
            tf = False
            continue
    if tf == True:
        increase_list.append(i)
for i in increase_list:
    for x in range(len(i)-1):
        if i[x] == i[x+1]:
            list1.append(i)
            break
for i in list1:
    dic = {
    '0':0,
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0
    }
    for x in i:
        dic[x]+=1
    if 2 in dic.values():
        list2.append(i)

print(len(list2))
