"""Main engine for brain games."""

from brain_games.cli import ask, welcome_user

WRONG_SAMPLE = """
"{0}" is wrong answer ;(. Correct answer is "{1}".
Let`s try again, {2}!"""


def run(module, rounds=3):
    """Template for brain game engine."""
    print('Welcome to the Brain Games!')
    print(module.RULES)
    user_name = welcome_user()
    while rounds > 0:
        question, true_answer = module.game()
        print('Question: {0}'.format(question))
        answer = ask('Your answer: ')
        if answer != true_answer:
            print(WRONG_SAMPLE.format(answer, true_answer, user_name))
            break
        print('Correct!')
        rounds -= 1
    else:
        print('Congratulations!')
