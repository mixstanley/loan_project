CREATE TABLE dim_date (
    full_date DATE NOT NULL  PRIMARY KEY,
    year INT NOT NULL,
    month INT NOT NULL,
    day INT NOT NULL,
    quarter INT NOT NULL,
    day_of_week INT NOT NULL,
    week_of_year INT NOT NULL,
    is_weekend BOOLEAN NOT NULL
);



WITH RECURSIVE date_sequence AS (
    SELECT DATE '2020-01-01' AS full_date
    UNION ALL
    SELECT (full_date + INTERVAL '1 day')::DATE
    FROM date_sequence
    WHERE full_date < DATE '2030-12-31'
)
INSERT INTO dim_date (full_date, year, month, day, quarter, day_of_week, week_of_year, is_weekend)
SELECT
    full_date,
    EXTRACT(YEAR FROM full_date)::INT AS year,
    EXTRACT(MONTH FROM full_date)::INT AS month,
    EXTRACT(DAY FROM full_date)::INT AS day,
    EXTRACT(QUARTER FROM full_date)::INT AS quarter,
    EXTRACT(DOW FROM full_date)::INT AS day_of_week,
    EXTRACT(WEEK FROM full_date)::INT AS week_of_year,
    CASE WHEN EXTRACT(DOW FROM full_date)::INT IN (0, 6) THEN TRUE ELSE FALSE END AS is_weekend
FROM date_sequence;
