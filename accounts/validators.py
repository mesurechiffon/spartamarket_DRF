from .models import User


def validate_user_data(user_data):
    username = user_data.get("username")
    password = user_data.get("password")
    nickname = user_data.get("nickname")
    birth = user_data.get("birth")
    first_name = user_data.get("first_name")
    last_name = user_data.get("last_name")
    email = user_data.get("email")

    if len(nickname) < 4:
        return "닉네임은 4자 이상이어야 합니다."
    
    if len(password) < 8:
        return "비밀번호는 8자 이상이어야 합니다."

    if User.objects.filter(username=username).exists():
        return "이미 존재하는 이름입니다."
    
    if User.objects.filter(email=email).exists():
        return "이미 존재하는 이메일입니다."