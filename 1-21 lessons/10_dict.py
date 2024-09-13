da = {4:6, 'text': 'ratata', 'name': 'Mytka'}
# da = dict( num = 6, text = 'ratata')
# print(da["text"], da[4])

# print(da.items())

for key, value in da.items():
    print(key, value, sep=" — ")

# ---------------------------------------------------------------------------

print(da["text"])      # выводит слово за ключем
print(da.get("text"))  # выводит слово за ключем
da.clear()             # очищает
da.pop("text")         # удаляет за ключем
da.popitem()           # удаляет ласт елемент
print(da.keys())       # показывает все ключи
print(da.values())     # показывает все значения
print(da.items())      # показывает ключи + значения в картежах
da[4] = 'barak'        # заменяет значение

# ---------------------------------------------------------------------------

person = {
    'user_1': {
        'name': 'John',
        'age': '46',
        "weight": "97 kg",
        "adress": ["Город", "Улица", "Дом"],
        "grades": {'math': '5', 'history': '4'}
    },
    'user_2': {
    }
}
print(person['user_1']['adress'][2])

