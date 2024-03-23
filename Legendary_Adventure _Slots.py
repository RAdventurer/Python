import random

# Define adventurers and their corresponding symbols and values
adventurers = {
    "Warrior": {"symbol": "⚔️", "value": 5},
    "Rogue": {"symbol": "🗡️", "value": 4},
    "Wizard": {"symbol": "🔮", "value": 3},
    "Paladin": {"symbol": "🛡️", "value": 2}
}

# Define special actions and their corresponding symbols
special_actions = {
    "Dragon Slayer": "🐉",
    "Treasure Hunter": "💰",
    "Mystic Rune": "🌀"
}

# Define the size of the grid
ROWS = 3
COLS = 3

class LegendaryAdventureSlots:
    def __init__(self):
        self.scoreboard = {adventurer: 0 for adventurer in adventurers}
        self.current_player = None

    def get_slot_machine_spin(self):
        return [[random.choice(list(adventurers.keys())) for _ in range(ROWS)] for _ in range(COLS)]

    def print_slot_machine(self, columns):
        for row in range(ROWS):
            for column in columns:
                print(adventurers[column[row]]["symbol"], end=" | ")
            print()

    def check_winnings(self, columns):
        winnings = 0
        for row in range(ROWS):
            symbols = [column[row] for column in columns]
            unique_symbols = set(symbols)
            if len(unique_symbols) == 1:
                adventurer = symbols[0]
                winnings += adventurers[adventurer]["value"]
                self.scoreboard[adventurer] += 1
        return winnings

    def trigger_special_action(self):
        symbols = random.choices(list(special_actions.values()), k=3)
        return symbols

    def spin(self):
        print(f"\n{self.current_player}, it's your turn to spin!")
        input("Press Enter to spin the reels...")
        slots = self.get_slot_machine_spin()
        self.print_slot_machine(slots)
        winnings = self.check_winnings(slots)
        print(f"You won {winnings} adventure points!")
        if random.random() < 0.3:
            special_symbols = self.trigger_special_action()
            print("Special symbols appeared:", *special_symbols)
        return winnings

    def play_game(self):
        num_players = int(input("Enter the number of players: "))
        players = []
        for i in range(1, num_players + 1):
            player_name = input(f"Enter name for Player {i}: ")
            players.append(player_name)

        while True:
            for player in players:
                self.current_player = player
                winnings = self.spin()
                print(f"{self.current_player}'s total adventure points: {self.scoreboard}")
                if self.scoreboard[self.current_player] >= 3:
                    print(f"\nCongratulations {self.current_player}! You are the ultimate champion of the Legendary Adventure Slots Tournament!")
                    return

if __name__ == "__main__":
    game = LegendaryAdventureSlots()
    game.play_game()
