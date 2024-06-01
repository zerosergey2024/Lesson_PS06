class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def info(self):
        print(f"ID: {self._user_id}")
        print(f"Имя: {self._name}")
        print(f"Уровень доступа: {self._access_level}")

class Boss(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'boss'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Новое имя ({user.get_name()}) внесено в список")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь с ID {user_id} удалён из списка.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def info(self):
        print(f"ID: {self._user_id}")
        print(f"Имя: {self._name}")
        print(f"Уровень доступа: {self._access_level}")

if __name__ == "__main__":
    user1 = User(1, "Иван Иванов")
    user2 = User(2, "Петр Петров")
    user1.info()

    boss = Boss(3, "Админ Админов")
    boss.info()

    user_list = []

    boss.add_user(user_list, user1)
    boss.add_user(user_list, user2)

    print("Список пользователей:")
    for user in user_list:
        print(user)

    boss.remove_user(user_list, 1)

    print("\nСписок пользователей после удаления:")
    for user in user_list:
        print(user)



