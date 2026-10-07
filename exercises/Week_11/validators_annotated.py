"""
example of a validator performing a validation check, and returning the value unchanged.
After Validator
"""
from typing import Annotated, Any
from pydantic import AfterValidator, BaseModel, ValidationError

def is_even(value : int) -> int:
    if value % 2 == 1:
        raise ValueError(f"{value} is not an even number")
    return value
"""
Note that it is important to return the validated value.
"""

class Model(BaseModel):
    number : Annotated[int, AfterValidator(is_even)]

try:
    Model(number = 1)
except ValidationError as err:
    print(err)
    """
    1 validation error for model number
    Value error, 1 is not an even number [type=value_Error, input_value=1, input_type=int]
    """
"""
Model(number=1)
      ↓
Pydantic checks:
Is 1 an int?
      ↓
Yes
      ↓
AfterValidator runs
      ↓
is_even(1)
      ↓
1 % 2 == 1
      ↓
raise ValueError("1 is not an even number")
      ↓
Pydantic converts that into ValidationError
      ↓
except ValidationError as err:
      ↓
print(err)
"""

"""
Here is an example of a validator making changes to the validated value (no exception is raised).
After Validator
"""
def double_number(value : int) -> int:
    return value * 2

class Model2(BaseModel):
    number : Annotated[int, AfterValidator(double_number)]

print(Model2(number=2))
#> output : 4

"""
below is the example of before Validator
"""
from pydantic import BeforeValidator

def ensure_list(value : Any) -> Any:
    """
    Notice the use of Any as a type hint for value. Before validators take the raw input, which can be anything.
    """
    if not isinstance(value, list):
        """
        Before validators give you more flexibility, but you have to account for every possible case.
        """
        return [value]
    else:
        return value

class Model3(BaseModel):
    numbers: Annotated[list[int], BeforeValidator(ensure_list)]

print(Model3(numbers=2))

try:
    Model3(numbers='str')
except ValidationError as err:
    print(err)
    """
    1 validation error for Model
    numbers.0
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='str', input_type=str]
    """
"""
Model3(numbers=2)
        ↓
BeforeValidator runs FIRST
        ↓
ensure_list(2)
        ↓
Is 2 already a list?
        ↓
No
        ↓
return [2]
        ↓
Now Pydantic does normal validation
        ↓
Is [2] a list[int]?
        ↓
Yes ✅
        ↓
Model created:
numbers=[2]
"""

"""
Below is the example of plain validators
"""
from pydantic import PlainValidator

def val_number(value : Any) -> Any:
    if isinstance(value, int):
        return value * 2
    else:
        return value

class Model4(BaseModel):
    number : Annotated[int, PlainValidator(val_number)]

print(Model4(number=4))
# output : 8

print(Model4(number='invalid'))
"""
Although 'invalid' shouldn't validate against the int type, Pydantic accepts the input.
"""
# output : invalid


"""
below is the example of wrap validators
"""
from pydantic import Field, ValidatorFunctionWrapHandler, WrapValidator

def truncate(value: Any, handler : ValidatorFunctionWrapHandler) -> str:
    try:
        """
        handler is a function that Pydantic gives to your validator. Think of it as:
        “Run Pydantic's normal validation on this value.”
        """
        return handler(value)
    except ValidationError as err:
        if err.errors()[0]['type'] == "string_too_long":
            return handler(value[:5])
        else:
            raise

class Model5(BaseModel):
    my_string :  Annotated[str, Field(max_length=5), WrapValidator(truncate)]

print(Model5(my_string='abcde'))
#output : 'abcde'
print(Model5(my_string='abcdef'))
# output: 'abcde'

"""
So when you call Model5(my_string="abcdef"), truncate() gets "abcdef" first. 
Inside it, handler(value) tries to validate "abcdef" against str with max_length=5. That fails and raises a ValidationError of type "string_too_long"
Then your except checks that error. If it is specifically string_too_long, you do: value[:5], so it will become "abcde"
Then you call: handler(value[:5]) again. This time Pydantic validates "abcde", it passes the max_length=5 rule, and "abcde" is returned.
"""


"""
multiple use of validator using Annotated- example
"""
def is_even2(value : int) -> int:
    if value % 2 == 1:
        raise ValueError(f'{value} is not an even number')
    return value

EvenNumber = Annotated[int, AfterValidator(is_even)]

class Model6(BaseModel):
    my_number = EvenNumber

class Model7(BaseModel):
    other_number : Annotated[EvenNumber, AfterValidator(lambda v: v + 2)]
    """
    lambda v: v + 2 is same as
    def add_two(v):
        return v + 2
    """

class Model8(BaseModel):
    list_of_even_numbers : list[EvenNumber]


"""
Below is the example of ordering of validators
"""
def runs_3rd():
    return "3rd"

def runs_4th():
    return "4th"

def runs_2nd():
    return "2nd"

def runs_1st():
    return "1st"

class Model(BaseModel):
    name: Annotated[
        str,
        AfterValidator(runs_3rd),
        AfterValidator(runs_4th),
        BeforeValidator(runs_2nd),
        WrapValidator(runs_1st),
    ]
"""
before and wrap validators are run from right to left, and after validators are then run from left to right
"""

