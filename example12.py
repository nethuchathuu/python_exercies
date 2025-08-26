file =open("data.txt", 'w')

x = [str(i * 2) for i in range(0,100)]

msg = "\n".join(x)

print()

file.write(msg)

file.close()