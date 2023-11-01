class Game:

#DELIVERABLE 1:
# Player __init__(self, username)
# Player is initialized with a username
# Player property username
# Returns the player's username
# Usernames must be of type str
# Usernames must be between 2 and 16 characters, inclusive.
# Should be able to change after the player is instantiated

    def __init__(self, title):
        self.title = title
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and  0 < len(title) and not hasattr(self, "title"):
            self._title = title
# Deliverable 1 ^^^

# DELIVERABLE 6:
# Game results()
# Returns a list of all results for that game
# Results must be of type Result

# Game players()
# Returns a unique list of all players that played a particular game
# Players must be of type Player

    def results(self):
        return list({result for result in Result.all if result.game is self})

    def players(self):
        return list({ result.player for result in self.results()})
# Deliverable 6 ^^^

# DELIVERABLE 8:
# Game average_score(player)
# Receives a player object as argument
# Returns the average of all the player's scores for a particular game instance
# Reminder: you can calculate the average by adding up all the results' scores of
# the player specified and dividing by the number of those results
    def average_score(self, player):
        return sum([result.score for result in self.results()])/len(self.results())
# Deliverable 8 ^^


class Player:
    
# DELIVERABLE 2:
# Player __init__(self, username)
# Player is initialized with a username
# Player property username
# Returns the player's username
# Usernames must be of type str
# Usernames must be between 2 and 16 characters, inclusive.
# Should be able to change after the player is instantiated

    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
# Deliverable 2 ^^^^


# DELIVERABLE 5:
# Player results()

# Returns a list of all results for that player
# Results must be of type Result
# Player games_played()

# Returns a unique list of all games played by a particular player
# Games must be of type Game

    def results(self):
        return list({result for result in Result.all if result.player is self})

    def games_played(self):
        return list({result.game for result in self.results()})
# Deliverable 5 ^^


# Deliverable 7:
# Player
# Player played_game(game)
# Receives a game object as argument
# Returns True if the player has played the game object provided
# Returns False otherwise
# Player num_times_played(game)
# Receives a game object as argument
# Returns the number of times the player has played the game instance provided
# Returns 0 if the player never played the game provided

    def played_game(self, game):
        return game in self.games_played()
        

    def num_times_played(self, game):
            return len([result for result in self.results() if result.game == game])
# Deliverable 7 ^^^

# BONUS:
# Player classmethod highest_scored(game)
# Receives a game object as argument
# Returns the Player instance with the highest average score for the game provided.
# Returns None if there are no players that played the game provided.
# hint: will need a way to remember all player objects
# hint: do you have a method to get the average score on a game for a particular player?
# Uncomment lines 151-161 in the player_test file

# @classmethod
# def highest_score(self, game):

# Bonus Deliverable ^^^



class Result:
    all =[]
# DELIVERABLE 3:
# Result __init__(self, player, game, score)
# Result is initialized with a Player instance, a Game instance, and a score.
# Result property score
# Returns the result's score
# Scores must be of type int
# Scores must be between 1 and 5000, inclusive
# Should not be able to change after the result is instantiated
# hint: hasattr()

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, "score"):
            self._score = score
# Deliverable 3 ^^^^



#DELIVERABLE 4:
# Result property player
# Returns the player object for that result
# Must be of type Player
# Result property game
# Returns the game object for that result
# Must be of type Game

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
# Deliverable 4 ^^^