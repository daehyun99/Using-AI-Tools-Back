-- USERS 테이블
CREATE TABLE USERS (
    id INT NOT NULL AUTO_INCREMENT COMMENT 'ID (AUTO_INCREMENT)',
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '가입 일시',
    uuid VARCHAR(255) NOT NULL COMMENT '고유 ID',
    email VARCHAR(255) NOT NULL COMMENT '이메일',
    password_hash VARCHAR(255) NOT NULL COMMENT '비밀번호 해시',
    service_enabled BOOLEAN NOT NULL COMMENT '서비스 이용 가능 여부',
    PRIMARY KEY (uuid),
    UNIQUE KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- SURVEY_SUBMISSIONS 테이블
CREATE TABLE SURVEY_SUBMISSIONS (
    id INT NOT NULL AUTO_INCREMENT COMMENT 'ID (AUTO_INCREMENT)',
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '응시 시각',
    uuid VARCHAR(255) NOT NULL COMMENT 'USERS 테이블의 고유 ID (FK)',
    payload JSON NOT NULL COMMENT '설문 데이터',
    PRIMARY KEY (id),
    KEY idx_survey_uuid (uuid),
    CONSTRAINT fk_survey_user FOREIGN KEY (uuid) REFERENCES USERS(uuid) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- SERVICE_USAGE 테이블
CREATE TABLE SERVICE_USAGE (
    id INT NOT NULL AUTO_INCREMENT COMMENT 'ID (AUTO_INCREMENT)',
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '이용 시각',
    uuid VARCHAR(255) NOT NULL COMMENT 'USERS 테이블의 고유 ID (FK)',
    correlation_id VARCHAR(255) NOT NULL COMMENT '요청과 응답을 연계하기 위한 고유 식별자 (Indexed)',
    PRIMARY KEY (id),
    KEY idx_service_uuid (uuid),
    KEY idx_service_correlation_id (correlation_id),
    CONSTRAINT fk_service_user FOREIGN KEY (uuid) REFERENCES USERS(uuid) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- SYSTEM_LOGS 테이블
CREATE TABLE SYSTEM_LOGS (
    id INT NOT NULL AUTO_INCREMENT COMMENT 'ID (AUTO_INCREMENT)',
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '로그가 기록된 시간',
    layer ENUM('PRESENTATION', 'BUSINESS', 'PERSISTENCE', 'DATABASE') NOT NULL COMMENT '로그가 기록된 계층',
    log_type ENUM('REQUEST', 'RESPONSE') NOT NULL COMMENT '요청 또는 응답 구분',
    correlation_id VARCHAR(255) NOT NULL COMMENT '요청과 응답을 연계하기 위한 고유 식별자',
    status VARCHAR(255) DEFAULT NULL COMMENT '응답의 상태 코드 또는 메시지 (nullable)',
    msg VARCHAR(255) DEFAULT NULL COMMENT '로그 메시지 (nullable)',
    error JSON DEFAULT NULL COMMENT '오류 발생 시 에러 정보 (nullable, JSON 형식)',
    data JSON DEFAULT NULL COMMENT '요청 또는 응답 데이터 (nullable, JSON 형식)',
    PRIMARY KEY (id),
    KEY idx_logs_correlation_id (correlation_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
