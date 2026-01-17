from sqlalchemy.orm import Session
from typing import List, Optional

from app.tasks.infra.models import (
    TareaORM, AsignacionTareaORM, HistorialEstadoTareaORM, ComentarioTareaORM
)
from app.tasks.domain.enums import EstadoTarea


class TasksRepository:
    def __init__(self, db: Session):
        self.db = db

    # ----- TAREAS -----
    def list_tareas(self) -> List[TareaORM]:
        return self.db.query(TareaORM).all()

    def get_tarea(self, id_tarea: int) -> Optional[TareaORM]:
        return self.db.query(TareaORM).filter(TareaORM.id_tarea == id_tarea).first()

    def create_tarea(self, tarea: TareaORM) -> TareaORM:
        self.db.add(tarea)
        self.db.commit()
        self.db.refresh(tarea)
        return tarea

    def update_tarea(self, tarea: TareaORM) -> TareaORM:
        self.db.commit()
        self.db.refresh(tarea)
        return tarea

    def delete_tarea(self, tarea: TareaORM) -> None:
        self.db.delete(tarea)
        self.db.commit()

    # ----- ASIGNACIONES -----
    def add_asignacion(self, asignacion: AsignacionTareaORM) -> AsignacionTareaORM:
        self.db.add(asignacion)
        self.db.commit()
        self.db.refresh(asignacion)
        return asignacion

    def list_asignaciones(self, id_tarea: int) -> List[AsignacionTareaORM]:
        return self.db.query(AsignacionTareaORM).filter(AsignacionTareaORM.id_tarea == id_tarea).all()

    # ----- HISTORIAL -----
    def add_historial(self, hist: HistorialEstadoTareaORM) -> None:
        self.db.add(hist)
        self.db.commit()

    # ----- COMENTARIOS -----
    def add_comentario(self, comentario: ComentarioTareaORM) -> ComentarioTareaORM:
        self.db.add(comentario)
        self.db.commit()
        self.db.refresh(comentario)
        return comentario

    def list_comentarios(self, id_tarea: int) -> List[ComentarioTareaORM]:
        return self.db.query(ComentarioTareaORM).filter(ComentarioTareaORM.id_tarea == id_tarea).all()
