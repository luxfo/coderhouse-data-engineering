create table if not exists games (
id 					int not null distkey,
date 				date not null,
home_team_id		int not null,
home_team_score		int,
period 				int,
postseason			boolean,
season				int,
status 				varchar(20),
visitor_team_id		int not null,
visitor_team_score	int,
etl_date            date not null,
constraint games_pk primary key (id),
constraint games_uq unique ("date", home_team_id, visitor_team_id)
) sortkey(date, season)
