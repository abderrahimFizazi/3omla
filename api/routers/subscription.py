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

@router.post("/", response_model=schemas.Subscription)
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

@router.get("/{subscription_id}", response_model=schemas.Subscription)
def get_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = db.query(models.Subscription).filter(models.Subscription.id == subscription_id).first()
    if not db_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription

# Other subscription endpoints...

