def  get_top_student(subject: str, dataset: dict):
    max_marks= 0
    max_student = ""

    for name, marks in dataset.items():
        if marks > max_marks:
            max_marks = marks
            max_student = name

    return max_student,max_marks

def get_marks(recod: tuple):
    return recod[1]

lines = None

with open("data2.txt") as file:
    lines = file.readlines()

if not lines:
    print("somthing went wrong")
    exit()

marks_lines = lines[1:]

subject_marks = {}
student_marks = {}

for line in marks_lines:
    entries = line.split(',')

    name = entries[0].strip()
    subject = entries[1].strip()
    marks = int(entries[2].strip())

    if subject not in subject_marks:
        subject_marks[subject]  = {}

    subject_marks[subject][name] = marks

    prev_marks = student_marks.get(name, 0)
    student_marks[name] = prev_marks + marks

message = []

for subject, dataset in subject_marks.items():
    name, marks = get_top_student(subject, dataset)

    msg = f'Top student for {subject} is {name} with {marks} marks'

    print(msg)
    message.append(msg)

print()

#print(student_marks)

marks_list = [
    (name, marks) for name, marks in student_marks.items()
]

marks_list.sort(key=get_marks, reverse = True)

top = marks_list[0]

msg = (f"Top student is {top[0]} with {top[1]} marks")

message.append(msg)

print(msg)

with open('results.txt', 'w') as outputfile:
    for msg in message:
        outputfile.write(msg)
        outputfile.write("\n")

#print(subject_marks)
