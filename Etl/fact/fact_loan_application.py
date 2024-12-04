import sys
import os
import asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_util import DBUtils

# 创建 DBUtils 实例
db_utils = DBUtils()

# 执行 INSERT INTO SELECT SQL 查询
insert_sql = """
    INSERT INTO fact_loan_application
    SELECT
        application_id,
        amount,
        application_date,
        issuance_date,
        repaid_amount,
        repaid_date,
        CASE
            WHEN application_status = 'Repaid' THEN 1
            WHEN application_status = 'Outstanding' THEN 2
            ELSE 0
        END,       -- 申请状态
        due_date,
        is_voluntary_repayment,
        application_hour,
        issuance_hour,
        repaid_hour,
        due_hour,
        late_days
    FROM
        ods_loan_application;
"""

# Asynchronously run the query
async def main():
    await db_utils.execute_sql(insert_sql)

# Start the asyncio event loop to run the query
if __name__ == "__main__":
    asyncio.run(main())
