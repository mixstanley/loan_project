#!/bin/bash
log_file="/logs/ods_loan_application.log"
start_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[$start_time] ods_loan_application Task Started" >> $log_file

# 运行 Python 脚本任务
python3 ods_loan_application.py >> $log_file 2>&1
status=$?

end_time=$(date "+%Y-%m-%d %H:%M:%S")
if [ $status -eq 0 ]; then
    echo "[$end_time] ods_loan_application Completed Successfully" >> $log_file
    exit 0
else
    echo "[$end_time] ods_loan_application Failed" >> $log_file
    exit 1
fi
