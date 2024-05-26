select d.dept_id, d.dept_name_en, round(avg(h.sal)) as avg_sal from hr_department d
join hr_employees h on d.dept_id = h.dept_id
group by dept_id
order by round(avg(h.sal)) desc