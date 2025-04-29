from fastapi import APIRouter
from controllers.users import UserController

router = APIRouter()

router.post("/register")(UserController.register)
router.get("/recomendados")(UserController.recommended)
router.post("/login")(UserController.login)