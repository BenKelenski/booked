from fastapi import FastAPI

from .routers import books, users


app = FastAPI()

app.include_router(users.router)
app.include_router(books.router)

@app.get("/health")
async def health_check() -> list[str, str]:
    return {"status": "ok"}