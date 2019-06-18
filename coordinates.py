import random
import numpy as np

def genURandPoint(lo, hi):
    return lo + random.random() * hi


def genURandLandscape(lo, hi, ptsNum):
    coords = [
            (genURandPoint(lo, hi), genURandPoint(lo, hi))
            for _ in range(10)
        ]
    return coords


if __name__ == "__main__":
    ptsNum = 100
    (lo, hi) = (0, 10)
    coords = genURandLandscape(lo, hi, ptsNum)
    print(coords) 
