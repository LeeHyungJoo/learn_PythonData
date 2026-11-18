# @ sql_sunny.sql
import cx_Oracle as cxo
import sys
import re

# DB 연결
conn = cxo.connect("hr","hr","127.0.0.1:1521/XE")

# 현재 커서 얻기
cursor = conn.cursor()

idx = 1
while True:
    ssn = input("{0}번째 고객의 SSN을 입력하세요 : ".format(idx))

    if ssn == "exit":
        sys.exit()

    if not re.match(r'\d{3}-\d{3}',ssn):
        print("ssn 포맷이 맞지 않습니다. cf) nnn-nnn")
        continue

    name = input("고객 이름\t: ")
    home = input("거주지\t: ")

    # sql 작성
    sql = "insert into customer values(:ssn,:name,:home)"

    # 예외처리
    try:
        cursor.execute(sql, {"ssn":ssn, "name":name, "home":home})
        print("{0}번째 고객이 정상적으로 등록되었습니다. ".format(idx))
    except cxo.IntegrityError as e:
        conn.rollback()
        print("Exception ! : ", e)
    finally:
        conn.commit()


    idx += 1

    # sql 실행
    sql = "select * from customer"
    cursor.execute(sql)
    for c in cursor:
        print(c)

# 예외 처리
# 고객 ID 가 있을때




# 쿼리 작성

# sql 실행



# close
cursor.close()
conn.close()



