from fastapi import Depends, FastAPI, Header, HTTPException

from app.core.database import settings
from app.routes import tasks_router

app = FastAPI(title="Task Manager API")


def verify_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return x_api_key


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(tasks_router, dependencies=[Depends(verify_api_key)])
