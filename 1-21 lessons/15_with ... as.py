try:
    with open('text.txt', encoding='utf=8') as file:
        file.read()
except FileNotFoundError:
    print("File is no found")


