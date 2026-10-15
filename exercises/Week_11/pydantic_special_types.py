"""
Pydantic provides few special utilities
"""

from pydantic import BaseModel, InstanceOf, ValidationError

"""
below is the example of instanceof
"""
class Fruit:
    def __repr__(self):
        return self.__class__.__name__

class Banana(Fruit):
    pass

class Apple(Fruit):
    pass

class Basket(BaseModel):
    fruits : list[InstanceOf[Fruit]]
    """
    InstancOf : can be used to validate that a value is an instance of a given class.
    """

print(Basket(fruits=[Banana(), Apple()]))
# output : [Banana, Apple]

try:
    Basket(fruits=[Banana(), "Apple"])
except ValidationError as e:
    print(e)
    """
    1 validation error for Basket
    fruits.1
      Input should be an instance of Fruit [type=is_instance_of, input_value='Apple', input_type=str]
    """


"""
below is the example of SkipValidation
"""
from pydantic import SkipValidation

class Model2(BaseModel):
    names = list[SkipValidation[str]]

m = Model2(names = ["foo", "bar"])
print(m)
# output : ['foo', 'bar']

n = Model2(names = ["Foo", 123])
"""
Note that the validation of the second item is skipped. If it has the wrong type it will emit a warning during serialization.
SkipValidation : can be used to skip validation on a field.
"""
print(n)
# output : ['foo', 123]


"""
below is the example of ValidateAs
"""
from typing import Annotated

from pydantic import TypeAdapter, ValidateAs

class MyCls:
    def __init__(self, a: int) -> None:
        self.a = a

    def __repr__(self) -> str:
        return f"MYCls(a={self.a})"

class ValModel(BaseModel):
    a: int

ta = TypeAdapter( Annotated[MyCls, ValidateAs(ValModel, lambda v : MyCls(a=v.a))])
"""
ValidateAs : can be used to validate a custom type from a type natively supported by Pydantic.
"""

print(ta.validate_python({"a" : 1}))
# output : (a=1)


"""
below is the example of PydanticUseDefault
"""
from typing import Any

from pydantic_core import PydanticUseDefault
from pydantic import BeforeValidator

def default_if_none(value : Any) -> Any:
    if value is None:
        raise PydanticUseDefault()
    """
    PydanticUseDefault can be used to notify Pydantic that the default value should be used.
    """
    return value

class Model(BaseModel):
    name : Annotated[str, BeforeValidator(default_if_none)] = "default_name"

print(Model(name = None))
#output : name='default_name'


"""
Below is the example of JSON Schema and field validators
"""
from pydantic import field_validator

class Model(BaseModel):
    value : str

    @field_validator("value", mode="before", json_schema_input_type=int | str)
    @classmethod
    def cast_ints(cls, value : Any) -> Any:
        if isinstance(value, int):
            return str(value)
        else:
            return value

print(Model(value='a'))
#> value='a'
print(Model(value=1))
#> value='1'

print(Model.model_json_schema()['properties']['value'])
#> {'anyOf': [{'type': 'integer'}, {'type': 'string'}], 'title': 'Value'}
