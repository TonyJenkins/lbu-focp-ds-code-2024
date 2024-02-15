#!/usr/bin/env python3


if __name__ == '__main__':

    NUMBER_OF_SCORES = 2

    margins = []

    for match in range(NUMBER_OF_SCORES):
        while True:
            try:
                result = input(f'Enter score of match #{match + 1}: ')

                home = int(result.split('-')[0])
                away = int(result.split('-')[1])
                margins.append(home - away)

                break

            except ValueError:
                print('Invalid Input. Try Again!')
            except IndexError:
                print('Invalid Input. Try Again!')

    biggest_win = max(margins)
    biggest_loss = abs(min(margins))
    goal_difference = sum(margins)

    print()
    print(f'Biggest Win:     {biggest_win:>3}.')
    print(f'Biggest Loss:    {biggest_loss:>3}.')
    print(f'Goal Difference: {goal_difference:>3}.')
