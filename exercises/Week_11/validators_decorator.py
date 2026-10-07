"""
example of a validator performing a validation check, and returning the value unchanged.
After Validator
"""
from pydantic import BaseModel, ValidationError, field_validator

class Model(BaseModel):
    number : int

    """
    'after' is the default mode for the decorator, and can be omitted.
    """
    @field_validator('number', mode='after')
    @classmethod
    def is_even(cls, value: int) -> int:
        """
        Because is_even() is marked with: classmethod, the first argument is conventionally called: cls
        """
        if value % 2 == 1:
            raise ValueError(f'{value} is not an even number')
        return value

try:
    Model(number=1)
except ValidationError as err:
    print(err)
"""
This version does the same validation idea, but instead of defining is_even() outside the model and attaching it with AfterValidator, 
you define the validator inside the Pydantic model using @field_validator.
"""
"""
1. Python defines the Model class
      ↓
2. Pydantic sees:
   number: int
      ↓
3. Pydantic also sees:
   @field_validator("number", mode="after")
      ↓
4. It registers is_even() as a validator for number
      ↓
5. Later you run:
   Model(number=1)
      ↓
6. Pydantic first checks:
   Is 1 a valid int?
      ↓
7. Yes
      ↓
8. Because mode="after",
   Pydantic now calls:
   is_even(cls, 1)
      ↓
9. 1 % 2 == 1
      ↓
10. raise ValueError("1 is not an even number")
      ↓
11. Pydantic converts that into ValidationError
      ↓
12. except ValidationError catches it
      ↓
13. print(err)
"""

"""
Here is an example of a validator making changes to the validated value (no exception is raised).
After Validator
"""

class Model2(BaseModel):
    number : int

    @field_validator('number', mode='after')  
    @classmethod
    def double_number(cls, value: int) -> int:
        return value * 2

print(Model2(number=2))

"""
below is the example of before Validator
"""
from typing import Any

class Model3(BaseModel):
    numbers : list[int]

    @field_validator('numbers' , mode='before')
    @classmethod
    def ensure_list(cls, value: Any) -> Any:
        if not isinstance(value, list):
            return[value]
        else:
            return value

print(Model3)

try:
    Model3(number='str')
except ValidationError as err:
    print(err)
    """
    1 validation error for Model
    numbers.0
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='str', input_type=str]
    """

"""
Below is the example of plain validators
"""
class Model4(BaseModel):
    number : int

    @field_validator('number', mode='plain')
    @classmethod
    def val_number(cls, value: Any) -> Any:
        if isinstance(value, int):
            return value * 2
        else:
            return value

print(Model4(number=4))
# output: 8

print(Model4(number='invalid'))
# output : invalid


"""
below is the example of wrap validators
"""
from pydantic import Field, ValidatorFunctionWrapHandler
from typing import Annotated

class Model5(BaseModel):
    my_string : Annotated[str, Field(max_length=5)]

    @field_validator("my_string", mode="wrap")
    @classmethod
    def truncate(cls, value : Any, handler : ValidatorFunctionWrapHandler) -> str:
        try:
            return handler(value)
        except ValidationError as err:
            if err.errors()[0]["type"] == "string_too_long":
                return handler(value[:5])
            else:
                raise

print(Model5(my_string='abcde'))
#output : 'abcde'

print(Model5(my_string='abcdef'))
#output : 'abcde'


"""
apply the function to multiple fields: decorator - example
"""
class Model6(BaseModel):
    f1: str
    f2: str

    @field_validator("f1", "f2", mode="before")
    @classmethod
    def capitalize(cls, value: str) -> str:
        return value.capitalize()
"""
If you want the validator to apply to all fields (including the ones defined in subclasses), you can pass '*' as the field name argument.
"""


"""
below is the example of model validators : beforeValidator type
"""
from pydantic import model_validator

class model7(BaseModel):
    username : str

    @model_validator(mode='before')
    @classmethod
    def check_card_number_not_present(cls, data : Any) -> Any:
        if isinstance(data, dict):
            if "card_number" in data:
                raise ValueError(" 'card_number' should not be included")
        return data
"""
This is a model-level validator, which means it checks the whole input data for the model, not just one field.
"""
"""
flow is 
Model7(username="raihan")
        ↓
Before Pydantic validates individual fields,
model_validator runs first
        ↓
data = {"username": "raihan"}
        ↓
Is data a dict? yes
        ↓
Does it contain "card_number"? no
        ↓
return data
        ↓
Pydantic continues normal validation
        ↓
username is a string ✅
        ↓
Model created

but if someone does 
Model7(
    username="raihan",
    card_number="123456789"
)
than raw input is 
{
    "username": "raihan",
    "card_number": "123456789"
}  , model validator decline it
"""


"""
below is the example of model validators : AfterValidator type
"""
from typing_extensions import Self

class Model8(BaseModel):
    username: str
    password : str
    password_repeat : str

    @model_validator(mode="after")
    @classmethod
    def check_passwords_match(self) -> Self:
        if self.password != self.password_repeat:
            raise ValueError("passwords do not match")
        return self
"""
We used self because 
@model_validator(mode="after") means Pydantic has already validated all the fields and created the model.
so now Self is essentially 
Model8(
    username="hello1234",
    password="hello",
    password_repeat="hello"
) and we can get the value of that field
"""


"""
below is the example of model validators : wrapValidator
"""
import logging
from pydantic import ModelWrapValidatorHandler

