#!/bin/bash
log_file="/logs/dws_loan_summary_ds.log"
start_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[$start_time] dws_loan_summary_ds Task Started" >> $log_file

# 运行 Python 脚本任务
python3 dws_loan_summary_ds.py >> $log_file 2>&1
status=$?

end_time=$(date "+%Y-%m-%d %H:%M:%S")
if [ $status -eq 0 ]; then
    echo "[$end_time] dws_loan_summary_ds Completed Successfully" >> $log_file
    exit 0
else
    echo "[$end_time] dws_loan_summary_ds Failed" >> $log_file
    exit 1
fi
