from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers import users, journal, analysis
from security.ratelimit import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)

app.include_router(users.router, prefix="/users")
app.include_router(journal.router, prefix="/journal")
app.include_router(analysis.router, prefix='/analysis')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)