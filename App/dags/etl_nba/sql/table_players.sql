
create table if not exists players (
id				int not null distkey,
first_name		varchar(100) not null,
last_name		varchar(100) not null,
position		varchar(5),
team_id			int,
etl_date        date not null,
constraint players_pk primary key (id)
) sortkey(first_name, last_name)

