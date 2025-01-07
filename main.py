import logging
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from database import engine
from models import Base
from routers import festivals, rockbands, performances

Base.metadata.create_all(bind=engine)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Incoming request: {request.method} {request.url}")
    try:
        response = await call_next(request)
    except Exception as e:
        logging.exception("Error handling request")
        raise e
    logging.info(f"Response status: {response.status_code}")
    return response

app.include_router(festivals.router)
app.include_router(rockbands.router)
app.include_router(performances.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Rock Festival API"}