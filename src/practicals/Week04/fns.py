#!/usr/bin/env python3


def validate_student_id(sid):
    try:
        return len(sid) == 7 and sid.startswith('c')
    except TypeError:
        raise TypeError('Student ID must be a string')


if __name__ == '__main__':
    print(validate_student_id('c123456'))
    print(validate_student_id('u7617271'))
    print(validate_student_id(''))
    print(validate_student_id(999))
