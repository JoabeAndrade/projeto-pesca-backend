from django.core.exceptions import ValidationError

def only_numeric_chars(value):
    if not value.isnumeric():
        raise ValidationError("The value inserted is not a numeric string")
