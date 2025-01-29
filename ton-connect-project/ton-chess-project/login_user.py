import mysql.connector
import bcrypt

# Функция для подключения к базе данных
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="chess_user",
        password="your_password",
        database="chess_game"
    )

# Функция для входа пользователя
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    db_connection = connect_to_db()
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        stored_password = user[2]  # Пароль из базы данных (хешированный)
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            print("Login successful!")
        else:
            print("Invalid password.")
    else:
        print("User not found.")

    cursor.close()
    db_connection.close()

if __name__ == "__main__":
    login_user()
