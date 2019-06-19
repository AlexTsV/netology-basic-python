class Read_file:

    cook_book = {}

    def get_dict(self):
        with open('recipe.txt') as f:
            for line in f:
                name = line.strip()
                self.cook_book[name] = []
                f.readline()
                i = 0
                while i == 0:
                    ingridients = f.readline()
                    if len(ingridients) > 1:
                        ingridients = ingridients.strip()
                        ingridients = ingridients.split(' | ')
                        in_cook_book = {'ingridient_name': ingridients[0], 'quantity': ingridients[1], 'measure': ingridients[2]}
                        self.cook_book[name].append(in_cook_book)
                    else:
                        i += 1
        print(self.cook_book)



    def get_shop_list_by_dishes(dishes, person_count):
        list = []
        ingridients = {}
        for name in dishes:
            for key, value in Read_file.cook_book.items():
                if name == key:
                    for i in value:
                        list.append(i['ingridient_name'])
                        setlist = set(list)
                        if len(setlist) == len(list):
                            ingridients[i['ingridient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity'])*person_count}
                        else:
                            diff = len(list) - len(setlist)
                            ingridients[i['ingridient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count * (diff + 1)}
        for key, value in ingridients.items():
            print(key, value)



Read_file.get_dict(Read_file)

Read_file.get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
