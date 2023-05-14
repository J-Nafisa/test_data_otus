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
    total_books = len(books)
    total_users = len(users)
    books_per_user = total_books // total_users
    remaining_books = total_books % total_users

    available_books = books.copy()  # Создаем копию списка книг для распределения

    for user in users:
        user['books'] = []  # Создаем пустой список книг для каждого пользователя

    for _ in range(books_per_user):
        for user in users:
            if available_books:
                book = available_books.pop(0)  # Извлекаем первую доступную книгу из списка
                user['books'].append({
                    'title': book['Title'],
                    'author': book['Author'],
                    'pages': int(book['Pages']),
                    'genre': book['Genre']
                })

    for _ in range(remaining_books):
        if available_books:
            book = available_books.pop(0)  # Извлекаем первую доступную книгу из списка
            user = users[_ % total_users]  # Равномерно распределяем оставшиеся книги между пользователями
            user['books'].append({
                'title': book['Title'],
                'author': book['Author'],
                'pages': int(book['Pages']),
                'genre': book['Genre']
            })
        else:
            break

    return users

# Сохраняем результат в JSON файл
def save_result(result):
    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4)

# Основная логика скрипта
def main():
    books = read_books_data()
    users = read_users_data()

    # Создаем новый список пользователей с нужными полями
    result_users = []
    for user in users:
        result_user = {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': []
        }
        result_users.append(result_user)

    result = distribute_books(books, result_users)
    save_result(result)


if __name__ == '__main__':
    main()
