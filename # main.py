# main.py
from auth_module import authorize
from profile_module import show_user_profile

def main():
    print("=== Система авторизации и управления профилем ===\n")
    
    while True:
        # Шаг 1: Авторизация пользователя
        current_user = authorize()
        
        if current_user is None:
            print("Попробуйте снова.\n")
            continue
        
        # Шаг 2: Работа с профилем
        result = show_user_profile(current_user)
        
        if result == "exit":
            break
        elif result == "reauth":
            print("\n" + "="*50 + "\n")
            continue

if __name__ == "__main__":
    main()