import streamlit as st
from supabase import create_client
from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt

# 加载环境变量
load_dotenv()

# 获取 Supabase 配置信息
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# 创建 Supabase 客户端
supabase = create_client(url, key)

res = supabase.table("adm_kpi_report_ds").select("*").execute()

if res.data:
    data = pd.DataFrame([res.data[0]])  # 将记录转换为 DataFrame
    st.title("KPI Dashboard")

    # 展示数据表格
    st.subheader("Raw Data")
    st.dataframe(data)

    # 可视化每个字段
    st.subheader("Visualizations")


    # 总申请数
    st.write("### Total Application")
    st.metric("Total Application", f"{data['total_cnt'][0]}")


    # 还款率
    st.write("### Repaid Application")
    st.metric("Repaid Application", f"{data['repaid_cnt'][0]}")

    # 还款率
    st.write("### Outgoing Application")
    st.metric("Outgoing Application", f"{data['outgoing_cnt'][0]}")


    # 还款率
    st.write("### Repayment Rate")
    st.metric("Repayment Rate", f"{data['repayment_rate'][0]:.2%}")


    # 自愿提前还款比例
    st.write("### Voluntary Repayment Percentage")
    st.metric("Voluntary Repayment %", f"{data['voluntary_repayment_percentage'][0]:.2%}")

    # 逾期还款比例
    st.write("### Late Repayment Percentage")
    st.metric("Late Repayment %", f"{data['late_repayment_percentage'][0]:.2%}")


else:
    st.error("No data found in the table!")