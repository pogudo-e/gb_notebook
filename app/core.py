# Имя файла БД. В последующем можно добавить настройки с возможностью смены файла
def file_name():
    '''DATABASE . TXT'''
    return 'database.txt'

# На вход получает файл и возвращает двумерный массив
def array(file):
    '''Full array objects: [[1,2,3][1,2,3][1,2,3]]'''
    file1 = open(file)
    file1.close
    res = []
    for line in file1:
        arr = line.split()
        res.append(arr)
    return res

# Находит максимальный id из имеющихся и возвращает id+1
def find_id():
    '''Folling the maximum identificator max < id '''
    count = 1
    arr = array(file_name())
    for i in range(0, len(arr)):
        if int(arr[i][0]) > count:
            count = int(arr[i][0])  
    return str(count+1)
