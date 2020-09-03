import pygame
import sys
import time

pygame.init()

size = width, height = 900, 900
brown, white, black = [75, 24, 0], [210, 210, 210], [30, 30, 30]
selected_white, selected_black = [237, 237, 195], [143, 143, 69]
circcolor = [230, 230, 90]
screen = pygame.display.set_mode(size)
bg = pygame.image.load("BG.png")
bg_rect = bg.get_rect()
screen.blit(bg, bg_rect)



class Piece:
    def __init__(self, name, pos, strength, side):
        self.name = name
        self.pos = pos
        self.strength = strength
        self.side = side
        self.poss_moves = []
        self.alive = True
        self.firstmove = True


W = []
for i in range(0, 8):
    W.append(Piece("Pawn", [1, i], 1, "White"))
W.extend([Piece("Rook", [0, 0], 5, "White"), Piece("Knight", [0, 1], 3, "White"), Piece("Bishop", [0, 2], 3, "White")])
W.extend([Piece("Queen", [0, 3], 8, "White"), Piece("King", [0, 4], 9, "White"), Piece("Bishop", [0, 5], 3, "White")])
W.extend([Piece("Knight", [0, 6], 3, "White"), Piece("Rook", [0, 7], 5, "White")])

B = []
for i in range(0, 8):
    B.append(Piece("Pawn", [6, i], 1, "Black"))
B.extend([Piece("Rook", [7, 0], 5, "Black"), Piece("Knight", [7, 1], 3, "Black"), Piece("Bishop", [7, 2], 3, "Black")])
B.extend([Piece("Queen", [7, 3], 8, "Black"), Piece("King", [7, 4], 9, "Black"), Piece("Bishop", [7, 5], 3, "Black")])
B.extend([Piece("Knight", [7, 6], 3, "Black"), Piece("Rook", [7, 7], 5, "Black")])


class GridClass:
    def __init__(self, occupied, cpiece):
        self.occupied = occupied
        self.cpiece = cpiece


grid = []
temp = []
for i in range(0, 8):
    temp = []
    for j in range(0, 8):
        temp.append(GridClass(0, None))
    grid.append(temp)

for i in range(0, 8):
    grid[1][i].cpiece = W[i]
    grid[1][i].occupied = 1
    grid[0][i].cpiece = W[i + 8]
    grid[0][i].occupied = 1
    grid[6][i].cpiece = B[i]
    grid[6][i].occupied = 1
    grid[7][i].cpiece = B[i + 8]
    grid[7][i].occupied = 1


