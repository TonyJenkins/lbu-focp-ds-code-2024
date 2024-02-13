#!/usr/bin/env python3

from statistics import mean

if __name__ == '__main__':

    NUMBER_OF_MARKS = 5

    marks = []

    for mark in range(NUMBER_OF_MARKS):
        while True:
            try:
                next_mark = int(input(f'Enter Mark #{mark + 1}: '))
                if 0 <= next_mark <= 100:
                    marks.append(next_mark)
                    break
                else:
                    print('Mark must be between 0 and 100')
            except ValueError:
                print('Please enter an integer!')

    highest = max(marks)
    lowest = min(marks)
    average = mean(marks)

    print()

    print(f'Highest Mark: {highest}')
    print(f'Lowest Mark:  {lowest}')
    print(f'Average Mark: {average}')
