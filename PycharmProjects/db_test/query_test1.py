# 라이브러리
import cx_Oracle

# Oracle의 샘플 HR 스키마를 사용
# database connection 연결
# cx_Oracle.connect("id","password", "ip:port/서비스이름")
connection = cx_Oracle.connect(user="hr", password ="hr", dsn="127.0.0.1:1521/XE")

# cursor 얻기
# cursor(커서)는 명령문을 실행하고 결과(있는 경우)를 가져오는 객체
cursor = connection.cursor()

# 조회할 데이터
manager_id = 145
first_name = "Peter"

# 쿼리 작성 및 실행
# 명령문이 실행될 때 manager_id 및 first_name 의 데이터 값은 명령문 자리 표시자 '바인딩 변수'에 '바인딩'됨
# :mid. :fn 형식은 SQL 삽입 보안 위험을 방지하는 데 도움이 되는 데이터에서 명령문 텍스트가 분리해줌
# 바인딩은 성능과 확장성에도 중요
sql = "SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEES WHERE MANAGER_ID =:min AND FIRST_NAME =:fn"

cursor.execute(sql, {"min":manager_id, "fn":first_name})

# result set(결과집합) 으로 부터 반복하며 데이터 꺼내서 출력
# cursor(커서)를 사용하면 행을 반복하고 표시할 수 있음
for row in cursor:
    print(row)

cursor.close()
connection.close()