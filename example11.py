name = "nethu"
height = 176
 
#message = "hello " + name + " your hight = " + str(height)

#message = "hello %s, your height is %05d" %(name,height)

message = f"hello {name}, your hight is {height:05d}"

print(message)