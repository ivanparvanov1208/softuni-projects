start = int(input())
end = int(input())

string = ""

for i in range(start, end + 1):
    string += chr(i) + " "

print(string)