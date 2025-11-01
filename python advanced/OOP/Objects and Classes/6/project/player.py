class Player:
    def __init__(self, name, hp, mp):
        self.skills = {}
        self.guild = "Unaffiliated"
        self.name = name
        self.hp = hp
        self.mp = mp

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self):
        skills = "\n".join("===" + name + " - " + str(mana_cost) for name, mana_cost in self.skills.items())

        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{skills}\n"