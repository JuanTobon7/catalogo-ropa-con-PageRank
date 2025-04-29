import json
from pathlib import Path
from models.user import User
from models.user import UserLogin
from services.user_pref_service import UserPrefService
from core.graph import G

USERS_PATH = Path('database/users.json')

class UserService:

    @staticmethod
    def load_users():
        if not USERS_PATH.exists():
            return []

        try:
            with open(USERS_PATH, 'r') as f:
                content = f.read().strip()
                return json.loads(content) if content else []
        except json.JSONDecodeError:
            # Puedes loggear aquí si quieres debuggear, o incluso limpiar el archivo
            return []

    @staticmethod
    def login(user: UserLogin):
        try:
            bankUser = UserService.load_users()
            for i in bankUser:
                if i["email"] == user.email and i["password"] == user.password:
                    email = user.email
                    return {"email":email}
            return ValueError("No se encontro ningun usuario asi manito")
        except ValueError as e:
            return e

    @staticmethod
    def save_user(user: User):
        users = UserService.load_users()

        # Evitar duplicados (por ejemplo por email)
        if any(u["email"] == user.email for u in users):
            raise ValueError("Ya existe un usuario con ese email")

        users.append(user.dict())

        with open(USERS_PATH, 'w') as f:
            json.dump(users, f, indent=2)

        return user
    @staticmethod
    async def recommended(id_email:str):
        prefs = UserPrefService.get_prefs(id_email)
        result = await G.get_recommendations(prefs=prefs,id_email=id_email)
        return result
    
