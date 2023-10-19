import pytest
from typing import List


teleporters1 = ["3,1", "4,2", "5,10"]
teleporters2 = ["5,10", "6,22", "39,40", "40,49", "47,29"]
teleporters3 = ["6,18", "36,26", "41,21", "49,55", "54,52",
                "71,58", "74,77", "78,76", "80,73", "92,85"]
teleporters4 = ["97,93", "99,81", "36,33", "92,59", "17,3",
                "82,75", "4,1", "84,79", "54,4", "88,53",
                "91,37", "60,57", "61,7", "62,51", "31,19"]
teleporters5 = ["3,8", "8,9", "9,3"]


def destinations(teleporters: List[str], die_sides: int, start_position: int, board_size: int) -> None:
    """Calculate all possible board positions for a given die size.

    This function will print every possible board position for the given die
    size, and teleporter configuration.

    Args:
        teleporters: List of teleporters that move the players position if they
            land on a specific location.
        die_sides: Number of sides on the die to be rolled.
        start_position: Players start position on the board.
        board_size: Size of the available board.
    """
    board: Dict[str, int] = {}
    move_history: List[int] = []
    
    for teleporter in teleporters:
        key, value = teleporter.split(',')
        board[int(key)] = int(value)
  
    for roll in range(1, die_sides+1):
        position = start_position + roll

        if position > board_size:
            continue
        else:
            if position in board.keys():
                move_history.append(board[position])
            else:
               move_history.append(position)

    temp_dict = dict.fromkeys(move_history, 0)
    unique = list(temp_dict.keys())
    return unique


@pytest.mark.parametrize(
    "teleporters, die_size, start_position, board_size, expected", 
    [
        (teleporters1, 6, 0, 20, [1, 2, 6, 10]),
        (teleporters2, 6, 46, 100, [48, 49, 50, 51, 52, 29]),
        (teleporters2, 10, 0, 50, [1, 2, 3, 4, 7, 8, 9, 10, 22]),
        (teleporters3, 10, 95, 100, [96, 97, 98, 99, 100]),
        (teleporters3, 10, 70, 100, [72, 73, 75, 76, 77, 79, 58]),
        (teleporters4, 6, 0, 100, [1, 2, 3, 5, 6]),
        (teleporters5, 6, 0, 20, [1, 2, 4, 5, 6, 8])
    ]
)
def test_teleporter1_beginning_of_board(teleporters, die_size, start_position, board_size, expected):
    actual: List[int] = destinations(teleporters, die_size, start_position, board_size)
    assert actual == expected
