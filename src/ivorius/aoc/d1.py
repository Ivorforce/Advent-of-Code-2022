from pathlib import Path
calories_str = (Path(__file__).parent / Path("input.txt")).read_text()

calories_per_elf = []
current_elf_calories = 0

for line in calories_str.split("\n"):
    if not line:
        if current_elf_calories > 0:
            calories_per_elf.append(current_elf_calories)
            current_elf_calories = 0
        continue

    current_elf_calories += int(line)

print(sum(sorted(calories_per_elf, reverse=True)[:3]))
