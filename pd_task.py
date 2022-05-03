#Задание 1
import pandas as pd

authors = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']}, columns=['author_id', 'author_name'])

book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                     'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price': [450, 300, 350, 500, 450, 370, 290]}, columns=['author_id', 'book_title', 'price'])

print(f'Датафрейм, содержащий информацию об авторах книг: \n{authors}'
      f'\n\nДатафрейм, содержащий информацию о названиях книг и их стоимости: \n{book}')

#Задание 2
authors_price = pd.merge(authors, book, on='author_id')
print(f'\nОбъединённый датафрейм, полученный в результате слияния двух исходных датафреймов: \n{authors_price}')

#Задание 3
top5 = authors_price.nlargest(5, 'price')
top5 = top5.reset_index()
print(f'\nДатафрейм, содержащий информацию о пяти самых дорогих книгах: \n{top5}')

#Задание 4
min_price = authors_price.groupby('author_name').agg({'price': 'min'})
min_price = min_price.reset_index()
min_price = min_price.rename(columns={'price': 'min_price'})

max_price = authors_price.groupby('author_name').agg({'price': 'max'})
max_price = max_price.reset_index()
max_price = max_price.rename(columns={'price': 'max_price'})

mean_price = authors_price.groupby('author_name').agg({'price': 'mean'})
mean_price = mean_price.reset_index()
mean_price = mean_price.rename(columns={'price': 'mean_price'})

authors_stat = pd.merge(pd.merge(min_price, max_price, on='author_name'), mean_price, on='author_name')
print(f'\nДатафрейм, содержащий информацию о наибольшей, наименьшей и средней цене книг каждого автора: \n{authors_stat}')

#Задание 5
authors_price['cover'] = ['твёрдая', 'мягкая', 'мягкая', 'твёрдая', 'твёрдая', 'мягкая', 'мягкая']
print(f'\nОбъединённый датафрейм, дополненный информацией о типе обложки каждой книги: \n{authors_price}')

book_info = pd.pivot_table(authors_price, values='price', index='author_name', columns='cover', aggfunc=sum, fill_value=0)
print(f'\nСводная таблица с суммарной стоимостью книг каждого автора в мягкой и твёрдой обложках: \n{book_info}')

book_info.to_pickle('book_info.pkl')
book_info2 = pd.read_pickle('book_info.pkl')
print(f'\nЭкспортированный из файла датафрейм, содержащий информацию сводной таблицы: \n{book_info2}')

if book_info.equals(book_info2):
    print('\nСводная таблица и экспортированный датафрейм идентичны!')
else:
    print('\nСводная таблица и экспортированный датафрейм различаются.')
