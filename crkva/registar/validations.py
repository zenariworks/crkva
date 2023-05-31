# # validation of the input data

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError

# field validation
def check_value_uppercase(value: str) -> ValidationError:
    """check if value is all uppercase

    Params
    ------------
    value: str

    Return
    -----------
    ValidationError() if not uppercase
    """

    if value != value.upper():
        return ValidationError(f"This field needs to be in Uppercase")


def check_value_context(unit_code: str, value: float) -> ValidationError:
    """check if value is valid given the unit_code

    Params
    ------------
    value: float

    Return
    -----------
    ValidationError()
    """

    if unit_code == "P":
        if value > 200:
            return ValidationError(f"Percentage is more than 200")
    elif unit_code == "R":
        if value > 10:
            return ValidationError(f"Rapportcijfer is more than 10")
        elif value < 0:
            return ValidationError(f"Rapportcijfer is negative")


# model validation
def check_code_in_name(code: str, name: str) -> ValidationError:
    """check if code is containt in the name

    Params
    ------------
    dimension_code: str
        code from the dimension table
    name: str
        name of a table that needs to contain '_'code

    Return
    -----------
    ValidationError() if name doesn't contain '_'code
    """

    name_split = name.split("_")
    if code not in name_split:
        return ValidationError(f"This field needs to be containing _{code}")


def get_instance(model, field, row, column):
    try:
        instance = model.objects.get(**{f"{field}__iexact": row[column]})
        error = False
    except model.DoesNotExist:
        instance = None
        error = ObjectDoesNotExist(f"Provided {column}={row[column]} does not exist.")
    return (instance, error)
