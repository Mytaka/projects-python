import wikipediaapi
import webbrowser
import random

def get_random_wikipedia_article():
    wiki = wikipediaapi.Wikipedia('en')
    random_title = wiki.random(pages=1)[0]
    page = wiki.page(random_title)
    return page.fullurl


while True:
    user_input = input("Хотите отобразить случайную статью Википедии? (да/нет): ").strip().lower()
    if user_input == 'да':
        url = get_random_wikipedia_article()
        print(f"Открываю случайную статью: {url}")
        webbrowser.open(url)
    elif user_input == 'нет':
        print("Программа завершена.")
        break
    else:
        print("Пожалуйста, введите 'да' или 'нет'.")

