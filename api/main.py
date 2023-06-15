from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, subscription, service, user_subscription, payment_status, notification

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(subscription.router)
app.include_router(service.router)
app.include_router(user_subscription.router)
app.include_router(payment_status.router)
app.include_router(notification.router)
