from django.core import exceptions


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed!')

def validate_only_letters_and_spaces(value):
    for ch in value:
        if ch.isalpha() or ch.isspace():
            pass
        else:
            raise exceptions.ValidationError('Only letters are allowed!')
