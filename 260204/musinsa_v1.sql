# 현재 만들어져있는 데이터베이스 조회
SHOW DATABASES;

# 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS musinsa_db_v6;

CREATE DATABASE IF NOT EXISTS musinsa_db_v6
	DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_0900_ai_ci;

# 생성된 데이터베이스를 선택
USE musinsa_db_v6;

# 생성된 데이터베이스를 삭제
DROP DATABASE musinsa_db_v6;

# 생성된 데이터베이스 안에 테이블 생성
CREATE TABLE IF NOT EXISTS musinsa_reviews (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    brand VARCHAR(100) NOT NULL,
    product_name VARCHAR(300) NOT NULL,
    product_id BIGINT UNSIGNED NULL,
    url VARCHAR(500) NOT NULL,
    review_count INT NULL,
    rating DECIMAL(3,2) NULL,
    review_text TEXT NOT NULL,
    review_hash CHAR(40) NOT NULL,
    source_file VARCHAR(255) NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_brand (brand),
    KEY idx_product_id (product_id),
    KEY idx_rating (rating),
    UNIQUE KEY uq_review_hash (review_hash)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

# 테이블 조회
SHOW TABLES;

# 실제 테이블 안에 있는 데이터를 조회
SELECT * FROM musinsa_reviews;