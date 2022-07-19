import requests


def count_letters() -> dict:

    url = 'https://ru.wikipedia.org/w/api.php'

    params = {
        'action': 'query',
        'format': 'json',
        'list': 'categorymembers',
        'cmtitle': 'Category:Животные_по_алфавиту',
        'cmlimit': 500,
    }

    dict_with_letters = {}

    while True:
        response = requests.get(url=url, params=params)
        result = response.json()

        for i in result.get('query').get('categorymembers'):
            if i.get('title')[0] not in dict_with_letters:
                dict_with_letters[i.get('title')[0]] = 1
            else:
                dict_with_letters[i.get('title')[0]] += 1
        try:
            params['cmcontinue'] = result.get('continue').get('cmcontinue')
            params['continue'] = result.get('continue').get('continue')
        except AttributeError:
            break

    return dict_with_letters


if __name__ == '__main__':
    print(count_letters())
