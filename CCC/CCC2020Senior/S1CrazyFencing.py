n = int(input())
student = []
answers = []
correct = 0

for i in range(n):
    response = input()
    student.append(response)

for i in range(n):
    answer = input()
    answers.append(answer)

for i in range(n):
    if student[i] == answers[i]:
        correct += 1

print(correct)