from pydantic import BaseModel

class Interaction(BaseModel):
    from_node: str
    to_node: str