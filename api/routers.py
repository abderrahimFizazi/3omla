from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from . import schemas, models
from .database import get_db

router = APIRouter()


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
    db_service = models.Service(**service.dict(), created_at=datetime.now(), updated_at=datetime.now())
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


@router.post("/users/{user_id}/user_services", response_model=schemas.User_Service)
def create_user_service_for_user(
    user_id: int, user_service: schemas.User_ServiceCreate, db: Session = Depends(get_db)
):
    db_user_service = models.User_Service(
        **user_service.dict(), user_id=user_id, created_at=datetime.now(), updated_at=datetime.now()
    )
    db.add(db_user_service)
    db.commit()
    db.refresh(db_user_service)
    return db_user_service


@router.get("/users/{user_id}/user_services", response_model=List[schemas.User_Service])
def get_user_services_for_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.User_Service).filter(models.User_Service.user_id == user_id).all()


@router.post("/user_services/{user_service_id}/payments", response_model=schemas.Payment)
def create_payment_for_user_service(
    user_service_id: int, payment: schemas.PaymentCreate, db: Session = Depends(get_db)
):
    db_payment = models.Payment(
        **payment.dict(), user_service_id=user_service_id, created_at=datetime.now(), updated_at=datetime.now()
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


@router.get("/user_services/{user_service_id}/payments", response_model=List[schemas.Payment])
def get_payments_for_user_service(user_service_id: int, db: Session = Depends(get_db)):
    return db.query(models.Payment).filter(models.Payment.user_service_id == user_service_id).all()


@router.post("/user_services/{user_service_id}/notifications", response_model=schemas.Notification)
def create_notification_for_user_service(
    user_service_id: int, notification: schemas.NotificationCreate, db: Session = Depends(get_db)
):
    db_notification = models.Notification(
        **notification.dict(), user_service_id=user_service_id, created_at=datetime.now(), updated_at=datetime.now()
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


@router.get("/user_services/{user_service_id}/notifications", response_model=List[schemas.Notification])
def get_notifications_for_user_service(user_service_id: int, db: Session = Depends(get_db)):
    return db.query(models.Notification).filter(models.Notification.user_service_id == user_service_id).all()


@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for field, value in user.dict(exclude_unset=True).items():
        setattr(db_user, field, value)
    db_user.updated_at = datetime.now()
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user


@router.put("/services/{service_id}", response_model=schemas.Service)
def update_service(service_id: int, service: schemas.ServiceUpdate, db: Session = Depends(get_db)):
    db_service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Service not found")
    for field, value in service.dict(exclude_unset=True).items():
        setattr(db_service, field, value)
    db_service.updated_at = datetime.now()
    db.commit()
    db.refresh(db_service)
    return db_service


@router.delete("/services/{service_id}", response_model=schemas.Service)
def delete_service(service_id: int, db: Session = Depends(get_db)):
    db_service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Service not found")
    db.delete(db_service)
    db.commit()
    return db_service


@router.put("/user_services/{user_service_id}", response_model=schemas.User_Service)
def update_user_service(
    user_service_id: int, user_service: schemas.User_ServiceUpdate, db: Session = Depends(get_db)
):
    db_user_service = db.query(models.User_Service).filter(models.User_Service.id == user_service_id).first()
    if not db_user_service:
        raise HTTPException(status_code=404, detail="User service not found")
    for field, value in user_service.dict(exclude_unset=True).items():
        setattr(db_user_service, field, value)
    db_user_service.updated_at = datetime.now()
    db.commit()
    db.refresh(db_user_service)
    return db_user_service


@router.delete("/user_services/{user_service_id}", response_model=schemas.User_Service)
def delete_user_service(user_service_id: int, db: Session = Depends(get_db)):
    db_user_service = db.query(models.User_Service).filter(models.User_Service.id == user_service_id).first()
    if not db_user_service:
        raise HTTPException(status_code=404, detail="User service not found")
    db.delete(db_user_service)
    db.commit()
    return db_user_service


@router.put("/payments/{payment_id}", response_model=schemas.Payment)
def update_payment(payment_id: int, payment: schemas.PaymentUpdate, db: Session = Depends(get_db)):
    db_payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    for field, value in payment.dict(exclude_unset=True).items():
        setattr(db_payment, field, value)
    db_payment.updated_at = datetime.now()
    db.commit()
    db.refresh(db_payment)
    return db_payment


@router.delete("/payments/{payment_id}", response_model=schemas.Payment)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    db.delete(db_payment)
    db.commit()
    return db_payment


@router.put("/notifications/{notification_id}", response_model=schemas.Notification)
def update_notification(
    notification_id: int, notification: schemas.NotificationUpdate, db: Session = Depends(get_db)
):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    for field, value in notification.dict(exclude_unset=True).items():
        setattr(db_notification, field, value)
    db_notification.updated_at = datetime.now()
    db.commit()
    db.refresh(db_notification)
    return db_notification


@router.delete("/notifications/{notification_id}", response_model=schemas.Notification)
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(db_notification)
    db.commit()
    return db_notification
