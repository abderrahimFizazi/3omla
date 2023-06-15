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

@router.post("/", response_model=schemas.PaymentStatus)
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

@router.get("/{payment_status_id}", response_model=schemas.PaymentStatus)
def get_payment_status(payment_status_id: int, db: Session = Depends(get_db)):
    db_payment_status = db.query(models.PaymentStatus).filter(models.PaymentStatus.id == payment_status_id).first()
    if not db_payment_status:
        raise HTTPException(status_code=404, detail="Payment Status not found")
    return db_payment_status

# Other payment status endpoints...

