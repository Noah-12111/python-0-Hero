"""Exercise 02: compose Bot with a strategy."""


class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)


def move_toward_goal(state):
    """Đi một bước về phía goal; goal có thể là 0 hoặc 4."""
    position = state["position"]
    goal = state["goal"]

    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state):
    """Đứng yên nếu đối thủ ở ngay cạnh; nếu không thì đi về goal."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state):
    return move_toward_goal(state)


def aggressive(state):
    # Arena đơn giản chỉ có left, right và wait.
    # Vì thế aggressive cũng đi thẳng về goal như balanced.
    return move_toward_goal(state)


state = {"position": 3, "opponent_position": 4, "goal": 0}

print("Defensive:", Bot(defensive).choose_action(state))  # wait
print("Balanced:", Bot(balanced).choose_action(state))    # left
print("Aggressive:", Bot(aggressive).choose_action(state))  # left

# Đổi strategy bằng cách tạo Bot mới; không cần sửa class Bot.
bot = Bot(balanced)
print("Before:", bot.choose_action({"position": 1, "goal": 4}))  # right
bot = Bot(defensive)
print("After:", bot.choose_action({"position": 1, "opponent_position": 2, "goal": 4}))  # wait
