from random import randrange

class Board:
    """
    The first two ranks of the board at start of a game of Fischer Random Chess.
    """
    def __init__(self):
        def set_piece(max_skip_spaces, character):
            """
            Put a piece onto the board.
            :param max_skip_spaces: The maximum number of spaces the piece could skip from left to right in placement.
            :param character: The character used to represent the piece.
            """
            skip_spaces = randrange(0, max_skip_spaces + 1)

            for i in range(0, 8):
                if self.random_rank[i] == "":
                    skip_spaces -= 1

                    if skip_spaces <= 0:
                        self.random_rank[i] = character
                        break

        # Random rank
        self.random_rank = [""]*8
        self.random_rank[randrange(0, 7, 2)] = "♗"  # Bishop 1
        self.random_rank[randrange(1, 8, 2)] = "♗"  # Bishop 2
        set_piece(6, "♕")  # Queen
        set_piece(4, "♘")  # Knight 1
        set_piece(3, "♘")  # Knight 2
        set_piece(0, "♖")  # Rook 1
        set_piece(0, "♔")  # King
        set_piece(0, "♖")  # Rook 2

    def __str__(self):
        output = "♙"*8 + "\n"

        for piece in self.random_rank:
            output += piece

        return output
