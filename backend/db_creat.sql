CREATE TABLE managers (
id int primary key,
name    varchar(80),
surname     varchar(80),
job_name     varchar(80),
department  varchar(80),
birthday    varchar(80)
);

CREATE TABLE workers(
manager_id int REFERENCES managers (id),
id int primary key,
name    varchar(80),
surname     varchar(80),
job_name     varchar(80),
department  varchar(80),
birthday    varchar(80)
);