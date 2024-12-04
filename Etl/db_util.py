import asyncpg
import asyncio
class DBUtils:
    def __init__(self):

        self.dbname = 'postgres'
        self.user = 'postgres.cnzhzflrnknemzwqcddu'
        self.password = 'b8.3GB'
        self.host = 'aws-0-ca-central-1.pooler.supabase.com'
        self.port = 6543

    # Method to establish the database connection
    async def _connect(self):
        return await asyncpg.connect(
            host=self.host,
            database=self.dbname,
            user=self.user,
            password=self.password
        )

    # Method to execute SQL query
    async def execute_sql(self, query):
        conn = None
        try:
            # Connect to the database
            conn = await self._connect()
            # Execute the SQL query
            await conn.execute(query)
            print("Query executed successfully")
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            if conn:
                # Close the connection after execution
                await conn.close()