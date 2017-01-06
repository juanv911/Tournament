#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach
import pprint

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("DELETE FROM match")
    dbConn.commit()
    dbConn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("DELETE FROM player")
    dbConn.commit()
    dbConn.close()
    
def countPlayers():
    """Returns the number of players currently registered."""
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("SELECT COUNT(name) FROM player")
    players = c.fetchone()[0]
    dbConn.close()
    return players

def registerPlayer(name):
    """Adds a player to the tournament database."""
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("INSERT INTO player (name) VALUES (%s)", (name,))
    dbConn.commit()
    dbConn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins."""
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("SELECT * FROM standings")
    standings = c.fetchall()
    dbConn.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players."""
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("INSERT INTO match (winner, loser) VALUES (%s,%s)", (winner, loser))
    dbConn.commit()
    dbConn.close()

def swissPairings():
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("SELECT * FROM standings ORDER BY wins DESC")
    standings = c.fetchall()
    dbConn.close()
    pairings = list()

    for player1, player2 in zip(standings[0::2], standings[1::2]):
        pairings.append((player1[0], player1[1], player2[0], player2[1]))

    return pairings

