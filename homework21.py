file_name = "text.txt"
with open(file_name, mode="r", encoding='utf8') as file:
    for list in file:
        print(list, end='')

print(file)