def update_valid_moves(piece):

    if piece.name == "Pawn":
        piece.poss_moves.clear()
        if piece.side == "White":
            if piece.pos[0] + 1 <= 7:
                if grid[piece.pos[0] + 1][piece.pos[1]].occupied == 0:
                    piece.poss_moves.append([piece.pos[0] + 1, piece.pos[1]])
                if piece.firstmove is True:
                    if grid[piece.pos[0] + 2][piece.pos[1]].occupied == 0 and piece.pos[0] + 2 <= 7:
                        piece.poss_moves.append([piece.pos[0] + 2, piece.pos[1]])
                if piece.pos[1] + 1 <= 7:
                    if grid[piece.pos[0] + 1][piece.pos[1] + 1].occupied == 1 \
                            and grid[piece.pos[0] + 1][piece.pos[1] + 1].cpiece.side != piece.side:
                        piece.poss_moves.append([piece.pos[0] + 1, piece.pos[1] + 1])
                if piece.pos[1] - 1 >= 0:
                    if grid[piece.pos[0] + 1][piece.pos[1] - 1].occupied == 1 \
                            and grid[piece.pos[0] + 1][piece.pos[1] - 1].cpiece.side != piece.side:
                        piece.poss_moves.append([piece.pos[0] + 1, piece.pos[1] - 1])
        else:
            if piece.pos[0] - 1 >= 0:
                if grid[piece.pos[0] - 1][piece.pos[1]].occupied == 0:
                    piece.poss_moves.append([piece.pos[0] - 1, piece.pos[1]])
                if piece.firstmove is True:
                    if grid[piece.pos[0] - 2][piece.pos[1]].occupied == 0 and piece.pos[0] - 2 <= 7:
                        piece.poss_moves.append([piece.pos[0] - 2, piece.pos[1]])
                if piece.pos[1] + 1 <= 7:
                    if grid[piece.pos[0] - 1][piece.pos[1] + 1].occupied == 1 \
                            and grid[piece.pos[0] - 1][piece.pos[1] + 1].cpiece.side != piece.side:
                        piece.poss_moves.append([piece.pos[0] - 1, piece.pos[1] + 1])
                if piece.pos[1] - 1 >= 0:
                    if grid[piece.pos[0] - 1][piece.pos[1] - 1].occupied == 1 \
                            and grid[piece.pos[0] - 1][piece.pos[1] - 1].cpiece.side != piece.side:
                        piece.poss_moves.append([piece.pos[0] - 1, piece.pos[1] - 1])

    elif piece.name == "Rook":
        piece.poss_moves.clear()

        i = 1
        while piece.pos[0] + i <= 7:
            if grid[piece.pos[0] + i][piece.pos[1]].occupied == 0:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1]])
                i = i + 1
            elif grid[piece.pos[0] + i][piece.pos[1]].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1]])
                break
            else:
                break

        i = 1
        while piece.pos[0] - i >= 0:
            if grid[piece.pos[0] - i][piece.pos[1]].occupied == 0:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1]])
                i = i + 1
            elif grid[piece.pos[0] - i][piece.pos[1]].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1]])
                break
            else:
                break

        i = 1
        while piece.pos[1] + i <= 7:
            if grid[piece.pos[0]][piece.pos[1] + i].occupied == 0:
                piece.poss_moves.append([piece.pos[0], piece.pos[1] + i])
                i = i + 1
            elif grid[piece.pos[0]][piece.pos[1] + i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0], piece.pos[1] + i])
                break
            else:
                break

        i = 1
        while piece.pos[1] - i >= 0:
            if grid[piece.pos[0]][piece.pos[1] - i].occupied == 0:
                piece.poss_moves.append([piece.pos[0], piece.pos[1] - i])
                i = i + 1
            elif grid[piece.pos[0]][piece.pos[1] - i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0], piece.pos[1] - i])
                break
            else:
                break

    elif piece.name == "Knight":
        piece.poss_moves.clear()

        if piece.pos[0] + 2 <= 7 and piece.pos[1] + 1 <= 7:
            if grid[piece.pos[0] + 2][piece.pos[1] + 1].occupied == 0:
                piece.poss_moves.append([piece.pos[0] + 2, piece.pos[1] + 1])
            elif grid[piece.pos[0] + 2][piece.pos[1] + 1].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] + 2, piece.pos[1] + 1])

        if piece.pos[0] + 1 <= 7 and piece.pos[1] + 2 <= 7:
            if grid[piece.pos[0] + 1][piece.pos[1] + 2].occupied == 0:
                piece.poss_moves.append([piece.pos[0] + 1, piece.pos[1] + 2])
            elif grid[piece.pos[0] + 1][piece.pos[1] + 2].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] + 1, piece.pos[1] + 2])

        if piece.pos[0] - 2 >= 0 and piece.pos[1] - 1 >= 0:
            if grid[piece.pos[0] - 2][piece.pos[1] - 1].occupied == 0:
                piece.poss_moves.append([piece.pos[0] - 2, piece.pos[1] - 1])
            elif grid[piece.pos[0] - 2][piece.pos[1] - 1].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] - 2, piece.pos[1] - 1])

        if piece.pos[0] - 1 >= 0 and piece.pos[1] - 2 >= 0:
            if grid[piece.pos[0] - 1][piece.pos[1] - 2].occupied == 0:
                piece.poss_moves.append([piece.pos[0] - 1, piece.pos[1] - 2])
            elif grid[piece.pos[0] - 1][piece.pos[1] - 2].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] - 1, piece.pos[1] - 2])

        if piece.pos[0] + 2 <= 7 and piece.pos[1] - 1 >= 0:
            if grid[piece.pos[0] + 2][piece.pos[1] - 1].occupied == 0:
                piece.poss_moves.append([piece.pos[0] + 2, piece.pos[1] - 1])
            elif grid[piece.pos[0] + 2][piece.pos[1] - 1].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] + 2, piece.pos[1] - 1])

        if piece.pos[0] + 1 <= 7 and piece.pos[1] - 2 >= 0:
            if grid[piece.pos[0] + 1][piece.pos[1] - 2].occupied == 0:
                piece.poss_moves.append([piece.pos[0] + 1, piece.pos[1] - 2])
            elif grid[piece.pos[0] + 1][piece.pos[1] - 2].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] + 1, piece.pos[1] - 2])

        if piece.pos[0] - 2 >= 0 and piece.pos[1] + 1 <= 7:
            if grid[piece.pos[0] - 2][piece.pos[1] + 1].occupied == 0:
                piece.poss_moves.append([piece.pos[0] - 2, piece.pos[1] + 1])
            elif grid[piece.pos[0] - 2][piece.pos[1] + 1].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] - 2, piece.pos[1] + 1])

        if piece.pos[0] - 1 >= 0 and piece.pos[1] + 2 <= 7:
            if grid[piece.pos[0] - 1][piece.pos[1] + 2].occupied == 0:
                piece.poss_moves.append([piece.pos[0] - 1, piece.pos[1] + 2])
            elif grid[piece.pos[0] - 1][piece.pos[1] + 2].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] - 1, piece.pos[1] + 2])

    elif piece.name == "Bishop":
        piece.poss_moves.clear()

        i = 1
        while piece.pos[0] + i <= 7 and piece.pos[1] + i <= 7:
            if grid[piece.pos[0] + i][piece.pos[1] + i].occupied == 0:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1] + i])
                i = i + 1
            elif grid[piece.pos[0] + i][piece.pos[1] + i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1] + i])
                break
            else:
                break
        i = 1
        while piece.pos[0] - i >= 0 and piece.pos[1] - i >= 0:
            if grid[piece.pos[0] - i][piece.pos[1] - i].occupied == 0:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1] - i])
                i = i + 1
            elif grid[piece.pos[0] - i][piece.pos[1] - i].occupied == 1 \
                    and grid[piece.pos[0] - i][piece.pos[1] - i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1] - i])
                break
            else:
                break
        i = 1
        while piece.pos[0] + i <= 7 and piece.pos[1] - i >= 0:
            if grid[piece.pos[0] + i][piece.pos[1] - i].occupied == 0:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1] - i])
                i = i + 1
            elif grid[piece.pos[0] + i][piece.pos[1] - i].occupied == 1 \
                    and grid[piece.pos[0] + i][piece.pos[1] - i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1] - i])
                break
            else:
                break
        i = 1
        while piece.pos[0] - i >= 0 and piece.pos[1] + i <= 7:
            if grid[piece.pos[0] - i][piece.pos[1] + i].occupied == 0:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1] + i])
                i = i + 1
            elif grid[piece.pos[0] - i][piece.pos[1] + i].occupied == 1 \
                    and grid[piece.pos[0] - i][piece.pos[1] + i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1] + i])
                break
            else:
                break

    elif piece.name == "Queen":
        piece.poss_moves.clear()

        i = 1
        while piece.pos[0] + i <= 7:
            if grid[piece.pos[0] + i][piece.pos[1]].occupied == 0:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1]])
                i = i + 1
            elif grid[piece.pos[0] + i][piece.pos[1]].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1]])
                break
            else:
                break

        i = 1
        while piece.pos[0] - i >= 0:
            if grid[piece.pos[0] - i][piece.pos[1]].occupied == 0:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1]])
                i = i + 1
            elif grid[piece.pos[0] - i][piece.pos[1]].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1]])
                break
            else:
                break

        i = 1
        while piece.pos[1] + i <= 7:
            if grid[piece.pos[0]][piece.pos[1] + i].occupied == 0:
                piece.poss_moves.append([piece.pos[0], piece.pos[1] + i])
                i = i + 1
            elif grid[piece.pos[0]][piece.pos[1] + i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0], piece.pos[1] + i])
                break
            else:
                break

        i = 1
        while piece.pos[1] - i >= 0:
            if grid[piece.pos[0]][piece.pos[1] - i].occupied == 0:
                piece.poss_moves.append([piece.pos[0], piece.pos[1] - i])
                i = i + 1
            elif grid[piece.pos[0]][piece.pos[1] - i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0], piece.pos[1] - i])
                break
            else:
                break

        i = 1
        while piece.pos[0] + i <= 7 and piece.pos[1] + i <= 7:
            if grid[piece.pos[0] + i][piece.pos[1] + i].occupied == 0:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1] + i])
                i = i + 1
            elif grid[piece.pos[0] + i][piece.pos[1] + i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1] + i])
                break
            else:
                break
        i = 1
        while piece.pos[0] - i >= 0 and piece.pos[1] - i >= 0:
            if grid[piece.pos[0] - i][piece.pos[1] - i].occupied == 0:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1] - i])
                i = i + 1
            elif grid[piece.pos[0] - i][piece.pos[1] - i].occupied == 1 \
                    and grid[piece.pos[0] - i][piece.pos[1] - i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1] - i])
                break
            else:
                break
        i = 1
        while piece.pos[0] + i <= 7 and piece.pos[1] - i >= 0:
            if grid[piece.pos[0] + i][piece.pos[1] - i].occupied == 0:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1] - i])
                i = i + 1
            elif grid[piece.pos[0] + i][piece.pos[1] - i].occupied == 1 \
                    and grid[piece.pos[0] + i][piece.pos[1] - i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] + i, piece.pos[1] - i])
                break
            else:
                break
        i = 1
        while piece.pos[0] - i >= 0 and piece.pos[1] + i <= 7:
            if grid[piece.pos[0] - i][piece.pos[1] + i].occupied == 0:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1] + i])
                i = i + 1
            elif grid[piece.pos[0] - i][piece.pos[1] + i].occupied == 1 \
                    and grid[piece.pos[0] - i][piece.pos[1] + i].cpiece.side != piece.side:
                piece.poss_moves.append([piece.pos[0] - i, piece.pos[1] + i])
                break
            else:
                break

    elif piece.name == "King":
        piece.poss_moves.clear()
        if piece.side == "White":
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if 7 >= piece.pos[0] + j >= 0 and 7 >= piece.pos[1] + k >= 0:
                        invalid = False
                        if grid[piece.pos[0] + j][piece.pos[1] + k].occupied == 0:
                            for element in B:
                                if [piece.pos[0] + j, piece.pos[1] + k] in element.poss_moves \
                                        and element.name != "Pawn" and element.alive is True:
                                    invalid = True
                                if element.name == "Pawn" and element.alive is True:
                                    if [element.pos[0] - 1, element.pos[1] + 1] == [piece.pos[0] + j,
                                                                                    piece.pos[1] + k]:
                                        invalid = True
                                    elif [element.pos[0] - 1, element.pos[1] - 1] == [piece.pos[0] + j,
                                                                                      piece.pos[1] + k]:
                                        invalid = True
                            if invalid is False:
                                piece.poss_moves.append([piece.pos[0] + j, piece.pos[1] + k])

        elif piece.side == "Black":
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if 7 >= piece.pos[0] + j >= 0 and 7 >= piece.pos[1] + k >= 0 and j != 1 and k != 1:
                        invalid = False
                        if grid[piece.pos[0] + j][piece.pos[1] + k].occupied == 0:
                            for element in W:
                                if [piece.pos[0] + j, piece.pos[1] + k] in element.poss_moves \
                                        and element.name != "Pawn" and element.alive is True:
                                    invalid = True
                                if element.name == "Pawn" and element.alive is True:
                                    if [element.pos[0] + 1, element.pos[1] + 1] == [piece.pos[0] + j,
                                                                                    piece.pos[1] + k]:
                                        invalid = True
                                    elif [element.pos[0] + 1, element.pos[1] - 1] == [piece.pos[0] + j,
                                                                                      piece.pos[1] + k]:
                                        invalid = True
                            if invalid is False:
                                piece.poss_moves.append([piece.pos[0] + j, piece.pos[1] + k])


