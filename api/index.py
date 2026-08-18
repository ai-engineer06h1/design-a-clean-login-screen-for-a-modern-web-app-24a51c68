from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import os
import jwt
import bcrypt

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

class User(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    success: bool
    token: str = None
    message: str = None

# Dummy database of users for demonstration
# In production, replace this with actual database queries
fake_users_db = {
    "user@example.com": {
        "full_name": "John Doe",
        "hashed_password": bcrypt.hashpw(b"password", bcrypt.gensalt()),
    }
}

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

@app.post("/api/login", response_model=LoginResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    # Create JWT token
    token = jwt.encode({"sub": form_data.username}, os.environ["JWT_SECRET"], algorithm="HS256")
    return LoginResponse(success=True, token=token)
