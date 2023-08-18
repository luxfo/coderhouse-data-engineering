create table if not exists teams (
id 				int not null distkey,
abbreviation 	varchar(3) not null,
city 			varchar(50),
conference		varchar(50),
division		varchar(50),
full_name		varchar(100) not null,
name 			varchar(100) not null,
etl_date        date not null,
constraint teams_pk primary key (id),
constraint teams_uq unique (abbreviation, name, full_name)
) sortkey(full_name)




