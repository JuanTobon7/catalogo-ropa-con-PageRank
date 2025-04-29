from fastapi import APIRouter
from controllers.interaction import Interaction

router = APIRouter()

router.post("/interaction")(Interaction.interact)
