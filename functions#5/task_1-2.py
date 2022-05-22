def show_people(**kwargs):
    documents_ = kwargs['documents']
    num_document = input('Введите номер документа : ')
    for document in documents_:
        if document['number'] == num_document:
            return f'Документ c номером "{num_document}" принадлежит - {document["name"]}\n'
    return f'Документ c номером "{num_document}" отсутствует в каталоге\n'


def show_shelf(**kwargs):
    directories_ = kwargs['directories']
    num_document = input('Введите номер документа : ')
    for k, v in directories_.items():
        if num_document in v:
            return f'Документ с номером "{num_document}" находится на полке - {k}\n'
    return f'Документ c номером "{num_document}" отсутствует на полках\n'


def show_list(**kwargs):
    documents_ = kwargs['documents']
    lst_documents = ''
    for document in documents_:
        lst_documents += f'{" ".join(list(document.values()))}\n'
    return lst_documents


def add_document(**kwargs):
    documents_ = kwargs['documents']
    directories_ = kwargs['directories']
    type_document = input('Введите тип документа : ')
    num_document = input('Введите номер документа : ')

    for document in documents_:
        if document['number'] == num_document:
            return f'Документ c номером "{num_document}" уже есть в каталоге\n'

    name = input('Введите имя человека : ')
    num_directory = input('Введите номер полки : ')
    if num_directory not in directories_:
        return f'Документ не был внесен в каталог, указанная полка "{num_directory}" отсутствует\n'

    new_document = dict(zip(list(documents_[0].keys()), [type_document, num_document, name]))
    documents.append(new_document)
    directories[num_directory].append(num_document)

    return f'Новый документ {new_document} успешно добавлен\n' \
           f'Размещен на полке {num_directory}\n'


def delete_document(**kwargs):
    documents_ = kwargs['documents']
    directories_ = kwargs['directories']
    num_document = input('Введите номер документа : ')
    del_doc_directories = False
    del_doc_documents = False
    for lst in directories_.values():
        if num_document in lst:
            lst.remove(num_document)
            del_doc_directories = True
    for document in documents_:
        if document['number'] == num_document:
            documents.remove(document)
            del_doc_documents = True
    if del_doc_directories and del_doc_documents:
        return f'Документ с номером "{num_document}" удален из архива\n'
    if del_doc_directories:
        return f'Документ с номером "{num_document}" удален с полки, отсутствует в каталоге\n'
    return f'Документ c номером "{num_document}" отсутствует в архиве\n'


def move_document(**kwargs):
    directories_ = kwargs['directories']
    num_document = input('Введите номер документа : ')
    new_num_directory = input('На какую полку необходимо переместить : ')
    if new_num_directory not in directories_:
        return f'Документ не был перемещен, полка "{new_num_directory}" отсутствует\n'
    del_doc_directories = False
    for lst in directories_.values():
        if num_document in lst:
            lst.remove(num_document)
            del_doc_directories = True
    if not del_doc_directories:
        return f'Документ c номером "{num_document}" отсутствует на полках\n'
    directories[new_num_directory].append(num_document)
    return f'Документ номер "{num_document}" был перемещен на полку номер "{new_num_directory}"\n'


def add_shelf(**kwargs):
    directories_ = kwargs['directories']
    new_num_directory = input('Введите номер новой полки [число] : ')
    if not new_num_directory.isdigit():
        return f'Новая полка не добавлена, введено не числовое значение "{new_num_directory}"\n'
    if new_num_directory in directories_:
        return f'Полка с номером "{new_num_directory}" уже есть\n'
    directories[new_num_directory] = []
    return f'Полка с номером "{new_num_directory}" успешно добавлена\n'


def show_help_list(**kwargs):
    commands = kwargs['commands']
    lst_commands = ''
    for k, v in commands.items():
        lst_commands += f'{k} - {v}\n'
    return lst_commands


def main_launch(**kwargs):
    commands = kwargs['commands']
    command = input('Введите команду, ["exit" - выход] : ')
    if command == 'exit':
        return
    if command in commands:
        print({
            'p': show_people,
            's': show_shelf,
            'l': show_list,
            'a': add_document,
            'd': delete_document,
            'm': move_document,
            'as': add_shelf,
            'h': show_help_list
        }[command](documents=documents, directories=directories, commands=user_commands))
    else:
        print(f'Команда "{command}" отсутствует в списке команд,\n'
              f'воспользуйтесь командой "h" для вывода списка возможных команд\n')
    main_launch(**kwargs)


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

user_commands = {
    'p': 'выведет имя человека по номеру документа',
    's': 'выведет номер полки по номеру документа',
    'l': 'выведет список всех документов',
    'a': 'добавит новый документ в каталог и на полку',
    'd': 'удалит документ из каталога и с полки',
    'm': 'переместит документ с текущей полки на целевую',
    'as': 'добавит новую полку в перечень полок',
    'h': 'выведет список возможных команд'
}

if __name__ == '__main__':
    main_launch(documents=documents, directories=directories, commands=user_commands)
