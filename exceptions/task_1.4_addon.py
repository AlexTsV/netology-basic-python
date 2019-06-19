documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "10006"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def command(cmd):
    cmd = input('Введите команду: ')
    if cmd == 'p':
        people()
    if cmd == 'l':
        all_docs()
    if cmd == 's':
        shelf()
    if cmd == 'a':
        add()
    if cmd == 'd':
        delete()
    if cmd == 'm':
        move()
    if cmd == 'as':
        add_shelf()
    if cmd == 'an':
        all_name()
    if cmd == 'q':
        print('bye!')
        return cmd


def people():
    doc_num = (input('Введите номер документа для поиска: '))
    i = 0
    for doc in documents:
        for key, value in doc.items():
            if value == doc_num:
                print('Документ принадлежит: {}'.format(doc['name']))
                i += 1
    if i == 0:
        print('Такого документа нет!')


def all_docs():
    for doc in documents:
        print('{} "{}" "{}"'.format(doc['type'], doc['number'], doc['name']))


def shelf():
    doc_num = (input('Введите номер документа: '))
    i = 0
    for directory, value in directories.items():
        for num in value:
            if num == doc_num:
                print('Документ на полке № {}'.format(directory))
                i += 1
    if i == 0:
        print('Такого документа нет!')


def add():
    counter_doc = 0
    counter_shelf = 0
    doc_num = input('введите номер документа для добавления: ')
    for doc in documents:
        for key, value in doc.items():
            if value == doc_num:
                counter_doc += 1
                print('Документ уже существует')
    if counter_doc == 0:
        doc_type = input('введите тип документа для добавления: ')
        doc_name = input('введите имя владельца для добавления: ')
        shelf_num = input('На какую полку добавить документ: ')
        if shelf_num in directories:
            counter_shelf += 1
        else:
            print('Такой полки не существует')
        if counter_doc == 0 and counter_shelf != 0:
            new_doc = {}
            new_doc['type'] = doc_type
            new_doc['number'] = doc_num
            new_doc['name'] = doc_name
            documents.append(new_doc)
            directories[shelf_num].append(doc_num)
            print(documents)
            print(directories)


def delete():
    doc_num = input('Введите номер документа для удаления: ')
    i = 0
    for document in documents:
        if document.get('number') == doc_num:
            i += 1
            position = documents.index(document)
            documents.pop(position)
            print(documents)
    if i == 0:
        print('Такого документа нет')
    else:
        for shelf, value in directories.items():
            for number in value:
                if number == doc_num:
                    position = value.index(number)
                    value.pop(position)
                    print(directories)


def move():
    counter_doc = 0
    doc_num = input('Введите номер документа для перемещения: ')
    for document in documents:
        if document.get('number') == doc_num:
            counter_doc += 1
    if counter_doc != 0:
        shelf_num = input('На какую полку перенести №? ')
        if shelf_num in directories:
            for shelf, value in directories.items():
                for number in value:
                    if number == doc_num:
                        position = value.index(number)
                        value.pop(position)
                        directories[shelf_num].append(doc_num)
        else:
            print('Такой полки не существует')
    else:
        print('Такого документа не существует')
    print(directories)


def add_shelf():
    num_shelf = input('Введите номер новой полки: ')
    if num_shelf in directories:
        print('Такая полка уже есть')
    else:
        directories[num_shelf] = []
    print(directories)

def all_name():
    i = 0
    try:
        for document in documents:
            i += 1
            print('Владелец: {}, Тип: {}, Номер: {}'.format(document['name'], document['type'], document['number']))

    except KeyError:

        print('Здесь нет владельца', documents[i-1])


while True:
    if command('q'):
        break

