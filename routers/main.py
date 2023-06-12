from fastapi import FastAPI
import models
from database import engine
from router import auth, todo, admin, users

app = FastAPI()

#Esto se ejecuta si la bd no existe , la crea cuando se inicia. Si ya tiene datos esto no realiza nada
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(admin.router)
app.include_router(users.router)