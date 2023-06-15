from enum import Enum
from datetime import datetime, date
from pydantic import BaseModel
from typing import List


class UserType(str, Enum):
    admin = "admin"
    user = "user"
    partner = "partner"


class PaymentMethod(str, Enum):
    credit_card = "credit_card"
    paypal = "paypal"
    bank_transfer = "bank_transfer"
    partner = "partner"


class UserBase(BaseModel):
    name: str
    email: str
    address: str = None
    id_card_number: str = None
    photo_url: str = None
    user_type: UserType
    score: int = 0
    registration_date: datetime
    last_login: datetime = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ServiceBase(BaseModel):
    name: str
    description: str = None
    cost: float
    created_at: datetime
    updated_at: datetime


class ServiceCreate(ServiceBase):
    pass


class Service(ServiceBase):
    id: int

    class Config:
        orm_mode = True


class User_ServiceBase(BaseModel):
    user_id: int
    service_id: int
    start_date: date
    end_date: date
    status: str
    created_at: datetime
    updated_at: datetime


class User_ServiceCreate(User_ServiceBase):
    pass


class User_Service(User_ServiceBase):
    id: int

    class Config:
        orm_mode = True


class PaymentBase(BaseModel):
    user_service_id: int
    payment_date: date
    payment_method: PaymentMethod
    created_at: datetime
    updated_at: datetime


class PaymentCreate(PaymentBase):
    pass


class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True


class NotificationBase(BaseModel):
    user_service_id: int
    message: str
    notification_date: datetime
    is_read: bool = False
    created_at: datetime
    updated_at: datetime


class NotificationCreate(NotificationBase):
    pass


class Notification(NotificationBase):
    id: int

    class Config:
        orm_mode = True


class UserWithServices(User):
    services: List[User_Service]

    class Config:
        orm_mode = True


class ServiceWithUsers(Service):
    users: List[User_Service]

    class Config:
        orm_mode = True
