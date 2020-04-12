"""Main engine for brain games."""

from brain_games.cli import user_answers, welcome_user

wrong_tmpl = """
"{0}" is wrong answer ;(. Correct answer is "{1}".
Let`s try again, {2}!"""


def game(generate, check):
    """Template for brain game engine."""
    user_name = welcome_user()
    wins = 0
    while wins < 3:
        question = generate()
        print('Question: {0}'.format(question))
        answer = user_answers('Your answer: ')
        true_answer = check(question)
        if answer == true_answer:
            print('Correct!')
            wins += 1
        else:
            print(wrong_tmpl.format(answer, true_answer, user_name))
            break
    if wins == 3:
        print('Congratulations!')
