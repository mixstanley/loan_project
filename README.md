1. Data Model
Four layers of tasks were developed:
	1.	ODS Layer (Source Layer): Perform necessary cleaning of source data, then load it into the Supabase database.
	2.	DWD Layer (Detailed Data Layer): Build a star schema by developing fact and dimension tables to support analysis-focused consumption scenarios.
	3.	DWS Layer (Light Aggregation Layer): Aggregate frequently used and core metrics to reduce the cost of querying these metrics repeatedly.
	4.	ADM Layer (Application Layer): Process composite and derived metrics directly for application use, without excessive consideration of reusability.

2. ETL Pipeline
	1.	(ETL) Task: Use Python to wrap SQL to implement the ETL process for each table.
	2.	(Workflow) Scheduling:
	•	Use shell scripts to wrap tasks and handle execution logs.
	•	Define dependencies between tasks via shell scripts.
	•	Use crontab to set the scheduling time and frequency of tasks.
	3.	Utility Classes: Provide abstracted common objects, methods, and configuration information.

3. Dashboard
Connect to the database via Streamlit and use Python libraries to display reports in various formats.
