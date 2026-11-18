import cx_Oracle
import os

## 아래 코드는 이미 오라클 설치시 환경변수로 등록되어 있으므로 생략해도 무방 ##
# 인스턴트 클라이언트 프로그램 설치 경로
# loc = r"C:\oraclexe\app\oracle\product\11.2.0\server\bin"
# 환경 변수 등록
# os.environ["PATH"] = loc + ";" + os.environ['PATH']
######################################################################

# conn = cx_Oracle.connect("id","password", "ip:port/서비스이름")
conn = cx_Oracle.connect("scott","tiger", "127.0.0.1:1521/XE")
# conn = cx_Oracle.connect("hr","hr", "127.0.0.1:1521/XE")
cursor = conn.cursor()

sql = "select * from emp"  #scott/tiger
# sql = "select * from employees" #hr/hr

cursor.execute(sql)

for c in cursor:
    print(c)

cursor.close()
conn.close()