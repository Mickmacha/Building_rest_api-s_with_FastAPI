from fastapi import FastAPI
from uuid import uuid4, UUID
import asyncio
from typing import Optional, List
from models import Role, Gender, User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        name="Michelle",
        email="Mchelle123@gmail.com",
        gender=Gender.female,
        role=[Role.student]
    ),
    User(
        id=uuid4(),
        name="Mitch",
        email="Mitch123@gmail.com",
        gender=Gender.male,
        role= [Role.admin, Role.moderator]  # Wrap the values in a list
    )
]


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.get('/users')
def fetch_users():
    return db

@app.post('/users')
def create_user(user: User):
    db.append(user)
    return {'id': user.id}

@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
    return 