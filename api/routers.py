from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db, engine
from typing import List
from datetime import datetime

router = APIRouter()
models.Base.metadata.create_all(bind=engine)

@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict(), created_at=datetime.now(), updated_at=datetime.now())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.post("/services", response_model=schemas.Service)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    db_service = models.Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


@router.get("/services/{service_id}", response_model=schemas.Service)
def get_service(service_id: int, db: Session = Depends(get_db)):
    db_service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service


@router.get("/services", response_model=List[schemas.Service])
def get_services(db: Session = Depends(get_db)):
    return db.query(models.Service).all()



@router.post("/payments", response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    db_payment = models.Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


@router.get("/payments/{payment_id}", response_model=schemas.Payment)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment


@router.get("/payments", response_model=List[schemas.Payment])
def get_payments(db: Session = Depends(get_db)):
    return db.query(models.Payment).all()


@router.post("/notifications", response_model=schemas.Notification)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    db_notification = models.Notification(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


@router.get("/notifications/{notification_id}", response_model=schemas.Notification)
def get_notification(notification_id: int, db: Session = Depends(get_db)):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification


@router.get("/notifications", response_model=List[schemas.Notification])
def get_notifications(db: Session = Depends(get_db)):
    return db.query(models.Notification).all()