for i in B:
    update_valid_moves(i)
    print(i.side + " " + i.name + ": ", end="")
    print(i.poss_moves)

for i in W:
    update_valid_moves(i)
    print(i.side + " " + i.name + ": ", end="")
    print(i.poss_moves)

side = True
active = None


def movepiece(piece, dest_pos):
    if grid[dest_pos[0]][dest_pos[1]].occupied == 1:
        grid[dest_pos[0]][dest_pos[1]].cpiece.alive = False
    grid[piece.pos[0]][piece.pos[1]].occupied = 0
    grid[piece.pos[0]][piece.pos[1]].cpiece = None
    grid[dest_pos[0]][dest_pos[1]].occupied = 1
    grid[dest_pos[0]][dest_pos[1]].cpiece = piece
    piece.pos[0] = dest_pos[0]
    piece.pos[1] = dest_pos[1]
    piece.firstmove = False
    print(piece.side + piece.name)
    print(piece.pos)


def checkforinvalid():

    global side

    if side is True:
        for piece in W:
            if piece.alive is True and piece.name != "King":
                original_position = piece.pos.copy()
                original_possibilities = piece.poss_moves.copy()
                new_poss_moves = []
                for moves in original_possibilities:
                    grid[piece.pos[0]][piece.pos[1]].occupied = 0
                    grid[piece.pos[0]][piece.pos[1]].cpiece = None
                    piece.pos = moves.copy()
                    grid[piece.pos[0]][piece.pos[1]].occupied = 1
                    grid[piece.pos[0]][piece.pos[1]].cpiece = piece
                    invalid = False
                    for checker in B:
                        if piece.name == "Queen" or piece.name == "Rook" or piece.name == "Bishop" \
                                and piece.alive is True:
                            update_valid_moves(checker)
                            if W[12].pos in checker.poss_moves:
                                invalid = True
                                break;
                    if invalid is False:
                        new_poss_moves.extend([moves])
                grid[piece.pos[0]][piece.pos[1]].occupied = 0
                grid[piece.pos[0]][piece.pos[1]].cpiece = None
                piece.pos = original_position.copy()
                grid[piece.pos[0]][piece.pos[1]].occupied = 1
                grid[piece.pos[0]][piece.pos[1]].cpiece = piece
                piece.poss_moves = new_poss_moves.copy()

    else:
        for piece in B:
            if piece.alive is True and piece.name != "King":
                original_position = piece.pos.copy()
                original_possibilities = piece.poss_moves.copy()
                new_poss_moves = []
                for moves in original_possibilities:
                    grid[piece.pos[0]][piece.pos[1]].occupied = 0
                    grid[piece.pos[0]][piece.pos[1]].cpiece = None
                    piece.pos = moves.copy()
                    grid[piece.pos[0]][piece.pos[1]].occupied = 1
                    grid[piece.pos[0]][piece.pos[1]].cpiece = piece
                    invalid = False
                    for checker in W:
                        if piece.name == "Queen" or piece.name == "Rook" or piece.name == "Bishop" \
                                and piece.alive is True:
                            update_valid_moves(checker)
                            if B[12].pos in checker.poss_moves:
                                invalid = True
                                break;
                    if invalid is False:
                        new_poss_moves.extend([moves])
                grid[piece.pos[0]][piece.pos[1]].occupied = 0
                grid[piece.pos[0]][piece.pos[1]].cpiece = None
                piece.pos = original_position.copy()
                grid[piece.pos[0]][piece.pos[1]].occupied = 1
                grid[piece.pos[0]][piece.pos[1]].cpiece = piece
                piece.poss_moves = new_poss_moves.copy()


