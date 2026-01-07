from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.shared.base_model import Base


class RolORM(Base):
    __tablename__ = "roles"
    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    descripcion = Column(String(200), nullable=True)

    usuarios = relationship("UsuarioORM", back_populates="rol")


class UsuarioORM(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)

    id_rol = Column(Integer, ForeignKey("roles.id_rol"), nullable=False)

    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(120), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)

    area_trabajo = Column(String(100), nullable=True)
    foto_url = Column(String(255), nullable=True)

    estado = Column(Enum("activo", "inactivo"), nullable=False, default="activo")
    fecha_creacion = Column(DateTime, nullable=False, server_default=func.now())
    ultimo_acceso = Column(DateTime, nullable=True)

    rol = relationship("RolORM", back_populates="usuarios")
    accesos = relationship("AccesoUsuarioORM", back_populates="usuario")


class AccesoUsuarioORM(Base):
    __tablename__ = "accesos_usuarios"
    id_acceso = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)

    fecha_login = Column(DateTime, nullable=False, server_default=func.now())
    ip = Column(String(45), nullable=True)
    user_agent = Column(String(255), nullable=True)

    usuario = relationship("UsuarioORM", back_populates="accesos")
