import random

# This function chooses the move to beat the opponent's move
def counter_move(move):
    moves = {"R": "P", "P": "S", "S": "R"}
    return moves[move]

def player(prev_play, opponent_history=[]):
    # Save the opponent's last move in their history
    if prev_play != "":
        opponent_history.append(prev_play)

    # If the opponent has played 3 or more times, look for patterns
    if len(opponent_history) >= 3:
        # Find the move the opponent uses the most
        most_common_move = max(set(opponent_history), key=opponent_history.count)
        # Return the move that beats their most common move
        return counter_move(most_common_move)

    # If there isn't enough data, play randomly
    return random.choice(["R", "P", "S"])
