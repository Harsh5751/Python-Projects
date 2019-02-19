## @file StdntAllocTypes.py
#  @author Harsh Patel
#  @brief Enumerated types and NamedTuples
#  @date 11/02/2019


from enum import Enum
from typing import NamedTuple
from SeqADT import *


## @brief An enumerated type representing the gender set
class GenT(Enum):
    male = 1
    female = 2


## @brief An enumerated type representing the department set
class DeptT(Enum):
    civil = 1
    chemical = 2
    electrical = 3
    mechanical = 4
    software = 5
    materials = 6
    engphys = 7


## @brief A named tuple representing general information for a student
class SInfoT(NamedTuple):
    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: type(SeqADT(DeptT))
    freechoice: bool
