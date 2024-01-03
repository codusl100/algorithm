s = input()
n = int(input())
string_list = [ord(str)+n for str in s]
for i in range(len(string_list)):
    if (string_list[i] > 90 and string_list[i] < 97) or string_list[i] > 122:
        string_list[i] -= 26
    elif string_list[i] == 36:
        string_list[i] = ' '

for i in range(len(string_list)):
    if string_list[i] != ' ':
        string_list[i] = chr(string_list[i])
print(''.join(string_list))