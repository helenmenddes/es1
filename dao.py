# dao.py
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional, Type, Any, Dict
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete

from models import SessionLocal, Produto, Categoria

T = TypeVar("T")

class DAO(ABC, Generic[T]):
    """Interface básica para DAOs."""
    model: Type[T]

    def __init__(self, model: Type[T]):
        self.model = model

    @abstractmethod
    def create(self, obj: T) -> T:
        ...

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        ...

    @abstractmethod
    def list_all(self) -> List[T]:
        ...

    @abstractmethod
    def update(self, id: int, fields: Dict[str, Any]) -> Optional[T]:
        ...

    @abstractmethod
    def delete(self, id: int) -> bool:
        ...

class ProdutoDAO(DAO[Produto]):
    def __init__(self):
        super().__init__(Produto)

    def create(self, produto: Produto) -> Produto:
        with SessionLocal() as session:
            session.add(produto)
            session.commit()
            session.refresh(produto)
            return produto

    def get_by_id(self, id: int) -> Optional[Produto]:
        with SessionLocal() as session:
            stmt = select(Produto).where(Produto.id == id)
            return session.scalar(stmt)

    def list_all(self) -> List[Produto]:
        with SessionLocal() as session:
            stmt = select(Produto)
            return list(session.scalars(stmt))

    def update(self, id: int, fields: Dict[str, Any]) -> Optional[Produto]:
        with SessionLocal() as session:
            stmt = select(Produto).where(Produto.id == id)
            obj = session.scalar(stmt)
            if obj is None:
                return None
            for k, v in fields.items():
                setattr(obj, k, v)
            session.commit()
            session.refresh(obj)
            return obj

    def delete(self, id: int) -> bool:
        with SessionLocal() as session:
            stmt = select(Produto).where(Produto.id == id)
            obj = session.scalar(stmt)
            if obj is None:
                return False
            session.delete(obj)
            session.commit()
            return True

class CategoriaDAO(DAO[Categoria]):
    def __init__(self):
        super().__init__(Categoria)

    def create(self, categoria: Categoria) -> Categoria:
        with SessionLocal() as session:
            session.add(categoria)
            session.commit()
            session.refresh(categoria)
            return categoria

    def get_by_id(self, id: int) -> Optional[Categoria]:
        with SessionLocal() as session:
            stmt = select(Categoria).where(Categoria.id == id)
            return session.scalar(stmt)

    def list_all(self) -> List[Categoria]:
        with SessionLocal() as session:
            stmt = select(Categoria)
            return list(session.scalars(stmt))

    def update(self, id: int, fields: Dict[str, Any]) -> Optional[Categoria]:
        with SessionLocal() as session:
            stmt = select(Categoria).where(Categoria.id == id)
            obj = session.scalar(stmt)
            if obj is None:
                return None
            for k, v in fields.items():
                setattr(obj, k, v)
            session.commit()
            session.refresh(obj)
            return obj

    def delete(self, id: int) -> bool:
        with SessionLocal() as session:
            stmt = select(Categoria).where(Categoria.id == id)
            obj = session.scalar(stmt)
            if obj is None:
                return False
            session.delete(obj)
            session.commit()
            return True
