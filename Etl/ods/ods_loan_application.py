
import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv
import os
# Supabase 配置信息
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")  # Supabase URL
SUPABASE_KEY = os.getenv("SUPABASE_KEY")  # API 密钥

# 初始化 Supabase 客户端
def init_supabase():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# 读取 CSV 文件并清理数据
def read_and_prepare_data(file_path):


    # 读取 CSV 文件
    data = pd.read_csv(file_path, header=0)

    # print(data.head())
    print(data.isnull().sum())
    data['repaid_amount'] = data['repaid_amount'].fillna(0)
    data['repaid_date'] = data['repaid_date'].fillna('1970-01-01')
    data['repaid_hour'] = data['repaid_hour'].fillna(-1)
    data['repaid_hour'] = data['repaid_hour'].astype(int)
    data['due_hour'] = data['due_hour'].astype(int)
    # print(data.isnull().sum())

    # print(data.dtypes)
    return data



# 将数据批量写入 Supabase
def insert_data_to_supabase(dataframe, table_name, supabase_client):
    # 将 DataFrame 转换为字典列表
    records = dataframe.to_dict(orient="records")

    # 批量插入数据
    for record in records:
        response = supabase_client.table(table_name).insert(record).execute()

# 主函数
def main():
    # 初始化 Supabase 客户端
    supabase = init_supabase()

    # 读取并准备数据
    file_path = "/Users/stanley/Downloads/data.csv"  # CSV 文件路径
    data = read_and_prepare_data(file_path)

    # 写入 Supabase
    table_name = "ods_loan_application"  #
    insert_data_to_supabase(data, table_name, supabase)

    print("Data Load Success!")

if __name__ == "__main__":
    main()

#
# -- CREATE TABLE ods_loan_application (
# --     application_id BIGINT PRIMARY KEY ,
# --     amount DECIMAL(10, 2),
# --     application_date DATE,
# --     issuance_date DATE,
# --     repaid_amount DECIMAL(10, 2),
# --     repaid_date DATE,
# --     application_status VARCHAR(50),
# --     due_date DATE,
# --     is_voluntary_repayment BOOLEAN,
# --     application_hour INTEGER,
# --     issuance_hour INTEGER,
# --     repaid_hour INTEGER,
# --     due_hour INTEGER,
# --     late_days DECIMAL(10, 2)
# -- ) ;
