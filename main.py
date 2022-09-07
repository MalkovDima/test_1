
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def name_by_number(docs):
    number = str(input('Введите номер документа: '))
    name = 'Документа с таким номером нет!!!'
    for x in docs:
        if x['number'] == number:
            name = x['name']
    return name


def shelf_by_number(dirs):
    number = str(input('Введите номер документа: '))
    shelf = 'Документа с таким номером нет на полках!!!'
    for x, y in dirs.items():
        for z in y:
            if z == number:
                shelf = x
    return shelf


def all_documents(docs):
    result = ""
    for xx in docs:
        for yy, zz in xx.items():
            if yy == 'type':
                #print(zz, end=' ')
                result = result + zz + ' '
            elif yy == 'number':
                #print(f'''"{zz}"''', end=" ")
                result = result + f'''"{zz}"''' + ' '
            else:
                #print(f'''"{zz}"''')
                result = result + f'''"{zz}"''' + '\n'

    return result


def new_data(docs, dirs):
    number = str(input('Введите номер документа: '))
    type = str(input('Введите тип документа: '))
    name = str(input('Введите имя владельца: '))
    new_document = {
        "type": type,
        "number": number,
        "name": name
    }
    docs.append(new_document)
    shelf_number = int(input('Введите номер полки: '))
    if shelf_number > len(dirs):
        result = 'Такого номера полки не существует!!!'
    else:
        dirs[f'{shelf_number}'].append(number)
        result = 'Запись получилась'
    return result


def delete_data(docs, dirs):
    number = str(input('Введите номер '
                       'документа: '))
    n = -1
    in_document = False
    for x in docs:
        n += 1
        if x["number"] == number:
            docs.pop(n)
            in_document = True
    if not in_document:
        result = 'Документ с таким номером отсутсвует'
    else:
        for x, y in dirs.items():
            for n in y:
                if n == number:
                    y.remove(number)
                    result = 'Запись удалена'
    return result


def change_shelf(docs, dirs):
    in_doc = False
    number = str(input('Введите номер документа у которого нужно поменять полку: '))
    for x in docs:
        if x['number'] == number:
            in_doc = True
    if not in_doc:
        print('Документ с таким номером отсутствует!!!')
    else:
        while x != 1:
            shelf_number = int(input('Введите номер полки: '))
            if shelf_number > len(dirs):
                print('Такого номера полки не существует!!!')
            else:
                for x, y in dirs.items():
                    for n in y:
                        if n == number:
                            y.remove(number)
                            dirs[f'{shelf_number}'].append(number)
                break
                x = 1


def new_shelf(dirs):
    new_shelf_number = int(input('Введите номер полки: '))
    if f'{new_shelf_number}' in directories:
        print('Такой номер полки уже существует!!!')
    else:
        dirs[f'{new_shelf_number}'] = []


def main(doc, dir):
    while True:
        command = str(input('ведите команду: '))
        if command == "p":
            print(name_by_number(doc))
        elif command == "s":
            print(shelf_by_number(dir))
        elif command == "l":
            print(all_documents(doc))
        elif command == "a":
            print(new_data(doc, dir))
        elif command == "d":
            print(delete_data(doc, dir))
        elif command == "m":
            change_shelf(doc, dir)
        elif command == "as":
            new_shelf(dir)
        elif command == "q":
            break


if __name__ == '__main__':
    main(documents, directories)