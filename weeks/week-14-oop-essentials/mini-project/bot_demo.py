"""Mini-project: use composition to swap a bot's strategy."""


class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)


def move_toward_goal(state):
    position = state["position"]
    goal = state["goal"]

    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state):
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state):
    return move_toward_goal(state)


def aggressive(state):
    # Arena của bài chỉ có left/right/wait, nên strategy này cũng đi thẳng về goal.
    return move_toward_goal(state)


def main():
    examples = [
        ("Goal bên phải", {"position": 1, "opponent_position": 4, "goal": 4}),
        ("Goal bên trái", {"position": 3, "opponent_position": 4, "goal": 0}),
        ("Đã tới goal", {"position": 2, "opponent_position": 4, "goal": 2}),
    ]
    strategies = [
        ("defensive", defensive),
        ("balanced", balanced),
        ("aggressive", aggressive),
    ]

    for title, state in examples:
        print(f"\n{title}: {state}")
        for name, strategy in strategies:
            bot = Bot(strategy)
            action = bot.choose_action(state)
            print(f"  {name}: {action}")


if __name__ == "__main__":
    main()
