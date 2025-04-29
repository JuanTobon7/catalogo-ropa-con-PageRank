from fastapi import Request, HTTPException,Response
from models.user import User as UserModel
from models.user import  UserLogin as UserModelLogin
from services.users import UserService
from typing import Optional
import json

class UserController:

    @staticmethod
    async def register(request: Request, user: UserModel):
        try:
            saved = UserService.save_user(user)
            return {"msg": "Usuario registrado", "data": saved}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    @staticmethod
    async def login(request: Request,user: UserModelLogin, response: Response):
        try:
            result = UserService.login(user)
            print('result seteo before',result)
            response.set_cookie(
                key="user",
                value=json.dumps(result),
                httponly=False,
                secure=False,
                samesite="lax",
                path="/"
            )

            return {"email":user.email}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))    
    
    @staticmethod
    async def recommended(request: Request, email: Optional[str] = None):
        try:
            user_cookie = request.cookies.get('user')
            print('user cookie:', user_cookie)

            user_email = None

            if user_cookie:
                try:
                    email_data = json.loads(user_cookie)
                    user_email = email_data.get("email")
                except json.JSONDecodeError:
                    raise HTTPException(status_code=400, detail="Cookie mal formada")

            if not user_email:
                user_email = email

            if not user_email:
                raise HTTPException(status_code=400, detail="No se pudo determinar el email del usuario")

            result = await UserService.recommended(user_email)
            return result
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))