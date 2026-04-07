
import re
from auth_module import authorize, users


def is_valid_name_or_profession(text):
    return not re.search(r'\d', text)


def show_user_profile(user_data):
    while True:
        print("\n--- Ваш профиль ---")
        print(f"Имя: {user_data['name']}")
        print(f"Профессия: {user_data['profession']}")
        print(f"Возраст: {user_data['age']}")
        print("\nЧто вы хотите сделать?")
        print("1. Изменить имя")
        print("2. Изменить профессию")
        print("3. Изменить возраст")
        print("4. Выйти из профиля (завершить программу)")

        choice = input("Ваш выбор (1-4): ").strip()

        if choice == '1':
            new_name = input("Введите новое имя: ").strip()
            if not is_valid_name_or_profession(new_name):
                print("Ошибка: имя не должно содержать цифры!")
            elif new_name == "":
                print("Ошибка: имя не может быть пустым!")
            else:
                user_data['name'] = new_name
                print("Имя успешно обновлено!")

        elif choice == '2':
            new_prof = input("Введите новую профессию: ").strip()
            if not is_valid_name_or_profession(new_prof):
                print("Ошибка: профессия не должна содержать цифры!")
            elif new_prof == "":
                print("Ошибка: профессия не может быть пустой!")
            else:
                user_data['profession'] = new_prof
                print("Профессия успешно обновлена!")

        elif choice == '3':
            new_age = input("Введите новый возраст: ").strip()
            if new_age.isdigit() and 1 <= int(new_age) <= 120:
                user_data['age'] = int(new_age)
                print("Возраст успешно обновлён!")
            else:
                print("Ошибка: возраст должен быть числом от 1 до 120!")

        elif choice == '4':
            print("Выход из программы...")
            return False
        else:
            print("Неверный выбор, попробуйте снова (1-4).")
    return True


def main():
    print("=== Система авторизации и управления профилем ===\n")

    while True:
        # Авторизация пользователя
        current_user = authorize()

        if current_user is None:
            print("Попробуйте снова.\n")
            continue


        should_continue = show_user_profile(current_user)

        if not should_continue:
            break

        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()