class Model9(BaseModel):
    username : str

    @model_validator(mode="wrap")
    @classmethod
    def log_failed_verification(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        try:
            return handler(data)
        except ValidationError:
            logging.error("Model %s failed to validate with data %s", cls, data)
            raise
"""
your wrap validator
      ↓
handler(data)
      ↓
Pydantic does its normal validation
      ↓
success → return model
failure → catch error, log it, re-raise it

raw data:
{"username": "raihan"}
      ↓
log_failed_verification(...)
      ↓
handler(data)
      ↓
Pydantic checks:
username must be str
      ↓
valid ✅
      ↓
Pydantic creates:
Model9(username="raihan")
      ↓
return that model

before
your code → Pydantic

after
Pydantic → your code

wrap
your code → Pydantic → your code can react to success/failure
"""


"""
below is the example of validation errors
"""
from pydantic_core import PydanticCustomError

class Model10(BaseModel):
    x: int

    @field_validator("x", mode="after")
    @classmethod
    def validate__x(cls, v: int) -> int:
        if  v % 42 == 0:
            raise PydanticCustomError("the_answer_error", "{number} is the answer!", {"number" : v})
        return v

try:
    Model10(x = 42 * 2)
except ValidationError as e:
    print(e)
    """
    1 validation error for Model
    x
      84 is the answer! [type=the_answer_error, input_value=84, input_type=int]
    """


"""
Below is the example of Validation data
The data property is None for model validators.
"""
from pydantic import ValidationInfo

class Model11(BaseModel):
    password : str
    password_repeat :  str
    username : str

    @field_validator("password_repeat", mode="after")
    @classmethod
    def check_password_match(cls, value: str, info: ValidationInfo) -> str:
        if value != info.data['password']:
            raise ValueError("password do not match")
        return value
"""
As validation is performed in the order fields are defined, you have to make sure you are not accessing a field that hasn't been validated yet. 
In the code above, for example, the username validated value is not available yet, as it is defined after password_repeat.
"""

"""
below is the example of validation context
"""
class Model12(BaseModel):
    text : str

    @field_validator("text", mode="after")
    @classmethod
    def remove_stopwords(cls, v: str, info : ValidationInfo) -> str:
        if isinstance(info.context, dict):
            stopwords = info.context.get("stopwords", set())
            v = " ".join(w for w in v.split() if w.lower() not in stopwords)
            """
            Split the sentence into words, keep only the words that are not in stopwords, then join them back into one sentence.
            """
            """
            line 366 can also be written like this

            words = v.split()
            filterd_words = []

            for word in words:
                if word.lower() not in stopwords:
                    filtered_words.append(word)
            
            v = " ".join(filtered_words)
            """
        return v

data = {"text" : "This is an example document"} 
print(Model12.model_validate(data)) #info.context is empty right now
# output: This is an example document

print(Model12.model_validate(data, context={"stopwords" : ["this", "is", "an"]}))
# output : example document
"""
we pass the context in the model and we used inside the classmethod
"""


"""
Below is the example of context for serialization
"""
from __future__ import annotations
from collections.abc import Generator
from contextlib import contextmanager
from contextvars import ContextVar

_init_context_var = ContextVar("_init_context_var", default=None)


@contextmanager
def init_context(value: dict[str, Any]) -> Generator[None]:
    token = _init_context_var.set(value)
    try:
        yield
    finally:
        _init_context_var.reset(token)

class Model13(BaseModel):
    my_number: int

    def __init__(self, /, **data: Any) -> None:
        self.__pydantic_validator__.validate_python(
            data,
            self_instance=self,
            context=_init_context_var.get(),
        )

    @field_validator("my_number")
    @classmethod
    def multiply_with_context(cls, value: int, info: ValidationInfo) -> int:
        if isinstance(info.context, dict):
            multiplier = info.context.get('multiplier', 1)
            value = value * multiplier
        return value


print(Model13(my_number=2))
#> my_number=2

with init_context({'multiplier': 3}):
    print(Model13(my_number=2))
    #> my_number=6

print(Model13(my_number=2))
#> my_number=2
"""
this pattern uses a ContextVar plus a custom __init__ so that you can pass temporary validation context even when creating a Pydantic model 
normally with Model(...). The init_context() context manager stores a dictionary such as {"multiplier": 3} inside _init_context_var. 
When Model(...) is created, the custom __init__ calls Pydantic's validator manually and passes the stored context into validation. 
The field validator then reads that extra information using info.context. Once the with block ends, the context is reset, 
so later model creations are back to normal.

Example : if you run Model(my_number=2) without context, the validator sees no multiplier and leaves the value as 2. 
But inside with init_context({"multiplier": 3}), the context stores 3, the custom __init__ passes it into Pydantic, 
and the validator changes 2 into 2 * 3 = 6. After leaving the with block, the context is cleared, so Model(my_number=2) again returns 2.

below is the example with model_validate for the same problem and it is more easy
"""
class Model14(BaseModel):
    my_number : int

    @field_validator("my_number")
    @classmethod
    def multiply_with_context(cls, value: int, info: ValidationInfo) -> int:
        if isinstance(info.context, dict):
            multiplier = info.context.get("multiplier", 1)
            value = value * multiplier
        return value

data = {"my_number": 2}
print(Model.model_validate(data))
# my_number=2

print(Model.model_validate(data,context={"multiplier": 3}))
# my_number=6