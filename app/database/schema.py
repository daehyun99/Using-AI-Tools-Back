
from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    DateTime,
    func,
    Enum,
    Boolean,
    ForeignKey,
)


from app.database.conn import Base, db

class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False, default=func.utc_timestamp())


class temps(Base, BaseMixin):
    __tablename__ = "temps" # logs
    log_type = Column(Enum("request", "response"), nullable=False)
    correlation_id = Column(String, nullable=False, index=True)
    status = Column(String, nullable=True)
    msg = Column(String, nullable=True)
    error = Column(JSON, nullable=True)
    data = Column(JSON, nullable=True) # request -> metadata, response -> data
