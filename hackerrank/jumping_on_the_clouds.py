# https://www.hackerrank.com/challenges/jumping-on-the-clouds


def jumpingOnClouds(clouds):
    i = 0
    jump_count = 0

    while i < len(clouds) - 1:
        if clouds[i] == 0 and (i + 2 < len(clouds)) and clouds[i + 2] == 0:
            i += 2
            jump_count += 1
        elif clouds[i] == 0 and clouds[i + 1] == 0:
            i += 1
            jump_count += 1
        else:
            i += 1

    return jump_count


actual = jumpingOnClouds(clouds=[0, 0, 1, 0, 0, 1, 0])
print(actual == 4)
