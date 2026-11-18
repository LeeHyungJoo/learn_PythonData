# import
import cx_Oracle as cxo

def sql_excute_and_show(sql):
    cursor.execute(sql)

    for row in cursor:
        print(row)


# DB 연결
conn = cxo.connect('hr', 'hr', "127.0.0.1:1521/XE")
cursor = conn.cursor()

sql_list = [
    {
        "description": "BOSTON이나 DALLAS에 위치한 부서(부서명)를 출력",
        "sql": "select dname from dept where loc='BOSTON' OR loc='DALLAS'"
    },
    {
        "description": "급여가 2000에서 3000 사이인 사원(사원명)을 출력",
        "sql": "select ename from emp where sal>2000 AND sal<3000"
    },
    {
        "description": "이름이 A로 시작되는 사원을 출력",
        "sql": "select ename from emp where ename like 'A%'"
    },
    {
        "description": "커미션 지급 대상인 사원을 출력",
        "sql": "select ename from emp where comm is not null"
    },
    {
        "description": "직종이 CLERK인 사원 중에서 급여가 1000 이상인 사원을 출력",
        "sql": "select ename from emp where job = 'CLERK' AND sal>1000"
    },
    {
        "description": "사번이 7900인 사원의 이름과 급여를 출력",
        "sql": "select ename, sal from emp where empno = 7900"
    },
    {
        "description": "부서번호 내림차순, 같은 부서일 때 급여 내림차순으로 정렬",
        "sql": "select * from emp order by deptno desc, sal desc"
    },
    {
        "description": "20번 부서의 이름과 그 부서에 근무하는 사원의 이름을 출력",
        "sql": """select d.dname, e.ename
                  from dept d, emp e
                  where d.deptno = e.deptno
                  and e.deptno = 20"""
    },
    {
        "description": "직종별 최고 급여를 급여가 많은 직종부터 출력",
        "sql": """select job, max(sal)
                  from emp
                  group by job
                  order by max(sal) desc"""
    },
    {
        "description": "각 부서별로 최고 급여를 받는 사원을 출력",
        "sql": """select deptno, empno, ename, sal
                  from emp
                  where (deptno, sal) in (
                      select deptno, max(sal)
                      from emp
                      group by deptno
                  )"""
    }
]

for idx, item in enumerate(sql_list, start=1):
    print(f"\n========== 문제 {idx} ==========")
    print(f"{item['description']}")
    sql_excute_and_show(item['sql'])


# close
cursor.close()
conn.close()
