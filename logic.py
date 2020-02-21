# 2/19/2020
# Serfault. A chess-like game with different pieces, conditions, and a larger board.

from random import seed
from random import randint

# 7 x 7
# (x, y): occupied
spaces = \
    {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0, (0, 5): 0, (0, 6): 0,
     (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0, (1, 5): 0, (1, 6): 0,
     (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0, (2, 5): 0, (2, 6): 0,
     (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0, (3, 5): 0, (3, 6): 0,
     (4, 0): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0, (4, 5): 0, (4, 6): 0,
     (5, 0): 0, (5, 1): 0, (5, 2): 0, (5, 3): 0, (5, 4): 0, (5, 5): 0, (5, 6): 0,
     (6, 0): 0, (6, 1): 0, (6, 2): 0, (6, 3): 0, (6, 4): 0, (6, 5): 0, (6, 6): 0,
     (7, 0): 0, (7, 1): 0, (7, 2): 0, (7, 3): 0, (7, 4): 0, (7, 5): 0, (7, 6): 0,
}


class Piece:

    def __init__(self, attack_dir, attack_dist, start_pos, movement_dist, dist_increment, alias_id):
        # This string var is a way to identify which
        # directions relative to the piece it can attack.
        self.attack_dir = attack_dir
        # Pieces have a mandatory attack distance.
        self.attack_dist = attack_dist
        # there can be up to two instances of a piece on the board. If these values
        # are negative ones, it will be ignored when setting up the board.
        self.start_pos = start_pos
        # Max distance a piece can move
        self.movement_dist = movement_dist
        # Some pieces must move the whole distance
        self.dist_increment = dist_increment
        self.current_pos = self.start_pos
        self.alias_id = alias_id
        # set starting space as being occupied with piece
        spaces[start_pos] = alias_id


class Far(Piece):
    # These are versatile movement pieces that cannot attack unless attack distance is 2.
    def __init__(self, start_pos, alias_id):
        super().__init__("Bent", 2, start_pos, 2, 1, alias_id)


class Rider(Piece):
    # These pieces can move in any direction up to two spaces. When attacking, the attack distance
    # must be 2 (pierce).
    def __init__(self, start_pos, alias_id):
        super().__init__("Uni", 2, start_pos, 2, 1, alias_id)


class Barricade(Piece):
    # These pieces must be attached by two pieces during the same turn to be destroyed.
    # It can only be moved one space at a time in cardinal directions and cannot attack.
    def __init__(self, start_pos, alias_id):
        super().__init__("Cardinal", 0, start_pos, 1, 1, alias_id)


class FootSoldier(Piece):
    # The footsoldier is a simple, short movement piece that can attack at 1 distance.
    def __init__(self, start_pos, alias_id):
        super().__init__("Bent", 1, start_pos, 1, 1, alias_id)


class Ninja(Piece):
    # The ninja can bypass barricade (but cannot attack it). It can attack at 2 or less distance.
    # Normal movement is one tile at a time.
    def __init__(self, start_pos, alias_id):
        super().__init__("Uni", -2, start_pos, 1, 1, alias_id)


class Spinner(Piece):
    # The spinner can be spun in any direction and can charge direction types only when hitting a boundary.
    # It can attack at 3 or less distance, but any further and it simply gets stopped by anything else
    # that was 4 or more distance away.
    def __init__(self, start_pos, alias_id):
        super().__init__("Bent-Edge", -3, start_pos, 5, 5, alias_id)


class Wraith(Piece):
    # Your pieces can go through a wraith. Opponents cannot pass through a wraith and "stop short".
    # If a piece is stopped short because of wraith, wraith cannot attack the next turn.
    def __init__(self, start_pos, alias_id):
        super().__init__("Uni", -2, start_pos, 2, 1, alias_id)


class Brave(Piece):
    # The brave must attack from three distance and has
    # the ability martyr. Martyr is triggered when the brave is killed.
    # Martyr: If the divinity is still alive, it transforms into a spinner.
    # A wraith is created where the brave died.
    def __init__(self, start_pos, alias_id):
        super().__init__("Uni", 3, start_pos, 3, 1, alias_id)


class Divinity(Piece):
    # The divinity has 2 regular movement of forced direction.
    # However, it attacks from exactly four distance away.
    def __init__(self, start_pos, alias_id):
        super().__init__("Uni", 4, start_pos, 2, 2, alias_id)


class Game:

    def __init__(self, mode):
        # This var will be set to false any time a start condition is not met.
        # The status val will be checked after instantiation, and if it is False,
        # the instance will be deleted and the process restarted.
        self.status = True

        self.mode = mode

        if self.mode == "GreyVCom" or mode == "GreyVRed":
            self.p1color = "Grey"
            self.p2color = "Red"
        elif self.mode == "RedVCom" or mode == "RedVGrey":
            self.p1color = "Red"
            self.p2color = "Grey"
        else:
            print("Mode not selected.")
            self.status = False

    # Dice function that determines who goes first.
    @staticmethod
    def generate_die_val():
        seed(3)
        value = randint(1, 6)
        return value

    def attack(self, obj_piece, selected_space):
        pass

    def move(self, obj_piece, selected_space):
        pass
