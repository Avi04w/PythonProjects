num_lines = int(input())
string = ""

while num_lines > 0:
    line = input()
    string += line
    num_lines -= 1

num_s = 0
num_t = 0

for i in string:
    if i == "s" or i == "S":
        num_s += 1
    elif i == "t" or i == "T":
        num_t += 1

if num_s > num_t:
    print("French")
elif num_t > num_s:
    print("English")
elif num_s == num_t:
    print("French")