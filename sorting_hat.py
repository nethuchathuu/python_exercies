# Write code below 💖

gryffindor=0
ravenclaw=0
hufflepuff=0
slytherin=0

print("SORTING HAT")

print()

print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

print()

answer1 = int(input("Enter answer(1-2): "))

print()

if answer1 == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif answer1 == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print('Wrong input.')

print()
print()

print("Q2) When I'm dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

print()

answer2 = int(input('Enter your answer (1-4): '))

print()

if answer2 == 1:
  hufflepuff = hufflepuff + 2
elif answer2 == 2:
  slytherin = slytherin + 2
elif answer2 == 3:
  ravenclaw = ravenclaw + 2
elif answer2 == 4:
  gryffindor = gryffindor + 2
else:
  print('Wrong input.')

print()
print()

print('Q3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

print()


answer3 = int(input('Enter your answer (1-4): '))

print()

if answer3 == 1:
  slytherin = slytherin + 4
elif answer3 == 2:
  hufflepuff = hufflepuff + 4
elif answer3 == 3:
  ravenclaw = ravenclaw + 4
elif answer3 == 4:
  gryffindor = gryffindor + 4
else:
  print('Wrong input.')

print()
print()
  
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

print()
print()

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')