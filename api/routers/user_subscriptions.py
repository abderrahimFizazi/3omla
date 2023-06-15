from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from .. import schemas, models, database

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UserSubscription)
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

@router.get("/{user_subscription_id}", response_model=schemas.UserSubscription)
def get_user_subscription(user_subscription_id: int, db: Session = Depends(get_db)):
    db_user_subscription = db.query(models.UserSubscription).filter(models.UserSubscription.id == user_subscription_id).first()
    if not db_user_subscription:
        raise HTTPException(status_code=404, detail="User Subscription not found")
    return db_user_subscription

# Other user subscription endpoints...

