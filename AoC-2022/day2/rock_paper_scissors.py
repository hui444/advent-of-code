from enum import Enum 

f = open("day2/input.txt", "r")
f = f.read().split("\n")

class PlayerMove(Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'

class OpponentMove(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

class RoundScore(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0

class MoveScore(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# player POV
def get_round_results(playerMove, opponentMove):
    if playerMove is PlayerMove.ROCK:
        if opponentMove is OpponentMove.SCISSORS:
            return RoundScore.WIN
        if opponentMove is OpponentMove.ROCK:
            return RoundScore.DRAW
        # opponent move = PAPER
        return RoundScore.LOSE

    if playerMove is PlayerMove.PAPER:
        if opponentMove is OpponentMove.ROCK:
            return RoundScore.WIN
        if opponentMove is OpponentMove.PAPER:
            return RoundScore.DRAW
        # opponent move = SCISSORS
        return RoundScore.LOSE

    # player move = SCISSORS
    if opponentMove is OpponentMove.PAPER:
        return RoundScore.WIN
    if opponentMove is OpponentMove.SCISSORS:
        return RoundScore.DRAW
    # opponent move = ROCK
    return RoundScore.LOSE

def get_player_round_total_score(playerMove, opponentMove):
    round_score = get_round_results(playerMove, opponentMove).value
    move_score = MoveScore[playerMove.name].value
    return round_score + move_score

def get_player_total_score():
    player_score = 0
    for round in f:
        move = round.split(" ")
        playerMove = PlayerMove(move[1])
        opponentMove = OpponentMove(move[0])
        player_score += get_player_round_total_score(playerMove, opponentMove)
    return player_score

print(f"part1: {get_player_total_score()}")

class ExpectedResult(Enum):
    LOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'

def get_player_move(opponentMove, expectedResult):
    if expectedResult is ExpectedResult.DRAW:
        return PlayerMove[opponentMove.name]
    
    if expectedResult is ExpectedResult.WIN:
        if opponentMove is OpponentMove.PAPER:
            return PlayerMove.SCISSORS
        if opponentMove is OpponentMove.ROCK:
            return PlayerMove.PAPER
        # opponent move = SCISSORS
        return PlayerMove.ROCK

    # expected result = LOSE
    if opponentMove is OpponentMove.PAPER:
        return PlayerMove.ROCK
    if opponentMove is OpponentMove.ROCK:
        return PlayerMove.SCISSORS
    # opponent move = SCISSORS
    return PlayerMove.PAPER

def get_player_total_score_from_expected_result():
    player_score = 0
    for round in f:
        move = round.split(" ")
        opponentMove = OpponentMove(move[0])
        expectedResult = ExpectedResult(move[1])
        player_move = get_player_move(opponentMove, expectedResult)
        player_score += get_player_round_total_score(player_move, opponentMove)
    return player_score

print(f"part2: {get_player_total_score_from_expected_result()}")