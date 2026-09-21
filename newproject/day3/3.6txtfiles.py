
# общ вид открытия файла
# r-чтение, w-запись(создаст или перезапишет сущ), a-добавит еще данные, r+ - откроет для чтения и записи х - создаст новый файл
# read - чтение всего, readline одну строку, readlines все и возвр список строк
# with open('namefile','w', encoding='utf-8') as name:

#     запись в файл
# with open('test.txt', 'a', encoding='utf-8') as file:
#     file.write('hello wrld\n')
#     a=3
#     b=4
#     file.write(f'a: {str(a)}\nb: {str(b)}\n')

# чтение из файла
# read - чтение всего, readline одну строку, readlines все и возвр список строк
# with open('test.txt', 'r', encoding='utf-8') as file:
#     s=file.read()
#     lst=s.split()
# print(lst)

# второй способ readlines()
# with open('test.txt', 'r', encoding='utf-8') as file:
#     s=file.readlines()
#     for i in range(len(s)):
#         if '\n' in s[i]:
#             s[i]=s[i][:-1]
# print(s)


# чтение файла по строчно readline():
# with open('test.txt', 'r', encoding='utf-8') as file:
#     s=[]
#     while True:
#         line=file.readline().rstrip()
#         s.append(line)
#         if line =='':
#             break
#         # if line[-1]=='\n':
#         #     line=line[:-1]
#         print(line)


