from pathlib import Path
input_str = (Path(__file__).parent / Path("d2-input.txt")).read_text(encoding="ascii")

score = 0


def compare(theirs, mine) -> int:
    return (mine - theirs + 1) % 3 - 1


def get_score(theirs, mine):
    return (mine + 1) + (compare(theirs, mine) + 1) * 3


total_score = 0

for line in input_str.split("\n"):
    theirs = ord(line[0]) - ord("A")
    mine = ord(line[2]) - ord("X")
    total_score += get_score(theirs, mine)

print(total_score)
