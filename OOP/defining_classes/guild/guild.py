# from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player.guild != self.name and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        if player not in self.list_of_players:
            self.list_of_players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name):
        try:
            player_to_remove = [player for player in self.list_of_players if player.name == player_name][0]
            player_to_remove.guild = "Unaffiliated"
            self.list_of_players.remove(player_to_remove)
            return f"Player {player_name} has been removed from the guild."
        except IndexError:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        output = f"Guild: {self.name}\n"
        for member in self.list_of_players:
            output += member.player_info()
        return output

#
# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
