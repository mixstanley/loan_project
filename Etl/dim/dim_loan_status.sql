CREATE TABLE dim_loan_status (
    status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL
);

INSERT INTO dim_loan_status (status_name) VALUES
('Repaid'),
('Outstanding');
