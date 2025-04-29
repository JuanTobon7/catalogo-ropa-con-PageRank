from fastapi import Request, HTTPException
from models.interaction import Interaction as InteractionModel
from services.interaction import Interaction as InteractionService
from typing import Optional
import json

class Interaction:
    @staticmethod
    async def interact(request: Request, interaction: InteractionModel, email: Optional[str] = None):
        try:
            # 1. Intentar obtener y parsear la cookie
            user_email = None
            cookie_str = request.cookies.get("user")

            if cookie_str:
                try:
                    user_data = json.loads(cookie_str)
                    user_email = user_data.get("email")
                except json.JSONDecodeError:
                    raise HTTPException(status_code=400, detail="Cookie mal formada")

            # 2. Si no hay cookie válida, usar parámetro de fallback
            if not user_email:
                user_email = email

            # 3. Si no hay ninguna fuente válida, error
            if not user_email:
                raise HTTPException(status_code=400, detail="Usuario no autenticado")

            # 4. Llamar al servicio
            result = await InteractionService.interact(user_email, interaction)
            return result

        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
