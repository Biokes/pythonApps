import random

race = []
for tracks in range(70):
    race.append('-')


def get_race_circuit():
    return race
# tortoise1 = 0
# hare = 0
# race = []
# race2 = []
# for tracks in range(70):
#     race.append('-')
#     race2.append('-')
#
#
# def tortoise_move():
#     position = random.randrange(1, 10)
#     if 1 < position or position <= 5:
#         tortoise1 += 3
#     elif 6 <= position or position <= 7:
#         tortoise1 -= 6
#         if tortoise1 - 2 > 0:
#             tortoise1 -= 2
#         else:
#             tortoise1 = 0
#     elif 8 <= position or position <= 10:
#         tortoise1 += 1
#
#
# def hare_move(hare):
#     position = random.randrange(1, 10)
#     if 1 <= position or position <= 2:
#         hare += 0
#     elif 3 <= position or position <= 4:
#         hare += 9
#     elif position == 5:
#         hare -= 12
#         if hare - 12 > 0:
#             hare -= 2
#         else:
#             hare = 0
#     elif position >= 6 or position <= 8:
#         hare += 1
#     elif 9 <= position or position <= 10:
#         if hare - 2 > 0:
#             hare -= 2
#         else:
#             hare = 0
