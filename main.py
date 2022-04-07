from time import time as tm
import codecs, random, os.path


def cheching_for_start():
    main_katalog = os.path.isdir('texts_for_reading')
    extara_katalog = os.path.isdir('texts_for_reading/extra_files')
    if main_katalog and extara_katalog:
        list_for_check = ['texts_for_reading/texts_light_level.txt',
                          'texts_for_reading/texts_medium_level.txt',
                          'texts_for_reading/texts_hard_level.txt',
                          'texts_for_reading/extra_files/choice.txt']
        for i in list_for_check:
            check_file = os.path.exists(i)
            if not check_file:
                return False
        return True
    return False


def greeting():
    answer = input('Здравствуйте пользователь! \nВы готовы проверить свою скорость выразительного чтения? \n').lower()
    while answer not in p_n:
        answer = input('Я вас не понял... \n').lower()
    if answer in positive:
        prepare_to_read()
    elif answer in negative:
        print('Хорошего времяпровождения!')


def prepare_to_read():
    print('Выберите режим: \n' + "\n".join(list_of_offers))
    answer = input()
    while not answer.isdigit() or not 0 < int(answer) < 4:
        answer = input('Неправильный формат данных! Введите снова: \n')
    if answer == '3':
        print('До свидания')
        return
    if answer == 'Отменить' or answer == 'idw':
        print('До свидания!')
        return
    choices(list_of_func[int(answer) - 1])


def choice_of_text():
    item = 0
    print('Выбирите номер текста:', '\n')
    file_choice = codecs.open("texts_for_reading/extra_files/choice.txt", 'r', 'utf_8_sig')
    data_choice = list(map(str.strip, file_choice.readlines()))
    file_choice.close()
    counter = 0
    for i in range(len(data_choice)):
        if data_choice[i][0] == '~':
            print(data_choice[i])
            counter += 1
        else:
            print(f'\t{i + 1 - counter})', data_choice[i])
    answer = input()
    while not answer.isdigit() or not 0 < int(answer) <= len(data_choice):
        answer = input('Неправильный формат данных! Введите снова: \n')
    answer = int(answer)
    if answer <= 2:
        item = 1
    elif answer >= 4:
        item = 3
    else:
        item = 2
    reading(answer - 1 - len(data_choice[:answer]), item)


def choices(func):
    print('working...')
    return func()


def not_eyes_choise():
    item = random.randint(1, len(list_of_text))
    rand = random.randint(0, len(list_of_text[item]) - 1)
    reading(rand, item)


def proof():
    print('Вам будет предоставлен тект, который вы должны прочитать. \n'
          '\tПо прочтению подтвердите ваше окончание командой - "stop" или "s"')
    answer = input('Готовы?\n').lower()
    while answer not in p_n:
        answer = input('Ответьте понятнее: \n').lower()
    if answer in positive:
        print('Поехали!')
        print('-' * 15)
        return
    elif answer in negative:
        print('Эм... Ну ладно... До свидания!')
        exit()


def answer_and_ask(time, limit):
    print(f'Ваш результат {time}')
    print('==' * 10)
    if time <= limit * 0.75:
        answer = input('Вы его точно прочитали? \n')
        while answer not in p_n:
            answer = input('Я не понимаю): \n').lower()
        if answer in positive:
            prepare_to_read()
        elif answer in negative:
            print('За чем тогда вы сюда пришли?')
    elif time <= limit:
        print('Моолодец! Это отличный результат')
    elif time <= limit * 1.3:
        print('Это приемлемый результат')
    else:
        print('Это довольно посредственный результат')
    print('==' * 10)
    answer = input('Продолжить чтениe?\n').lower()
    while answer not in p_n:
        answer = input('Я не понимаю(: \n').lower()
    print('~~' * 15)
    if answer in positive:
        prepare_to_read()
    elif answer in negative:
        print('Прощайте!')
        exit()


def timer():
    time_start = 0
    time_start = tm()
    answer = input().lower()
    while not answer in ['stop', 's', 'с', 'стоп']:
        print('Неизвестная команда!')
        answer = input()
    else:
        time = round(tm() - time_start, 2)
        time_start = 0
    return time


def reading(number, item=1):
    start_line, stop_line, a, limit = list_of_text[item][number]
    proof()
    file = codecs.open(list_of_files[item - 1], 'r', 'utf_8_sig')
    for i, line in enumerate(file):
        if i < start_line:
            continue
        if i == stop_line:
            break
        line = line.replace("\n", "")
        if i >= start_line:
            print(line)
    file.close()
    time = timer()
    answer_and_ask(time, limit)


if cheching_for_start():
    positive = ['y', 'yes', 'lets do it', 'да', 'давай', 'приступай', 'д']
    negative = ['n', 'no', 'not do it', 'нет', 'отказываюсь', 'я не хочу', 'н']
    p_n = positive + negative
    list_of_offers = ['1) Выбрать текст самостоятельно.', '2) Выбор текста в слепую.', '3) Закрыть приложение.']
    list_of_func = [choice_of_text, not_eyes_choise]
    list_of_files = ['texts_for_reading/texts_light_level.txt',
                     'texts_for_reading/texts_medium_level.txt',
                     'texts_for_reading/texts_hard_level.txt']
    list_of_text = {1 : [(0, 9, 1, 36), (11, 23, 2, 41)], # Журавли / Синицы
                    2 : [(0, 17, 1, 81)], # Дуб
                    3 : [(0, 22, 1, 121)]} # Глазки
    greeting()
else:
    print("Не хватает важных данных!")
