CREATE TABLE managers (
id int primary key,
name    varchar(80),
surname     varchar(80),
job_name     varchar(80),
department  varchar(80),
birthday    varchar(80)
);

CREATE TABLE workers(
boss_id int,
id int primary key,
name    varchar(80),
surname     varchar(80),
job_name     varchar(80),
department  varchar(80),
birthday    varchar(80)
);