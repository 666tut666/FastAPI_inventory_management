from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class MailProvider(Base):
    __tablename__ = 'mail_provider'

    id = Column(Integer, primary_key=True)
    service_provider = Column(String(250), nullable=False)

    imap_server = Column(String(250))
    imap_server_port = Column(Integer)
    imap_server_ssl = Column(String(250))
    imap_server_port_ssl = Column(Integer)
    imap_server_use_tls = Column(Boolean)

    smtp_server = Column(String(250))
    smtp_server_port = Column(Integer)
    smtp_server_ssl = Column(String(250))
    smtp_server_port_ssl = Column(Integer)
    smtp_server_use_tls = Column(Boolean)

    accounts = relationship("MailAccount", back_populates="provider")

class MailAccount(Base):
    __tablename__ = "mail_account"

    id = Column(Integer, primary_key=True)
    email_address = Column(String(250), nullable=False)
    imap_username = Column(String(250), nullable=False)
    imap_password = Column(String(250), nullable=False)
    smtp_username = Column(String(250), nullable=False)
    smtp_password = Column(String(250), nullable=False)
    provider_id = Column(Integer, ForeignKey('mail_provider.id'), nullable=False)
    provider = relationship("MailProvider", back_populates="accounts")
    account_owner = Column(String(250), nullable=False)
    mails_sent = relationship("SentMail", back_populates="sent_from", order_by="SentMail.time_sent")

class SentMail(Base):
    __tablename__ = "sent_mail"

    id = Column(Integer, primary_key=True)
    mail_uuid = Column(String(36), nullable=False)
    time_sent = Column(DateTime(timezone=True), nullable=False)
    sent_from_id = Column(Integer, ForeignKey('mail_account.id'), nullable=False)
    sent_from = relationship("MailAccount", back_populates="mails_sent")
    sent_to = Column(String(250), nullable=False)
    msg_subject = Column(String(250))
    msg_body = Column(String)
    send_status = Column(String(500))
    received_mails = relationship("ReceivedMail", back_populates="sent_mail", order_by="ReceivedMail.time_received")

class ReceivedMail(Base):
    __tablename__ = "received_mail"

    id = Column(Integer, primary_key=True)
    sent_mail_id = Column(Integer, ForeignKey('sent_mail.id'), nullable=False)
    sent_mail = relationship("SentMail", back_populates="received_mails")
    time_received = Column(DateTime(timezone=True), nullable=False)

Base.metadata.create_all(engine)
session = Session()
gmail = MailProvider(service_provider="gmail.com")

session.add(gmail)
session.commit()