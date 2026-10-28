text = "comprehensions"

unique_characters = {
    character.lower()
    for character in text
    if character.isalpha()
}

print(unique_characters)
