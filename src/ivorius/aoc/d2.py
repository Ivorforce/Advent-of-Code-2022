from pathlib import Path
input_str = (Path(__file__).parent / Path("d2-input.txt")).read_text(encoding="ascii")

score = 0


def compare(theirs, mine) -> int:
    return (mine - theirs + 1) % 3 - 1


def get_score(theirs, mine):
    return (mine + 1) + (compare(theirs, mine) + 1) * 3


def get_score_p1(theirs, mine):
    return get_score(theirs, mine)


def get_score_p2(theirs, outcome):
    mine = (theirs + outcome - 1) % 3
    return get_score(theirs, mine)


total_score = 0

for line in input_str.split("\n"):
    a = ord(line[0]) - ord("A")
    b = ord(line[2]) - ord("X")
    total_score += get_score_p2(a, b)

print(total_score)
