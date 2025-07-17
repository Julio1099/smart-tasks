from fastapi import FastAPI
from . import routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SmartTasks API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à SmartTasks API!"} 