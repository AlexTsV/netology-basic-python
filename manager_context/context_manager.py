cook_book = {}
import time


class Myopen:
    def __init__(self, file_path):
        self.file_path = file_path
        global start_time
        start_time = time.monotonic()

    def __enter__(self):
        self.file = open(self.file_path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        end_time = time.monotonic()
        print('Время начало работы:', start_time, 'Время конца работы:', end_time, 'Продолжительность', start_time - end_time)



def get_dict():
    with Myopen('recipe.txt') as f:
        for line in f:
            name = line.strip()
            cook_book[name] = []
            f.readline()
            i = 0
            while i == 0:
                ingridients = f.readline()
                if len(ingridients) > 1:
                    ingridients = ingridients.strip()
                    ingridients = ingridients.split(' | ')
                    in_cook_book = {'ingridient_name': ingridients[0], 'quantity': ingridients[1], 'measure': ingridients[2]}
                    cook_book[name].append(in_cook_book)
                else:
                    i += 1
    print(cook_book)

get_dict()



