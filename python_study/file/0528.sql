-- cslee 스키마에 Set as Default 설정해두기


-- 테이블 생성 create table (emp 테이블 복사하여 tb_test1 생성)
create table tb_test1
as
select * from tb_emp;

select * from tb_test1;   -- 확인



-- 제약조건 추가 add constraint (pk 생성)
alter table tb_test1
add constraint pk_test1 primary key(emp_no);

-- 제약조건 삭제 drop constraint (생성한 pk 제거) 
alter table tb_test1
drop constraint pk_test1;



-- 테이블명 수정 rename to (tb_test1 > tb_test2)
alter table tb_test1
rename to tb_test2;

select * from tb_test2;   -- 확인

alter table tb_test2      -- 재변경 (tb_test2 > tb_test1)
rename to tb_test1;

select * from tb_test1;   -- 확인



-- 데이터 제거 truncate
---- truncate의 특징 : 구조를 유지한 채 모든 행 삭제
truncate table tb_test1;

select * from tb_test1;   -- 실행하면 오류가 나는 게 아니라 데이터가 제거된 빈 테이블이 나옴


-- 테이블 제거 drop
---- drop의 특징 : 테이블 안의 모든 데이터와 구조 삭제
drop table tb_test1;

select * from tb_test1;   -- 실행하면 오류 발생: "tb_test1" 이름의 릴레이션(relation)이 없습니다

-- 중복 제거 distinct
select * from tb_org;
select distinct org_cd from tb_org;

select * from tb_cust;
select distinct cust_no from tb_cust;



-- 들여쓰기, tab 예시
select
	cust_no,
	cust_name
from
	tb_cust;
	


-- 특정 컬럼만 확인하기
select emp_no, emp_name, org_cd, position, gender  -- 참고) position이라는 예약어가 있어서 position 컬럼은 색깔이 입혀져서 보임
from tb_emp;


select distinct position from tb_emp;



-- 별칭 지정
select emp_no as 사번,
emp_name 사원이름 from tb_emp;   -- 별칭에 띄어쓰기를 넣고 싶다면 큰 따옴표로 묶어줘야 함. 작은 따옴표 X



-- 산술연산자 사용
select emp_no as 사번,
emp_name "사원 이름", salary 연봉,
(salary/12*3) 보너스, (salary / 12 * 3 * 0.75) 실보너스,
(salary / 12 * 3 * 0.9) "Re"
from tb_emp;

-- 합성 연산자 (문자와 문자 연결)
select emp_name|| ' 님의 연봉은 ' || salary || '원 입니다'   -- 문자열은 작은 따옴표 표기
from tb_emp;

-- 날짜 연산자
select current_timestamp + '- 12 months';

select current_timestamp + '+ 30 minutes';

select current_timestamp + '3 years - 1 days';

-- 현재 데이터베이스의 정보 조회 (잘 안 쓰이지만 필요 시 사용하는 기능)
select 
	current_catalog,
	current_user,
	current_schema ,
	current_date,
	current_time,
	current_timestamp;

-- 데이터 삽입: 일부 컬럼값만 입력
insert into tb_emp(emp_no, emp_name, ent_date)
values(1051, '김미정', '2014-01-02');

-- 데이터 삽입: 전체 데이터 입력
insert into tb_emp
values(1052, '황기범', null, '사원', null,'M', '2014-01-02', current_timestamp);  -- 개수를 맞춰넣어야함

select * from tb_emp;    -- 확인

-- 데이터 수정
create table tb_emp3     -- 데이터 수정할 임시 테이블 생성
as
select * from tb_emp;

update tb_emp3           -- gender 컬럼값을 전부 M으로 수정
set gender = 'M';

select * from tb_emp3;   -- 확인

-- 데이터 삭제 delete 
delete from tb_emp3