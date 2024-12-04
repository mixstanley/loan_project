import sys
import os
import asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_util import DBUtils

# 创建 DBUtils 实例
db_utils = DBUtils()

# 执行 INSERT INTO SELECT SQL 查询
insert_sql = """
with date_tab as (
 select full_date
 from dim_date
 where full_date between '2024-01-01' and current_date
), fact_tab as (
    select *
    from fact_loan_application 
), app_tab as (
    select 
        application_date as rpt_date
        ,sum(amount) as apply_amount
        ,count(1) as apply_cnt
        ,sum(case when is_voluntary_repayment = true then amount end) as  voluntary_amount 
        ,count(case when is_voluntary_repayment = true  then 1  end)  as voluntary_cnt 
    from fact_tab
    group by application_date
), issu_tab as (
    select 
        issuance_date as rpt_date
        ,sum(amount) as issue_amount
        ,count(1) as issue_cnt
    from fact_tab
    group by issuance_date
), repaid_tab as (
    select 
        repaid_date as rpt_date
        ,sum(case when application_status = '1' then repaid_amount end) as repaid_amount
        ,count(case when application_status = '1'  then 1  end) as repaid_cnt
    from fact_tab
    group by repaid_date
), due_tab as (
    select 
        due_date as rpt_date
        ,sum(case when late_days > 0   then amount end) as due_amount
        ,count(case when late_days > 0   then 1  end) as due_cnt
    from fact_tab
    group by due_date
),join_tab as (
     select 
    d.full_date as rpt_date,

    app_tab.apply_amount as apply_amount ,
    app_tab.apply_cnt  as apply_cnt , 

    issue_amount as  issue_amount ,
    issue_cnt  as issue_cnt,

    repaid_amount as  repaid_amount ,
    repaid_cnt  as repaid_cnt ,  

    due_amount as  due_amount ,
    due_cnt  as due_cnt ,    

    voluntary_amount as  voluntary_amount ,
    voluntary_cnt  as voluntary_cnt  
 from date_tab d 
 left join  app_tab
 on d.full_date = app_tab.rpt_date
left join issu_tab
 on d.full_date = issu_tab.rpt_date
 left join   repaid_tab
 on d.full_date = repaid_tab.rpt_date
  left join    due_tab
 on d.full_date = due_tab.rpt_date

)
 insert into dws_loan_process_summary_ds
 select 
     rpt_date,
     apply_amount ,
     apply_cnt ,    
     issue_amount ,
     issue_cnt ,
     repaid_amount ,
     repaid_cnt ,     
     due_amount ,
     due_cnt ,        
     voluntary_amount ,
     voluntary_cnt  
 from join_tab;
"""

# Asynchronously run the query
async def main():
    await db_utils.execute_sql(insert_sql)

# Start the asyncio event loop to run the query
if __name__ == "__main__":
    asyncio.run(main())
