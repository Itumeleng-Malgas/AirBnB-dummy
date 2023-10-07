#!/usr/bin/python3
"""combines all models modules."""

from .base_model import BaseModel as Base
from .interpreter import interpreter

from .review import Review
from .place import Place
from .state import State
from .city import City
from .user import User
