from fastapi import FastAPI, CORSMiddleware
import uvicorn
from routers import users
from routers import journal
from routers import analysis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(journal.router)
app.include_router(analysis.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)