from pydantic import BaseModel

class PassphraseRequest(BaseModel):
    num: int = 5
    delimiter: str = ' '
    specials: int = 0
    caps: bool = True