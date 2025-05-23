from project.player import Player

class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    def add_player(self, player: "Player"):
        # Check by player name (property)
        for p in self.__players:
            if p.name == player.name:
                return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for p in self.__players:
            if p.name == player_name:
                self.__players.remove(p)
                return p
        return f"Player {player_name} not found"
