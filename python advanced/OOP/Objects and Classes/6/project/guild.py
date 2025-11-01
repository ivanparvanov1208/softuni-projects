from .player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated" and player.guild != self.name:
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = f"{self.name}"
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name and player in self.players:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player.name} has been removed from the guild."
            elif player not in self.players:
                return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players = "\n".join(p.player_info() for p in self.players)
        return f"Guild: {self.name}\n{players}"
