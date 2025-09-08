from os import path

file_name = "data.txt"

#if path.exists(file_name):
 #   with open(file_name) as file:
  #      print(file.readline())

#else:
 #   print("File not found")
#


x = 10
y = 1

try:
    z = x / y
    print(z)


    with open(file_name) as file:
        print(file.readline())



except ZeroDivisionError as e:
    print("input error", e)

except FileNotFoundError as e:
    print("File not found", e)

except Exception as e:
    print("Something went wrong", e)

finally:
    print("Process completed")