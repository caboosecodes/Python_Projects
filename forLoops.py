List = [1, 85, 6, 78, 22, 58, 41, 23, 101, 69]

for i in List:
    print(i)
    if i == 22:
        break

#range() returns of sequence of numbers starting at 0
for x in range(10):
    print(x)
#retuns only 0-14

#you can add a starting parameter; in the following code its 2
for y in range(2, 8):
    print(y)
    
#by adding a 3rd parameter you can set the incrementing value in this case 3
for z in range (0, 15, 3):
    print(z)
#only returns up to 12

#will print after 0 to 5 and then the message 'finished'
for a in range(6):
    print(a)
else:
    print('finished')
