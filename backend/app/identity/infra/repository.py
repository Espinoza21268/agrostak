from sqlalchemy.orm import Session
from typing import Optional, List

from app.identity.infra.models import UsuarioORM, RolORM, AccesoUsuarioORM


class IdentityRepository:
    def __init__(self, db: Session):
        self.db = db

    # Roles
    def get_role(self, id_rol: int) -> Optional[RolORM]:
        return self.db.query(RolORM).filter(RolORM.id_rol == id_rol).first()

    def list_roles(self) -> List[RolORM]:
        return self.db.query(RolORM).all()

    # Usuarios
    def get_user_by_id(self, id_usuario: int) -> Optional[UsuarioORM]:
        return self.db.query(UsuarioORM).filter(UsuarioORM.id_usuario == id_usuario).first()

    def get_user_by_email(self, correo: str) -> Optional[UsuarioORM]:
        return self.db.query(UsuarioORM).filter(UsuarioORM.correo == correo).first()

    def list_users(self) -> List[UsuarioORM]:
        return self.db.query(UsuarioORM).all()

    def create_user(self, user: UsuarioORM) -> UsuarioORM:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user: UsuarioORM) -> UsuarioORM:
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user: UsuarioORM) -> None:
        self.db.delete(user)
        self.db.commit()

    # Accesos
    def log_access(self, id_usuario: int, ip: str | None, user_agent: str | None) -> None:
        self.db.add(AccesoUsuarioORM(id_usuario=id_usuario, ip=ip, user_agent=user_agent))
        self.db.commit()
