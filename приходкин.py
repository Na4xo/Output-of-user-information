
users = [
    {
        "login": "user1",
        "password": "+",
        "name": "Иван Иванов",
        "profession": "Инженер",
        "age": 30
    },
    {
        "login": "user2",
        "password": "pass2",
        "name": "Мария Петрова",
        "profession": "Дизайнер",
        "age": 25
    }
]


def find_user(login):
    for user in users:
        if user["login"] == login:
            return user
    return None


def authorize():
    login = input("Введите логин: ")
    user = find_user(login)
    if user is None:
        print("Пользователь не найден.")
        return None

    attempts = 3
    while attempts > 0:
        password = input("Введите пароль: ")
        if password == user["password"]:
            print(f"\nДобро пожаловать, {user['name']}!\n")
            return user
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Неверный пароль. Попробуйте ещё раз. Осталось попыток: {attempts}")
            else:
                print("Превышено количество попыток. Доступ заблокирован.")
                return None


if __name__ == "__main__":

    user = authorize()
    if user:
        print("Авторизация успешна!")
