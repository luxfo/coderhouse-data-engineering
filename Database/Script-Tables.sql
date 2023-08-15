create table teams (
id 				int not null distkey,
abbreviation 	varchar(3) not null,
city 			varchar(50),
conference		varchar(50),
division		varchar(50),
full_name		varchar(100) not null,
name 			varchar(100) not null,
etl_date        date not null
) sortkey(full_name)

ALTER TABLE teams ADD CONSTRAINT teams_pk PRIMARY KEY (id);
ALTER TABLE teams ADD CONSTRAINT teams_un UNIQUE (abbreviation, name, full_name);

go

create table players (
id				int not null distkey,
first_name		varchar(100) not null,
last_name		varchar(100) not null,
position		varchar(5),
team_id			int,
etl_date        date not null
) sortkey(first_name, last_name)

ALTER TABLE players ADD CONSTRAINT players_pk PRIMARY KEY (id);

go
create table games (
id 					int not null distkey,
date 				date not null,
home_team_id		int not null,
home_team_score		int,
period 				int,
postseason			boolean,
season				int,
status 				varchar(10),
visitor_team_id		int not null,
visitor_team_score	int,
etl_date            date not null
) sortkey(date, season)

ALTER TABLE games ADD CONSTRAINT games_pk PRIMARY KEY (id);
ALTER TABLE games ADD CONSTRAINT games_un UNIQUE ("date", home_team_id, visitor_team_id);


