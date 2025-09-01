from fastapi import FastAPI
from controller import home_controller, healthy_controller
from settings.config import settings

app = FastAPI(
    title=settings.API_NAME,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(home_controller.router)
app.include_router(healthy_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.API_PORT)
