#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def relativeLocation(queenX, queenY, pawnX, pawnY):
    if pawnY == queenY and pawnX < queenX:
        return 'L'
    if pawnY == queenY and pawnX > queenX:
        return 'R'
    if pawnY > queenY and pawnX == queenX:
        return 'U'
    if pawnY < queenY and pawnX == queenX:
        return 'D'
    if abs(queenX - pawnX) == abs(queenY - pawnY):
        if pawnY > queenY and pawnX < queenX:
            return 'UL'
        if pawnY > queenY and pawnX > queenX:
            return 'UR'
        if pawnY < queenY and pawnX > queenX:
            return 'DR'
        if pawnY < queenY and pawnX < queenX:
            return 'DL'
    
def cellBlockedByPawns(queenX, queenY, pawns):
    blockedCells = set()
    for pawn in pawns:
        x = pawn[1]
        y = pawn[0]
        
        position = relativeLocation(queenX, queenY, x, y)
        
        if position == 'U':
            for i in range(y, n+1):
                blockedCells.add((i, x))
        if position == 'D':
            for i in range(y, 0, -1):
                blockedCells.add((i, x))
        if position == 'L':
            for i in range(x, 0 , -1):
                blockedCells.add((y, i))
        if position == 'R':
            for i in range(x, n+1):
                blockedCells.add((y, i))
        if position == 'UL':
            while y <= n and x > 0:
                blockedCells.add((y, x))
                x -= 1
                y += 1
        if position == 'UR':
            while y <= n and x <= n:
                blockedCells.add((y, x))
                x += 1
                y += 1
        if position == 'DR':
            while y > 0 and x <= n:
                blockedCells.add((y, x))
                y -= 1
                x += 1
        if position == 'DL':
            while y > 0 and x > 0:
                blockedCells.add((y, x))
                y -= 1
                x -= 1
    return len(blockedCells)
        
        
        
def cellsQueencanAttack(queenX, queenY, boardSize):
    orthogonals = 2 * boardSize - 2
    diagonals = 2 * boardSize - 2 - abs(queenX - queenY) - abs(queenX + queenY - boardSize - 1)
    return orthogonals + diagonals

    
def queensAttack(boardSize, k, queenY, queenX, pawns):
    # Write your code here
    queenCells = cellsQueencanAttack(queenX, queenY, boardSize)
    if len(pawns) == 0:
        return queenCells
    else:
        pawnCells = cellBlockedByPawns(queenX, queenY, pawns)
        return queenCells - pawnCells

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
