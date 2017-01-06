/* Deletes the database if it exists */
DROP DATABASE IF EXISTS tournament;

/* Create database */
CREATE DATABASE tournament;

-- Connect to the DB before creating tables.
\c tournament;

/* Create SCHEMAS */
CREATE TABLE player(
    id SERIAL PRIMARY KEY,
    name TEXT
);
CREATE TABLE match(
    match_id SERIAL PRIMARY KEY,
    winner INTEGER REFERENCES player(id),
    loser INTEGER REFERENCES player(id)
);
CREATE VIEW standings AS 
SELECT player.id, player.name, (SELECT COUNT(*) FROM match WHERE match.winner = player.id) AS wins, (SELECT COUNT(*) FROM match WHERE player.id IN(winner, loser)) AS matches FROM player;
/*
 id |     name     | wins | matches 
----+--------------+--------+---------
 93 | Bruno Walton |      1 |       1
 94 | Boots O'Neal |      1 |       1
 95 | Cathy Burton |      0 |       1
 96 | Diane Grant  |      0 |       1
 */
 