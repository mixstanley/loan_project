import sys
import os
import asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_util import DBUtils

# 创建 DBUtils 实例
db_utils = DBUtils()

# 执行 INSERT INTO SELECT SQL 查询
insert_sql = """
WITH repayment_rate AS (
    SELECT
        round(sum(repaid_cnt) / sum(apply_cnt), 4) AS repayment_rate
    FROM dws_loan_process_summary_ds
),
voluntary_repayment_percentage AS (
    SELECT
        round(sum(voluntary_cnt) / sum(repaid_cnt), 4) AS voluntary_repayment_percentage
    FROM dws_loan_process_summary_ds
),
late_repayment_percentage AS (
    SELECT
        round(sum(due_cnt) / sum(apply_cnt), 4) AS late_repayment_percentage
    FROM dws_loan_process_summary_ds
),
loan_counts AS (
    SELECT
        sum(apply_cnt) AS total_cnt,
        sum(repaid_cnt) AS repaid_cnt,
        sum(apply_cnt) - sum(repaid_cnt) AS outgoing_cnt
    FROM dws_loan_process_summary_ds
)
INSERT INTO adm_kpi_report_ds
SELECT
    current_date rpt_date,
    rr.repayment_rate,
    vrp.voluntary_repayment_percentage,
    lrp.late_repayment_percentage,
    lc.total_cnt,
    lc.repaid_cnt,
    lc.outgoing_cnt
FROM
    repayment_rate rr
    FULL OUTER JOIN voluntary_repayment_percentage vrp ON 1 = 1
    FULL OUTER JOIN late_repayment_percentage lrp ON 1 = 1
    FULL OUTER JOIN loan_counts lc ON 1 = 1
;
"""

# Asynchronously run the query
async def main():
    await db_utils.execute_sql(insert_sql)

# Start the asyncio event loop to run the query
if __name__ == "__main__":
    asyncio.run(main())
