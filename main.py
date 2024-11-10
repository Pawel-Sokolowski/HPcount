import re
with open("sorcerers_stone.txt", "r") as file:
    file_content = file.read()
    bad_chars = [';', ':', '!', "*", "?", ".", ",", "-", "'", '"']
    for char in bad_chars:
        file_content = file_content.replace(char, " ")

character_counts = {}
first_names = set()
with open("harry_potter_characters.txt", "r") as hp_char:
    characters = hp_char.read().splitlines()
    for character in characters:
        character = character.strip()
        character_counts[character] = file_content.count(character)
        first_name = character.split()[0]
        first_names.add(first_name)

for first_name in first_names:
    first_name_count = len(re.findall(r'\b' + re.escape(first_name) + r'\b', file_content))
    if first_name in character_counts:
        character_counts[first_name] += first_name_count
    else:
        character_counts[first_name] = first_name_count

for character, count in character_counts.items():
    print(f"{character}: {count}")