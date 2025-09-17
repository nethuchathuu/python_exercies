from backend.models import Person

from frontend.validators import is_valid_age


age = 30


p = Person("Nethmi")

if is_valid_age(age):
    p.set_age(age)