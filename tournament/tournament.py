#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect(dbname="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        return db
    except:
        print("<error message>")

def queryexecution(query,parameter=None):
    db = connect()
    cursor = db.cursor()
    cursor.execute(query,parameter)
    db.commit()
    db.close()

def deleteMatches():
    """Remove all the match records from the database."""
    query = "delete from match;"
    queryexecution(query)


def deletePlayers():
    """Remove all the player records from the database."""
    query = "delete from players;"
    queryexecution(query)

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("select * from playerscount")
    count = c.fetchone()
    db.close()
    return count[0]

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    query="insert into players (playername) values (%s);"
    name = bleach.clean(name)
    parameter = (name,)
    queryexecution(query, parameter)



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db =connect()
    c = db.cursor()
    c.execute("select * from scoreboard")
    results = c.fetchall()
    db.close()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = "insert into match (winnerid, loserid) values (%s,%s);"
    winner = bleach.clean(winner)
    loser = bleach.clean(loser)
    parameter = (winner, loser)
    queryexecution(query,parameter)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    results = playerStandings()
    swisspairs = []
    subpair = []
    for r in results:
        if len(subpair) >= 0 and len(subpair) < 4:
            subpair.append(r[0])
            subpair.append(r[1])
        else:
            swisspairs.append(subpair)
            subpair = [r[0], r[1]]
    swisspairs.append(subpair)
    return swisspairs