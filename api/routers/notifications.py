from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import schemas, models, database

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Notification)
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

@router.get("/{notification_id}", response_model=schemas.Notification)
def get_notification(notification_id: int, db: Session = Depends(get_db)):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification

# Other notification endpoints...

