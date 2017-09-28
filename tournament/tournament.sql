-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- The players table contains infor
-- The players table contains information about players
-- such as playerId, PlayerName and Scores

CREATE TABLE players(playername text, playerid SERIAL PRIMARY KEY);

-- The match table contains information about the match occured
-- between two players and stored who won and lost the match

CREATE TABLE match(
                   winnerid INTEGER REFERENCES players(playerid) ON DELETE CASCADE,
                   loserid INTEGER REFERENCES players(playerid) ON DELETE CASCADE,
                   matchid SERIAL PRIMARY KEY, CHECK (winnerid <> loserid));


-- The playerscount view is used to return the distinct number of players

CREATE VIEW playerscount AS (select count(*) as pcount from players);

-- The winners_count view is used to display the leader board
-- results sorted by players with max number of wins

--CREATE VIEW winners_count AS (select playerid, count(winnerid) as wins from players left join match on playerid = winnerid group by playerid);

-- The losers_count view is used to display the leader board
-- results sorted by players with max number of wins

--CREATE VIEW loser_count AS (select playerid, count(loserid) as loses from players left join match on playerid = loserid group by playerid);

-- The matchesplayed view will show how many matches played by each player
CREATE VIEW scoreboard  AS (
select players.playerid, players.playername, matchesplayed.wins, matchesplayed.matches from players,
(select W.playerid, W.wins+L.loses as matches, W.wins as wins  from
(select playerid, count(winnerid) as wins from players left join match on playerid = winnerid group by playerid) as W,
(select playerid, count(loserid) as loses from players left join match on playerid = loserid group by playerid) as L
where W.playerid = L.playerid
) as matchesplayed where players.playerid = matchesplayed.playerid order by matchesplayed.wins DESC);