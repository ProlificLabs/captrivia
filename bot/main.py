#!/usr/bin/env python

from captrivia import Captrivia

# Simple bot to play Captrivia.  Starts a new game, answers all of the questions, ends the game, and starts
# a new one.

# Assumes we're running Captrivia locally, or that it's running in Docker portmapped to the same 8080
# port.  The default `docker compose up` should do this correctly.
CAPTRIVIA_URL = "http://localhost:8080"

# Instantiate a Captrivia object to talk to the server
cap = Captrivia(CAPTRIVIA_URL)
game_count = 0

# Main infinite loop: Start a game, answer the questions, finish the game
while True:
    # Start a game
    cap.start_game()

    # Answer all of the questions
    questions = cap.get_questions()
    for question in questions:
        qid = question["id"]
        # For now we always choose the first answer.  This should probably
        # be changed!
        cap.answer_question(qid, 0)

    # End the game
    cap.end_game()

    # Do some logging so we can see how many answers we've given
    game_count += 1
    if game_count % 100 == 0:
        print("Played %d games" % (game_count))
