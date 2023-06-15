from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from . import schemas, models, database

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(
        nom=user.nom,
        email=user.email,
        adresse=user.adresse,
        type_utilisateur=user.type_utilisateur,
        score=0,
        date_inscription=datetime.now(),
        derniere_connexion=datetime.now()
    )
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

@router.post("/subscriptions", response_model=schemas.Subscription)
def create_subscription(subscription: schemas.SubscriptionCreate, db: Session = Depends(get_db)):
    db_subscription = models.Subscription(
        utilisateur_id=subscription.utilisateur_id,
        date_debut=subscription.date_debut,
        date_fin=subscription.date_fin
    )
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

@router.get("/subscriptions/{subscription_id}", response_model=schemas.Subscription)
def get_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = db.query(models.Subscription).filter(models.Subscription.id == subscription_id).first()
    if not db_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription

@router.post("/services", response_model=schemas.Service)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    db_service = models.Service(
        nom=service.nom,
        description=service.description,
        cout=service.cout
    )
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

@router.post("/user-subscriptions", response_model=schemas.UserSubscription)
def create_user_subscription(user_subscription: schemas.UserSubscriptionCreate, db: Session = Depends(get_db)):
    db_user_subscription = models.UserSubscription(
        utilisateur_id=user_subscription.utilisateur_id,
        service_id=user_subscription.service_id,
        abonnement_id=user_subscription.abonnement_id,
        date_debut=user_subscription.date_debut,
        date_fin=user_subscription.date_fin
    )
    db.add(db_user_subscription)
    db.commit()
    db.refresh(db_user_subscription)
    return db_user_subscription

@router.get("/user-subscriptions/{user_subscription_id}", response_model=schemas.UserSubscription)
def get_user_subscription(user_subscription_id: int, db: Session = Depends(get_db)):
    db_user_subscription = db.query(models.UserSubscription).filter(models.UserSubscription.id == user_subscription_id).first()
    if not db_user_subscription:
        raise HTTPException(status_code=404, detail="User Subscription not found")
    return db_user_subscription

@router.post("/payment-statuses", response_model=schemas.PaymentStatus)
def create_payment_status(payment_status: schemas.PaymentStatusCreate, db: Session = Depends(get_db)):
    db_payment_status = models.PaymentStatus(
        utilisateur_id=payment_status.utilisateur_id,
        statut=payment_status.statut,
        date_paiement=payment_status.date_paiement,
        methode_paiement=payment_status.methode_paiement
    )
    db.add(db_payment_status)
    db.commit()
    db.refresh(db_payment_status)
    return db_payment_status

@router.get("/payment-statuses/{payment_status_id}", response_model=schemas.PaymentStatus)
def get_payment_status(payment_status_id: int, db: Session = Depends(get_db)):
    db_payment_status = db.query(models.PaymentStatus).filter(models.PaymentStatus.id == payment_status_id).first()
    if not db_payment_status:
        raise HTTPException(status_code=404, detail="Payment Status not found")
    return db_payment_status

@router.post("/notifications", response_model=schemas.Notification)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    db_notification = models.Notification(
        utilisateur_id=notification.utilisateur_id,
        message=notification.message,
        date_notification=datetime.now(),
        lu=False
    )
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

# Other endpoints...