def display(piece):
    for m in range(0, 8):
        for n in range(0, 8):
            if piece is None:
                if (m + n) % 2 == 0:
                    pygame.draw.rect(screen, white, ((n * 100) + 50, (m * 100) + 50, 100, 100))
                else:
                    pygame.draw.rect(screen, black, ((n * 100) + 50, (m * 100) + 50, 100, 100))
                if grid[7 - m][n].occupied == 1:
                    img_loader = grid[7 - m][n].cpiece.side + grid[7 - m][n].cpiece.name + ".png"
                    current_piece = pygame.image.load(img_loader)
                    current_piece_rect = ((n * 100) + 50, (m * 100) + 50, 100, 100)
                    screen.blit(current_piece, current_piece_rect)
            else:
                if [7-m, n] == piece.pos:
                    if (m + n) % 2 == 0:
                        pygame.draw.rect(screen, selected_white, ((n * 100) + 50, (m * 100) + 50, 100, 100))
                    else:
                        pygame.draw.rect(screen, selected_black, ((n * 100) + 50, (m * 100) + 50, 100, 100))
                else:
                    if (m + n) % 2 == 0:
                        pygame.draw.rect(screen, white, ((n * 100) + 50, (m * 100) + 50, 100, 100))
                    else:
                        pygame.draw.rect(screen, black, ((n * 100) + 50, (m * 100) + 50, 100, 100))
                if grid[7-m][n].occupied == 1:
                    img_loader = grid[7 - m][n].cpiece.side + grid[7 - m][n].cpiece.name + ".png"
                    current_piece = pygame.image.load(img_loader)
                    current_piece_rect = ((n * 100) + 50, (m * 100) + 50, 100, 100)
                    screen.blit(current_piece, current_piece_rect)
                if [7-m, n] in piece.poss_moves:
                    pygame.draw.circle(screen, circcolor, ((n * 100) + 100, (m * 100) + 100), 10)
                    pygame.draw.circle(screen, [0, 0, 0], ((n * 100) + 100, (m * 100) + 100), 12, 2)
    pygame.display.flip()
    for i in reversed(range(8)):
        for j in range(8):
            print(grid[i][j].occupied, end="")
            print(" ", end="")
        print()
    for k in W:
        print(k.side + k.name + ": ", end="")
        print(k.poss_moves)


