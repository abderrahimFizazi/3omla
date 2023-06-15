from sqlalchemy import Column, Integer, String, Enum, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum

Base = declarative_base()


class UserType(str, PyEnum):
    admin = 'admin'
    utilisateur = 'utilisateur'
    partenaire = 'partenaire'


class PaymentStatus(str, PyEnum):
    payé = 'payé'
    en_attente = 'en attente'
    en_retard = 'en retard'


class PaymentMethod(str, PyEnum):
    carte_credit = 'carte_credit'
    paypal = 'paypal'
    virement_bancaire = 'virement_bancaire'


class Utilisateur(Base):
    __tablename__ = 'utilisateur'

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String)
    adresse = Column(String)
    type_utilisateur = Column(Enum(UserType, native_enum=False), nullable=False)
    score = Column(Integer)
    date_inscription = Column(DateTime)
    derniere_connexion = Column(DateTime)

    abonnements = relationship("Abonnement", back_populates="utilisateur")
    services = relationship("Utilisateur_Service", back_populates="utilisateur")
    paiements = relationship("Statut_Paiement", back_populates="utilisateur")
    notifications = relationship("Notification", back_populates="utilisateur")


class Abonnement(Base):
    __tablename__ = 'abonnement'

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateur.id'))
    date_debut = Column(Date)
    date_fin = Column(Date)

    utilisateur = relationship("Utilisateur", back_populates="abonnements")


class Service(Base):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    description = Column(String)
    cout = Column(Integer)

    utilisateurs = relationship("Utilisateur_Service", back_populates="service")


class Utilisateur_Service(Base):
    __tablename__ = 'utilisateur_service'

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateur.id'))
    service_id = Column(Integer, ForeignKey('service.id'))
    abonnement_id = Column(Integer, ForeignKey('abonnement.id'))
    date_debut = Column(Date)
    date_fin = Column(Date)

    utilisateur = relationship("Utilisateur", back_populates="services")
    service = relationship("Service", back_populates="utilisateurs")
    abonnement = relationship("Abonnement")


class Statut_Paiement(Base):
    __tablename__ = 'statut_paiement'

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateur.id'))
    statut = Column(Enum(PaymentStatus, native_enum=False))
    date_paiement = Column(Date)
    methode_paiement = Column(Enum(PaymentMethod, native_enum=False))

    utilisateur = relationship("Utilisateur", back_populates="paiements")


class Notification(Base):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateur.id'))
    message = Column(String)
    date_notification = Column(DateTime)
    lu = Column(Boolean)

    utilisateur = relationship("Utilisateur", back_populates="notifications")
