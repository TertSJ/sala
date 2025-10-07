from fastapi import FastAPI
from util.database import init_db
from controllers.controller_pessoa import router as pessoas_router
from controllers.controller_endereco import router as endereco_router

app = FastAPI(title="FastAPI + SQLModel - MVC + Repository")

init_db()

app.include_router(pessoas_router)
app.include_router(endereco_router)

@app.get("/")
def health():
    return {"status": "ok"}