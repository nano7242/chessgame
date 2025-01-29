import mysql.connector
import bcrypt

# Подключаемся к базе данных
conn = mysql.connector.connect(
    host="localhost",
    user="chess_user",
    password="your_password",
    database="chess_game"
)
cursor = conn.cursor()

# Функция для регистрации нового пользователя
def register_user(username, password, email):
    # Хешируем пароль с использованием bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Добавляем пользователя в базу данных
    query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, hashed_password, email))
    conn.commit()
    print(f"User {username} registered successfully!")

# Пример использования
username = input("Enter username: ")
password = input("Enter password: ")
email = input("Enter email: ")

register_user(username, password, email)

# Закрываем соединение
cursor.close()
conn.close()
