import uvicorn
from fastapi import FastAPI
from app.api import router
from app.database import engine
from app.models import Base

app = FastAPI(title="Enterprise Knowledge Base")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)