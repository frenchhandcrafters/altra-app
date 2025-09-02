from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from .db import Base


class User(Base):
__tablename__ = "users"
id = Column(Integer, primary_key=True)
aad_object_id = Column(String, index=True, unique=True) # Entra ID Object ID
display_name = Column(String)
email = Column(String, unique=True)
role = Column(String, default="technician") # admin | manager | technician


class Client(Base):
__tablename__ = "clients"
id = Column(Integer, primary_key=True)
name = Column(String, nullable=False)
email = Column(String)
phone = Column(String)
address = Column(String)


class Technician(Base):
__tablename__ = "technicians"
id = Column(Integer, primary_key=True)
user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
calendar_upn = Column(String) # user@domain.com for Graph
user = relationship("User")


class Intervention(Base):
__tablename__ = "interventions"
id = Column(Integer, primary_key=True)
title = Column(String, nullable=False)
description = Column(Text)
client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
technician_id = Column(Integer, ForeignKey("technicians.id"), nullable=False)
start_at = Column(DateTime)
end_at = Column(DateTime)
status = Column(String, default="planned") # planned|en_route|started|finished|canceled
graph_event_id = Column(String)


client = relationship("Client")
technician = relationship("Technician")