def main_game():

    global active
    global side
    click = [0, 0, 0]
    display(None)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # click = pygame.mouse.get_pressed()
        #
        # if click[0] == 1:
        #     mpos = pygame.mouse.get_pos()
        #     clicked_piece = [7 - int((mpos[1] - 50)/100), int((mpos[0] - 50)/100)]
        #
        #     if active is None:
        #         if grid[clicked_piece[0]][clicked_piece[1]].occupied == 1:
        #             if side is True and grid[clicked_piece[0]][clicked_piece[1]].cpiece.side == "White" \
        #                     and grid[clicked_piece[0]][clicked_piece[1]].cpiece.alive is True:
        #                 active[0] = True
        #                 active[1] = grid[clicked_piece[0]][clicked_piece[1]].cpiece
        #                 display(grid[clicked_piece[0]][clicked_piece[1]].cpiece)
        #             elif side is False and grid[clicked_piece[0]][clicked_piece[1]].cpiece.side == "Black" \
        #                     and grid[clicked_piece[0]][clicked_piece[1]].cpiece.alive is True:
        #                 active[0] = True
        #                 active[1] = grid[clicked_piece[0]][clicked_piece[1]].cpiece
        #                 display(grid[clicked_piece[0]][clicked_piece[1]].cpiece)
        #
        #     elif active[0] is True:
        #         if clicked_piece in active[1].poss_moves:
        #             print("Code Worked!!!")
        #             print()
        #             movepiece(active[1], clicked_piece)
        #             active = None
        #             display(None)
        #         elif grid[clicked_piece[0]][clicked_piece[1]].occupied == 1:
        #             if side is True and grid[clicked_piece[0]][clicked_piece[1]].cpiece.side == "White" \
        #                     and grid[clicked_piece[0]][clicked_piece[1]].cpiece.alive is True:
        #                 active[0] = True
        #                 active[1] = grid[clicked_piece[0]][clicked_piece[1]].cpiece
        #                 display(grid[clicked_piece[0]][clicked_piece[1]].cpiece)
        #             elif side is False and grid[clicked_piece[0]][clicked_piece[1]].cpiece.side == "Black" \
        #                     and grid[clicked_piece[0]][clicked_piece[1]].cpiece.alive is True:
        #                 active[0] = True
        #                 active[1] = grid[clicked_piece[0]][clicked_piece[1]].cpiece
        #                 display(grid[clicked_piece[0]][clicked_piece[1]].cpiece)

        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            mpos = pygame.mouse.get_pos()
            clicked_piece = [7 - int((mpos[1] - 50) / 100), int((mpos[0] - 50) / 100)]
            if active is None:
                if grid[clicked_piece[0]][clicked_piece[1]].occupied == 1:
                    if grid[clicked_piece[0]][clicked_piece[1]].cpiece.side == "White" and side is True:
                        active = grid[clicked_piece[0]][clicked_piece[1]].cpiece
                        display(active)
                    elif grid[clicked_piece[0]][clicked_piece[1]].cpiece.side == "Black" and side is False:
                        active = grid[clicked_piece[0]][clicked_piece[1]].cpiece
                        display(active)
            elif active is not None:
                if [clicked_piece[0], clicked_piece[1]] in active.poss_moves:
                    movepiece(active, [clicked_piece[0], clicked_piece[1]])
                    display(None)
                    active = None
                    side = not side
                    for i in B:
                        update_valid_moves(i)
                        print(i.side + " " + i.name + ": ", end="")
                        print(i.poss_moves)

                    for i in W:
                        update_valid_moves(i)
                        print(i.side + " " + i.name + ": ", end="")
                        print(i.poss_moves)

                elif grid[clicked_piece[0]][clicked_piece[1]].occupied == 1:
                    if grid[clicked_piece[0]][clicked_piece[1]].cpiece.side == "White" and side is True:
                        active = grid[clicked_piece[0]][clicked_piece[1]].cpiece
                        display(active)
                    elif grid[clicked_piece[0]][clicked_piece[1]].cpiece.side == "Black" and side is False:
                        active = grid[clicked_piece[0]][clicked_piece[1]].cpiece
                        display(active)

main_game()
