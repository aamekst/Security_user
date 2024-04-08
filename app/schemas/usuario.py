import re
from pydantic import BaseModel
from datetime import datetime
from pydantic import validator

class Usuarios(BaseModel):
    username: str
    password: str
    
    @validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$', value):
            raise ValueError('Invalid username')
        return value

class UsuariosRequest(Usuarios):
    username: str
    password: str

class TokenData(BaseModel):
    access_token: str
    expires_at: datetime

class UsuariosResponse(Usuarios):
    id: int
    username: str
    password: str
    
    class Config:
        from_attributes=True    
        orm_mode = True
