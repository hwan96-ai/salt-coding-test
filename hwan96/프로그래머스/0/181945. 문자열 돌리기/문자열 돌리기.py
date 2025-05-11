str = input()


result = ""
for i in range(0, len(str), 1):
    chunk = str[i:i+1]
    result += chunk + "\n"

print(result)
