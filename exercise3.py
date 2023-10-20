from collections import Counter

def make_list(file_location):
    file_list = []
    open_file = open(file_location, 'r')
    words = open_file.read().split()
    for i in range(len(words)):
        if '.' in words[i]:
            words[i] = words[i].replace('.', '')
        file_list.append(words[i].lower())
    return file_list

file1 = "C:/Python Program/06 file01.txt"
file2 = "C:/Python Program/06 file02.txt"

counter1 = Counter(make_list(file1))
counter2 = Counter(make_list(file2))

result = counter1 & counter2

print('공통된 단어와 각 파일에서의 빈도:')
for key in result:
    print(f'{key}: 파일1 - {counter1[key]} / 파일2 - {counter2[key]}')