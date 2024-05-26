with value as (select emp_no, 
case
    when avg(score) >= 96 then 'S'
    when avg(score) >= 90 then 'A'
    when avg(score) >= 80 then 'B'
    else 'C'
end as grade, 
case
    when avg(score) >= 96 then 0.2
    when avg(score) >= 90 then 0.15
    when avg(score) >= 80 then 0.1
    else 0
end as bonus
from hr_grade
group by emp_no
)

select e.emp_no, e.emp_name, grade, sal * bonus as bonus from hr_employees e
join value v on v.emp_no = e.emp_no
order by emp_no
