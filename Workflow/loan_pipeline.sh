#!/bin/bash
log_file="/logs/loan_pipeline.log"

# Step 1: Run ODS Task
bash /tasks/ods_loan_application.sh
if [ $? -ne 0 ]; then
    echo "ods_loan_application Task Failed. Pipeline Aborted." >> $log_file
    exit 1
fi

# Step 2: Run DWD Task
bash /tasks/fact_loan_application.sh
if [ $? -ne 0 ]; then
    echo "fact_loan_application Task Failed. Pipeline Aborted." >> $log_file
    exit 1
fi

# Step 3: Run DWS Task
bash /tasks/dws_loan_summarty_ds.sh
if [ $? -ne 0 ]; then
    echo "dws_loan_summarty_ds Task Failed. Pipeline Aborted." >> $log_file
    exit 1
fi

# Step 4: Run ADS Task
bash /tasks/adm_kpi_report_ds.sh
if [ $? -ne 0 ]; then
    echo "adm_kpi_report_ds Task Failed. Pipeline Aborted." >> $log_file
    exit 1
fi

echo "ETL Pipeline Completed Successfully" >> $log_file
