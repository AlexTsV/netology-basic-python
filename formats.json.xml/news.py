import json
import xml.etree.ElementTree as ET

def sort_for_json():
    list = []
    with open('newsafr.json', encoding='utf-8') as data:
        news = json.load(data)
        for key, value in news.items():
            for i, n in value.items():
                if i == 'channel':
                    for k, v in n.items():
                        if k == 'items':
                            for el in v:
                                e = (el['description']).split(' ')
                                for i in e:
                                    if len(i) > 6:
                                        list.append(i)
    print(*sorted(set(list), key=list.count, reverse=True)[:6], sep='\n')

# sort_for_json()

def sot_for_xml():
    list = []
    tree = ET.parse('newsafr.xml')
    description_el = tree.findall('channel/item/description')
    for desc in description_el:
        elems = (desc.text.split(' '))
        for elem in elems:
            if len(elem) > 6:
                list.append(elem)
    print(*sorted(set(list), key=list.count, reverse=True)[:6], sep='\n')

sot_for_xml()


# example func sorted

# my_list = [
#   'apple',
#   'banana',
#   'banana',
#   'orange',
#   'apple',
#   'kiwi',
#   'banana',
#   'apple',
#   'kiwi',
#   'banana'
# ]
#
# print(my_list)
#
# # сортируем по самому часто встречающемуся слову:
#
# my_list_sorted = sorted(my_list, reverse=True, key=lambda x: my_list.count(x))
#
# print(my_list_sorted)
