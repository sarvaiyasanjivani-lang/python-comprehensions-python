languages = ["Python", "C++", "Java"]

numbered_languages = [
    f"{index}. {language}"
    for index, language in enumerate(languages, start=2)
]

print(numbered_languages)
