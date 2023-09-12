#!/usr/bin/env python3
from random import choice
from hashlib import sha256

with open('./questions.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    previous_questions = []
    try:
        while True:
            if len(previous_questions) == len(lines):
                selection = input(f"No more questions! Would you like to start again? (y/n): ").strip().lower()
                if selection == 'n':
                    break
                else:
                    previous_questions = []

            line = choice(lines)
            hashed = sha256(line.encode('utf-8')).hexdigest()

            while hashed in previous_questions:
                line = choice(lines)
                hashed = sha256(line.encode('utf-8')).hexdigest()

            previous_questions.append(hashed)

            remaining = len(lines) - len(previous_questions)
            print(line)

            user_input = input(f"Another one? (y/n/reset) {remaining} questions remaining: ").strip().lower()
            if user_input == 'reset':
                previous_questions = []
            if user_input == 'n':
                break
            print('')
        pass
    except KeyboardInterrupt:
        pass
