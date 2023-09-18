class User:
    def __init__(self, id: int, email: str, name: str, deactivated: bool):
        self.ID = id
        self.Email = email
        self.Name = name
        self.Deactivated = deactivated

# 作成する。同じ ID が DB 上にあったり、ID が重複するとエラー
def CreateUsers(users: list[User]):
    pass

# 更新する。ID が DB 上にないとエラー
def UpdateUsers(users: list[User]):
    pass

# メールアドレスからユーザーを読み取る
def ListUsersByEmail(emails: list[str]) -> list[User]:
    pass

def FreshUserId():
    pass

# メールアドレスのリストを受け取り、新しくユーザーを登録する
def CreateUsersFromList(emails: list[str]) -> None:
    email_unique = list(set(emails))
    users = ListUsersByEmail(email_unique)
    already_registered = set()
    Old_users = []
    for user in users:
        already_registered.add(user.Email)
        if user.Deactivated:
            user.Deactivated = False
            Old_users.append(user)
    UpdateUsers(Old_users)

    # 新しく登録するメールアドレスについて、Userのインスタンスを作成し、DBの保存
    New_users = []
    for email in email_unique:
        if not email in already_registered:
            new_id = FreshUserId()
            user = User(new_id, email, '', False)
            New_users.append(user)
    CreateUsers(New_users)