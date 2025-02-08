#### https://medium.com/@abuolubunmi21/improve-your-python-skills-with-type-hinting-3496d422fe24

from typing import Optional, Union, List, Dict, Tuple, Any, NewType, Callable, Literal, NoReturn

# As Python 3.10+, Optional can be Optional or shortand: | None
def get_user_age(age: Optional[int] = None) -> Optional[int]:
    return age if age is not None else "Age not provided"

def get_user_colour(colour: str | None) -> str | None:
    return colour if colour is not None else "Colour not provided"

def example_union(data: Union[int, str] = None) -> Union[int, str]:
    return data if data is not None else "Data not provided"

# scores are expected to be a list of integers, and will be returning integer
def process_scores(scores: List[int]) -> int:
    return sum(scores)

# info is expected to be a dictionary with keys 'name' and 'age' and values of type str and int respectively
def student_info(info: Dict[str, Union[int, str]]) -> None:
    return info

# used when the function returns a fixed-length sequence of elements
def get_coordinates() -> Tuple[int, int]:
    return (10, 20)

# Any can be used when the function can return any type
def print_value(value: Any) -> None:
    print(value)

# Callable is used to define a function signature
def execute_functions(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# Literal is used to define a fixed set of values
def get_status(status: Literal['active', 'inactive']) -> str:
    return f"Status: {status}"

# NoReturn is used to indicate that the function does not return anything
def stop() -> NoReturn:
    raise SystemExit("Stopping the program")

if __name__ == "__main__":
    print(get_user_age(32))
    print(get_user_age())
    
    print(get_user_colour("Red"))
    print(get_user_colour(None))
    
    print(example_union(42))
    print(example_union("Hello"))
    print(example_union())
    print(example_union(None))

    print(process_scores([10, 20, 30, 40]))
    print(student_info({'name': 'John', 'age': 25}))
    
    print(get_coordinates())
    
    print(print_value(42))
    print(print_value("Hello"))
    print(print_value([1,2,3,4]))
    print(print_value({'name': 'John', 'age': 25}))
    
    print(execute_functions(lambda x, y: x + y, 10, 20))
    
    print(get_status('active'))
    
    # stop()
    
    
    