# Write a program that reads whith regex, from files "Руслан Манов" or "r.manov" or "R.Manov" or "Ruslan Manov" or "RUSLAN MANOV",
# or its variations and prints the first and last name in the format "First name: {first_name}, Last name: {last_name}".

import re

with open("test.txt", "r") as file:
    for line in file:
        match = re.search(
            r"\b[Р|М][а-я]\b{2,}\s\b[М|М][а-я]\b{2,}|\b[Р|М][а-я]\b{2,}\s\b[М|М][а-я]\b{2,}\s\b[М|М][а-я]\b{2,}",
            line,
        )
        if match:
            print(f"First name: {match.group(1)}, Last name: {match.group(2)}")
