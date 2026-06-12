from db_config import get_connection 
from psycopg2.extras import RealDictCursor 

def get_all_xodimlar(): 
    with get_connection() as conn: 
        with conn.cursor(
            cursor_factory=RealDictCursor
        ) as cur:
            cur.execute( "SELECT * FROM xodimlar" )
            return cur.fetchall() 

def get_one_employee(emp_id): 
    with get_connection() as conn:
        with conn.cursor(
            cursor_factory=RealDictCursor
        ) as cur:
            cur.execute( """SELECT * FROM xodimlar WHERE id = %s""", (emp_id,))
            return cur.fetchone() 

def get_high_salary_xodimlar(limit_salary): 
    with get_connection() as conn:
        with conn.cursor(
            cursor_factory=RealDictCursor
        ) as cur:
            cur.execute(
                """SELECT *FROM xodimlar WHERE maosh > %s""",(limit_salary,) )
            return cur.fetchall()

def employee_statistics():
    with get_connection() as conn:
        with conn.cursor(
            cursor_factory=RealDictCursor
        ) as cur:
            cur.execute("""SELECT COUNT(*) as total_xodimlar, AVG(maosh) as average_salary,MAX(maosh) as max_salary
FROM xodimlar """)
            return cur.fetchone()

def top_employee():
    with get_connection() as conn:
        with conn.cursor(
            cursor_factory=RealDictCursor
        ) as cur:
            cur.execute("""SELECT * FROM xodimlar ORDER BY maosh DESC LIMIT 1""")
            return cur.fetchone()
        
