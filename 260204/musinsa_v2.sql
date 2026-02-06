USE musinsa_db_v6;

SELECT * FROM musinsa_reviews;

# 전체 리뷰 건수
SELECT COUNT(*)
FROM musinsa_reviews;

# 브랜드별 리뷰 건수
SELECT brand, COUNT(*) AS review_rows
FROM musinsa_reviews
GROUP BY brand
ORDER BY review_rows DESC;

# 브랜드별 평균 평점
SELECT brand, AVG(rating) AS avg_rating, COUNT(*) AS n
FROM musinsa_reviews
WHERE rating IS NOT NULL
GROUP BY brand
HAVING n >= 5
ORDER BY avg_rating DESC;

# 상품ID 기준, 리뷰건수
SELECT product_id, product_name, COUNT(*) AS review_rows
FROM musinsa_reviews
GROUP BY product_id, product_name;

# 상품별 평균 평점
SELECT product_id, product_name,
	AVG(rating) AS avg_rating,
    COUNT(*) AS review_rows
FROM musinsa_reviews
WHERE rating IS NOT NULL
GROUP BY product_id, product_name
HAVING review_rows >= 5
ORDER BY avg_rating DESC;

# 리뷰길이 상위 10개
SELECT
	id, brand,
    product_name,
	CHAR_LENGTH(review_text) AS len_chars
FROM musinsa_reviews
ORDER BY len_chars DESC
LIMIT 10;

# 특정 키워드를 포함하고 있는 리뷰 검색
SELECT
	id, brand,
    product_name,
    rating, review_text
FROM musinsa_reviews
-- WHERE review_text LIKE '%따뜻%'
-- 	OR review_text LIKE "%포근%"
--     OR review_text LIKE "%보온%"
WHERE review_text REGEXP '따뜻|포근|보온'
ORDER BY rating DESC;

# 부정키워드 포함비율
SELECT
	SUM(CASE WHEN review_text REGEXP '작|별로|아쉽|불편|비추' THEN 1 ELSE 0 END) AS neg_like,
    COUNT(*) AS total,
    ROUND(100 * SUM(CASE WHEN review_text REGEXP '작|별로|아쉽|불편|비추' THEN 1 ELSE 0 END)/COUNT(*), 2) AS neg_pct
FROM musinsa_reviews;