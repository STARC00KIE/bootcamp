-- where 절 : 추출 시 조건 지정 --

-- 문자형 값 비교
select * from tb_emp
where position = '사원';      -- 비교값 지정 시 '' 사용

-- 숫자 값 비교
select salary,salary/12 from tb_emp
where salary <= 60000000;    -- 숫자

-- 비교 응용
select * from tb_emp
where position = '대리';

select emp_name, position, salary,salary/12 from tb_emp
where salary <= 60000000 and salary > 40000000;

-- 예제1: 연산자 우선 순위 파악
select emp_no, emp_name, org_cd, position, salary
from tb_emp
where (org_cd = '08'
or org_cd = '09'
or org_cd = '10')      -- ()가 없으면 잘못된 결과가 나옴
and position = '사원'
and salary >= 40000000
and salary <= 50000000;

-- 예제1 변형: 별칭 지정으로 상대가 보기 편하게 만들 수 있음
select emp_no 사번, emp_name 사원명, org_cd 조직코드, position 직책, salary 연봉    -- 별칭 정의
from tb_emp
where (org_cd = '08'
or org_cd = '09'
or org_cd = '10')      -- ()가 없으면 잘못된 결과가 나옴
and position = '사원'
and salary >= 40000000
and salary <= 50000000;

-- 예제1 변형: 줄여쓰기 (in, between 사용)
select emp_no 사번, emp_name 사원명, org_cd 조직코드, position 직책, salary 연봉    -- 별칭 정의
from tb_emp
where org_cd in('08', '09', '10')
and position = '사원'
and salary between 40000000 and 50000000;

-- where 조건 지정 방법1. << IN >>
---- 검사할 값이 리스트 내 요소에 포함되는지 확인
---- 만약 DB 내 06팀에 속하는 팀장과 07팀에 속하는 과장 명단만 확인하고 싶다면 어떻게 할까?

-- 방법 1 --
select emp_no 사번, emp_name 사원명, org_cd 조직코드, position 직책, salary 연봉
from tb_emp
where org_cd in ('06', '07')
and position in ('팀장', '과장');      -- 원하는 바가 명확히 나오지 않음

-- 방법 2 --
select emp_no 사번, emp_name 사원명, org_cd 조직코드, position 직책, salary 연봉
from tb_emp
where (org_cd, position)
in (('06', '팀장'), ('07', '과장'));    -- 다중 리스트를 이용하면 출력됨

-- where 조건 지정 방법2. << LIKE >>
---- 와일드 카드 검색 시 사용

select emp_no 사번, emp_name 사원명, org_cd 조직코드, position 직책, salary 연봉
from tb_emp
where emp_name like '김%';      -- 사원명이 '김'으로 시작하는 명단 보기

select emp_no 사번, emp_name 사원명, org_cd 조직코드, position 직책, salary 연봉
from tb_emp
where emp_name like '_승%';     -- 사원명 두 번째 글자가 '승'인 명단 보기

-- where 조건 지정 방법3. << IS NULL >>
----  null값 여부 찾는 문법 (↔ is not null)

select * from tb_emp
where gender = null;  -- 이렇게 하면 결과가 제대로 나오지 않음

select * from tb_emp
where gender is null;

-- where 조건 지정 방법4. << 부정연산자 not >>
select * from tb_emp
where org_cd = '10'
and not position = '팀장';    -- 10번 팀의 팀장 제외 명단 추출

select * from tb_emp
where org_cd is not null;    -- 결측치 없는 명단 추출

-- order by : 정렬 --
---- 기본적으로 오름차순 정렬

select * from tb_emp
order by salary asc;

select * from tb_emp
order by salary desc;


-- order by 사용 연습
select * from tb_emp                    -- org_cd 기준으로 오름차순, ent_date 기준으로 내림차순
order by org_cd asc, ent_date desc;     -- asc는 생략 가능. 기본값이기 때문


select * from tb_emp
order by org_cd, ent_date desc;         -- asc는 생략 가능. 기본값이기 때문 (윗 구문과 같은 결과 나옴)


select org_cd, emp_name, ent_date
from tb_emp
order by 1 asc, 3 desc;                  -- 컬럼 지정을 숫자로 할 수도 있음



-- 결괏값 개수 제한 limit
select * from tb_accnt
order by cont_amt desc limit 10;


select * from tb_accnt
order by cont_amt desc, op_date desc limit 3;    -- cont_amt 기준으로 내림차순 후 날짜 기준 최신으로 3개가 나오게 하기



-- where로 조건 주고 정렬하는 구문 연습
select
	org_cd,
	emp_name,
	ent_date
from
	tb_emp
where
	org_cd is not null
order by
	org_cd desc,
	ent_date desc;