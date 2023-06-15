from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    nom: str
    email: str
    adresse: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    score: int
    date_inscription: date
    derniere_connexion: date

    class Config:
        orm_mode = True


class SubscriptionBase(BaseModel):
    utilisateur_id: int
    date_debut: date
    date_fin: date


class SubscriptionCreate(SubscriptionBase):
    pass


class Subscription(SubscriptionBase):
    id: int

    class Config:
        orm_mode = True


class ServiceBase(BaseModel):
    nom: str
    description: str
    cout: int


class ServiceCreate(ServiceBase):
    pass


class Service(ServiceBase):
    id: int

    class Config:
        orm_mode = True


class UserSubscriptionBase(BaseModel):
    utilisateur_id: int
    service_id: int
    abonnement_id: int
    date_debut: date
    date_fin: date


class UserSubscriptionCreate(UserSubscriptionBase):
    pass


class UserSubscription(UserSubscriptionBase):
    id: int

    class Config:
        orm_mode = True


class PaymentStatusBase(BaseModel):
    utilisateur_id: int
    statut: str
    date_paiement: date
    methode_paiement: str


class PaymentStatusCreate(PaymentStatusBase):
    pass


class PaymentStatus(PaymentStatusBase):
    id: int

    class Config:
        orm_mode = True


class NotificationBase(BaseModel):
    utilisateur_id: int
    message: str
    date_notification: date
    lu: bool


class NotificationCreate(NotificationBase):
    pass


class Notification(NotificationBase):
    id: int

    class Config:
        orm_mode = True
