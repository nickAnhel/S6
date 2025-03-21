-- Query 1
select department_id, department_name, count(employee_id) as workers_count
from employees
join departments using(department_id)
group by department_id, department_name
order by workers_count;


-- Query 2
select *
from employees
where job_id = 'IT_PROG'
order by salary desc
limit 1;


-- Bonus query
create or replace function get_dpt_managers_count() returns int as $$
begin
  return (
    select count(*)
    from employees
    where employee_id in (select distinct manager_id from departments)
  );
end;
$$ language plpgsql;


create or replace function get_managers_count() returns int as $$
declare
  dpt_managers_count int;
begin
  dpt_managers_count := get_dpt_managers_count();
  return (
    select count(*) - dpt_managers_count
    from employees
    where (
      job_id ilike '%man' or
      job_id ilike '%mgr' or
      job_id ilike '%vp'
    )
  );
end;
$$ language plpgsql;


create or replace function get_workers_count() returns int as $$
declare
  dpt_managers_count int;
  managers_count int;
begin
  dpt_managers_count := get_dpt_managers_count();
  managers_count := get_managers_count();
  return (select count(*) - dpt_managers_count - managers_count from employees);
end;
$$ language plpgsql;


select 'dpt_managers' as emp, get_dpt_managers_count() as cnt
union
select 'managers' as emp, get_managers_count() as cnt
union
select 'workers' as emp, get_workers_count() as cnt
order by emp;