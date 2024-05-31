from typing import Any

from django.core.exceptions import ValidationError

from baserow.contrib.database.fields.constants import (
    BASEROW_BOOLEAN_FIELD_FALSE_VALUES,
    BASEROW_BOOLEAN_FIELD_TRUE_VALUES,
)
from baserow.core.utils import flatten


def ensure_boolean(value):
    """
    Ensures that the value is a boolean or converts it.

    @param value: The value to ensure as a boolean.
    @returns: The value as a boolean.
    """

    if value in BASEROW_BOOLEAN_FIELD_TRUE_VALUES:
        return True
    elif value in BASEROW_BOOLEAN_FIELD_FALSE_VALUES:
        return False

    raise ValidationError("Value is not a valid boolean or convertible to a boolean.")


def ensure_integer(value: Any) -> int:
    """
    Ensures that the value is an integer or can be converted to an integer.
    Raises a ValidationError if the value is not a valid integer or convertible to an
    integer.

    :param value: The value to ensure as an integer.
    :return: The value as an integer if conversion is successful.
    :raises ValidationError: If the value is not a valid integer or convertible to an
        integer.
    """

    try:
        return int(value)
    except (ValueError, TypeError) as exc:
        raise ValidationError(
            "The value must be an integer or convertible to an integer."
        ) from exc


def ensure_string(value, allow_empty=True):
    """
    Ensures that the value is a string or try to convert it.

    :param value: The value to ensure as a string.
    :param allow_empty: Whether we should throw an error if `value` is empty.
    :return: The value as a string.
    :raises ValueError: If not allow_empty and the `value` is empty.
    """

    if value is None or value == "" or value == []:
        if not allow_empty:
            raise ValidationError("A valid String is required.")
        return ""
    if isinstance(value, list):
        return ",".join(flatten(value))
    return str(value)


def ensure_array(value, allow_empty=True):
    """
    Ensure that the value is an array or try to convert it.
    Strings will be treated as comma separated values.
    Other data types will be transformed into a single element array.

    :param value: The value to ensure as an array.
    :param allow_empty: Whether we should raise an error if `value` is empty.
    :return: The value as an array.
    :rtype: list
    :raises ValueError: if not allow_empty and `value` is empty.
    """

    if value is None or value == "" or (isinstance(value, list) and not value):
        if not allow_empty:
            raise ValidationError("A non empty value is required.")
        return []

    if isinstance(value, list):
        return value

    if isinstance(value, str):
        return [item.strip() for item in value.split(",")]

    return [value]
