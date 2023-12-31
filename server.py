from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from routers import series, users

app = FastAPI()

#CORS
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas Series
app.include_router(series.router)

# Rotas Users
app.include_router(users.router)

if __name__ == "__main__":
    run(app, port=8000)