import csv
import json

# Разбираем CSV файл
def read_books_data():
    books = []
    with open('books.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

# Разбираем JSON файл
def read_users_data():
    with open('users.json', 'r') as file:
        users = json.load(file)
    return users

# Распределяем книги между пользователями
def distribute_books(books, users):
    result = []

    for user in users:
        # Создаем новый объект с нужными полями из users.json
        result_user = {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': []
        }

        total_books = len(books)
        total_users = len(users)
        books_per_user = total_books // total_users
        remaining_books = total_books % total_users
        book_index = 0

        # Распределяем книги для каждого пользователя
        for i in range(books_per_user):
            if book_index >= total_books:
                break
            result_user['books'].append({
                'title': books[book_index]['Title'],
                'author': books[book_index]['Author'],
                'pages': int(books[book_index]['Pages']),
                'genre': books[book_index]['Genre']
            })
            book_index += 1

        # Распределяем оставшиеся книги
        for i in range(remaining_books):
            if book_index >= total_books:
                break
            result_user['books'].append({
                'title': books[book_index]['Title'],
                'author': books[book_index]['Author'],
                'pages': int(books[book_index]['Pages']),
                'genre': books[book_index]['Genre']
            })
            book_index += 1

        result.append(result_user)

    return result

# Сохраняем результат в JSON файл
def save_result(result):
    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4)

# Основная логика скрипта
def main():
    books = read_books_data()
    users = read_users_data()
    result = distribute_books(books, users)
    save_result(result)


if __name__ == '__main__':
    main()
