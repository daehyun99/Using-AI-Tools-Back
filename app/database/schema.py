
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
from sqlalchemy.orm import relationship

from app.database.conn import Base

class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False, default=func.utc_timestamp())

# USERS 테이블
class USERS(Base, BaseMixin):
    __tablename__ = "USERS"
    
    uuid = Column(String(255), unique=True, nullable=False, index=True, comment="고유 ID")
    email = Column(String(255), nullable=False, comment="이메일")
    password_hash = Column(String(255), nullable=False, comment="비밀번호 해시")
    service_enabled = Column(Boolean, nullable=False, comment="서비스 이용 가능 여부")
    created_at = Column(DateTime, nullable=False, default=func.now(), comment="가입 일시")

    survey_submissions = relationship("SURVEY_SUBMISSIONS", back_populates="user", cascade="all, delete-orphan")
    service_usages = relationship("SERVICE_USAGE", back_populates="user", cascade="all, delete-orphan")

# SURVEY_SUBMISSIONS 테이블
class SURVEY_SUBMISSIONS(Base, BaseMixin):
    __tablename__ = "SURVEY_SUBMISSIONS"
    
    uuid = Column(String(255), ForeignKey("USERS.uuid", ondelete="CASCADE"), nullable=False, index=True, comment="USERS 테이블의 고유 ID (FK)")
    submitted_at = Column(DateTime, nullable=False, comment="응시 시각")
    payload = Column(JSON, nullable=False, comment="설문 데이터")

    user = relationship("USERS", back_populates="survey_submissions")

# SERVICE_USAGE 테이블
class SERVICE_USAGE(Base, BaseMixin):
    __tablename__ = "SERVICE_USAGE"
    
    uuid = Column(String(255), ForeignKey("USERS.uuid", ondelete="CASCADE"), nullable=False, index=True, comment="USERS 테이블의 고유 ID (FK)")
    correlation_id = Column(String(255), nullable=False, unique=True, index=True, comment="요청과 응답을 연계하기 위한 고유 식별자")
    # correlation_id = Column(String, nullable=False, index=True)
    used_at = Column(DateTime, nullable=False, comment="이용 시각")

    user = relationship("USERS", back_populates="service_usages")
    system_logs = relationship("SYSTEM_LOGS", back_populates="service_usage", cascade="all, delete-orphan")

# SYSTEM_LOGS 테이블
class SYSTEM_LOGS(Base, BaseMixin):
    __tablename__ = "SYSTEM_LOGS"

    layer = Column(Enum("PRESENTATION", "BUSINESS", "PERSISTENCE", "DATABASE"), nullable=False, comment="로그가 기록된 계층")
    log_type = Column(Enum("REQUEST", "RESPONSE"), nullable=False, comment="요청 또는 응답 구분")
    correlation_id = Column(String(255), ForeignKey("SERVICE_USAGE.correlation_id", ondelete="CASCADE"), nullable=False, index=True, comment="SERVICE_USAGE 테이블의 correlation_id (FK)")
    # correlation_id = Column(String, nullable=False, index=True)
    status = Column(String(255), nullable=True, comment="응답의 상태 코드 또는 메시지 (nullable)")
    msg = Column(String(255), nullable=True, comment="로그 메시지 (nullable)")
    error = Column(JSON, nullable=True, comment="오류 발생 시 에러 정보 (nullable, JSON 형식)")
    data = Column(JSON, nullable=True, comment="요청 또는 응답 데이터 (nullable, JSON 형식)")

    service_usage = relationship("SERVICE_USAGE", back_populates="system_logs")