create table teams (
id 				int distkey,
abbreviation 	varchar(3),
city 			varchar(50),
conference		varchar(50),
division		varchar(50),
full_name		varchar(100),
name 			varchar(100)
) sortkey(full_name)
go

create table players (
id				int distkey,
first_name		varchar(100),
last_name		varchar(100),
position		varchar(1),
height_feet		int,
height_inches	int,
weight_pounds	int,
team_id			int
) sortkey(first_name, last_name)

go
create table games (
id 					int distkey,
date 				date,
home_team_id		int,
home_team_score		int,
period 				int,
postseason			boolean,
season				int,
status 				varchar(10),
time 				varchar(10),
visitor_team_id		int,
visitor_team_score	int
) sortkey(date, season)
go