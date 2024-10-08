# 	{} — фігурні дужки вказують на місце для форматування значення.
# 	: — використовується для розділення значення і формату.
#   .nf — визначає кількість десяткових знаків.
#   :, — додає коми для розділу тисяч.
# 	:.2% — перетворює число на відсоток і форматує його з двома десятковими знаками.
# 	>, <, ^ — визначають вирівнювання в полі заданої ширини.

# Name = 'Name'
# Share = 'Share'
# Price = 'Price'
# Change = 'Change'

# print(f"{Name:<10} {Share:>10} {Price:^10} {Change:^10}")
# print('---------- '*4)
# print(f"{'AA':<10} {100:>10} {'$9.22':>10} {'-22.98%':>10}")
# print(f"{'IBM':<10} {50:>10} {'$106.28':>10} {'15.18%':>10}")
# print(f"{'CAT':<10} {150:>10} {'$36.46':>10} {'-47.98%':>10}")
# print(f"{'MSFT':<10} {200:>10} {'$20.89':>10} {'-30.34':>10}")
# print(f"{'GE':<10} {95:>10} {'$13.48':>10} {'-26.89%':>10}")
# print(f"{'MSFT':<10} {50:>10} {'$20.89':>10} {'-44.21%':>10}")
# print(f"{'IBM':<10} {100:>10} {'$106.28':>10} {'-36.84%':>10}")

# ------------------------------------------------------------------------

class Book:
    book_name = None
    book_autor = None
    book_year_of_publication = None
    book_count = None
    book_cost = None
    book_rating = None

    def __init__(self, book_name, book_autor, book_year_of_publication, book_count, book_cost, book_rating):
        self.book_name = book_name
        self.book_autor = book_autor
        self.book_year_of_publication = book_year_of_publication
        self.book_count = book_count
        self.book_cost = book_cost
        self.book_rating = book_rating

        self.get_info()
    
    def get_info(self):
        print(f'''
    Інформація про книгу:
    Назва: {self.book_name}
    Автор: {self.book_autor}
    Рік видання: {self.book_year_of_publication}
    Кількість екземплярів: {self.book_count:,}
    Вартість: ${self.book_cost:.2f}
    Рейтинг: {self.book_rating:.2f} 
    ''')

Book('Убити пересмішника','Харпер Лі',1960,1234567,18.99,9.2)

# book1 = Book(input('Введіть назву книги: '),
#              input('Введіть автора (американського автора): '),
#              int(input('Введіть рік видання: ')),
#              int(input('Введіть кількість екземплярів: ')),
#              float(input('Введіть вартість книги: ')),
#              float(input('Введіть рейтинг книги (0-10): '))
#              )
