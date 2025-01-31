import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    phone_number: so.Mapped[str] = so.mapped_column(sa.String(64), unique=True)