from sqlalchemy import Column, Integer, String, Enum, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    address = Column(String(255))
    id_card_number = Column(String(20))
    photo_url = Column(String(255))
    user_type = Column(Enum('admin', 'user', 'partner'), nullable=False)
    score = Column(Integer, default=0)
    registration_date = Column(DateTime, nullable=False)
    last_login = Column(DateTime)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    services = relationship('User_Service', back_populates='user')


class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String)
    cost = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    users = relationship('User_Service', back_populates='service')


class User_Service(Base):
    __tablename__ = 'user_services'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(Enum('paid', 'pending', 'late'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    user = relationship('User', back_populates='services')
    service = relationship('Service', back_populates='users')
    payments = relationship('Payment', back_populates='user_service')
    notifications = relationship('Notification', back_populates='user_service')


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    user_service_id = Column(Integer, ForeignKey('user_services.id'))
    payment_date = Column(Date, nullable=False)
    payment_method = Column(Enum('credit_card', 'paypal', 'bank_transfer', 'partner'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    user_service = relationship('User_Service', back_populates='payments')


class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_service_id = Column(Integer, ForeignKey('user_services.id'))
    message = Column(String, nullable=False)
    notification_date = Column(DateTime, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    user_service = relationship('User_Service', back_populates='notifications')
