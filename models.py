# models.py
from typing import List, Optional
from sqlalchemy import create_engine, String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

class Categoria(Base):
    __tablename__ = "categoria"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    produtos: Mapped[List["Produto"]] = relationship(
        back_populates="categoria", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Categoria(id={self.id!r}, nome={self.nome!r})"

class Produto(Base):
    __tablename__ = "produto"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    valor: Mapped[float] = mapped_column(Float, nullable=False)

    categoria_id: Mapped[Optional[int]] = mapped_column(ForeignKey("categoria.id"), nullable=True)
    associacao_tipo: Mapped[Optional[str]] = mapped_column(String(50), default="belongs_to")
    categoria: Mapped[Optional[Categoria]] = relationship(back_populates="produtos")

    def __repr__(self) -> str:
        return (
            f"Produto(id={self.id!r}, nome={self.nome!r}, valor={self.valor!r}, "
            f"categoria_id={self.categoria_id!r}, associacao_tipo={self.associacao_tipo!r})"
        )

DATABASE_URL = "sqlite:///banco_orm.db"
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, future=True)

Base.metadata.create_all(engine)
