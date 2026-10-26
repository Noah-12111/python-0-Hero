"""Compose a bot with a replaceable strategy."""


class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)


def move_toward_goal(state):
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
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
    # Trong line arena đơn giản, aggressive cũng đi thẳng về goal.
    return move_toward_goal(state)


state = {"position": 3, "opponent_position": 4, "goal": 0}

for name, strategy in [
    ("defensive", defensive),
    ("balanced", balanced),
    ("aggressive", aggressive),
]:
    bot = Bot(strategy)
    print(f"{name}: {bot.choose_action(state)}")

# Output:
# defensive: wait
# balanced: left
# aggressive: left
