# Tournament Results

## Files 

**tournament.py**  

Contains the implementation for the Swiss tournament  

**tournament.sql**  

Contains the SQL queries to create the database, tables and views   

**tournament_test.py**  

Contains the test cases for tournament.py  

## Prerequisites 

The latest vagrant build for the Udacity tournament project. (In project notes)

## Instructions

1. Start Vagrant
  1. Open Terminal or cmd and browse to the vagrant folder
  2. Type `vagrant up`
2. SSH in to the vagrant VM
  1. In the same terminal type `vagrant ssh`
3. Change to the correct folder
  1. Type `cd /vagrant/Tournament`
4. Open PSQL and run the tournament.sql 
  1. type `psql`
  2. copy the contents of tournament.sql and paste in to the terminal window
  3. type `\q` to quit out of PSQL 
5. Run the tests
  1. In the terminal type `python tournament_test.py`

## Expected Outcome

Success!  All tests pass!  
vagrant@vagrant-ubuntu-trusty-32:/vagrant/Tournament$ python tournament_test.py  

1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
