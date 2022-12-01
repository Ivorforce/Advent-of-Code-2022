calories_str = """
"""

calories_per_elf = []
current_elf_calories = 0

for line in calories_str.split("\n"):
    if not line:
        if current_elf_calories > 0:
            calories_per_elf.append(current_elf_calories)
            current_elf_calories = 0
        continue

    current_elf_calories += int(line)

print(max(calories_per_elf))
