with open("data.txt", 'a') as file:

    x = [str(i * 2) for i in range(0,100)]

    msg = "\n".join(x)

    print()

    file.write(msg)

'''
r = read only
w = write with truncate
x = open for exclusive creation
a = append
b = binary
t = text mode
+ = updating
'''