from fastapi import FastAPI
from app.routes import health
from app.utils.logger import logger


app = FastAPI(
    title="FastAPI",
    description="FastAPI application with health check endpoint",
    version="0.1.0",
)

# Register routes
app.include_router(health.router)




# Root endpoint
@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")   
    return {"message": "Welcome to Python FastAPI 🚀"}
