create table if not exists jobs (
    job_id varchar(10) PRIMARY KEY,
    job_title varchar(35) NOT NULL,
    min_salary integer,
    max_salary integer
);


create table if not exists departments (
    department_id integer PRIMARY KEY,
    department_name varchar(30) NOT NULL,
    manager_id integer
);


create table if not exists employees (
    employee_id serial PRIMARY KEY,
    first_name varchar(20) NOT NULL,
    last_name varchar(25) NOT NULL,
    job_id varchar(10) NOT NULL REFERENCES jobs (job_id),
    salary integer,
    manager_id integer,
    department_id integer NOT NULL REFERENCES departments (department_id)
);


alter table departments
add constraint mgr_emp_fkey foreign key (manager_id) references employees(employee_id);
