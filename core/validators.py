from django.forms import ValidationError


def validate_email(value):
    if not value.endswith('gmail.com'):
        raise ValidationError('Email must be Gmail!')