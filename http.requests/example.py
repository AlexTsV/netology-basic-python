import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(path_to_origin, path_to_translate, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    with open(path_to_origin, 'r', encoding='utf-8') as f:
        text = f.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }



    response = requests.get(URL, params=params)
    json_ = response.json()
    res = ''.join(json_['text'])

    with open(path_to_translate, 'w', encoding='utf-8') as f:
        f.write(res)

print(translate_it('ES.txt', 'result_ES.txt', 'es'))


requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', json=dict(a='goo', b='foo'))



