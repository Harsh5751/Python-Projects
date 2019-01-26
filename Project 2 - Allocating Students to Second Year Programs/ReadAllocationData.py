## @file ReadAllocationData.py
#  @author Harsh Patel
#  @brief Reads student information from files.
#  @date 1/15/2019

import ast

## @brief Reads a file and returns a list of dictionaries of student information. 
#  @details Function accepts one parameter that is the name of a file containing student information.
#  @param s ("students.txt") name of file being read.
#  @return List of dictionaries of student information. 
def readStdnts(s):
    with open(s, "r") as studentFiles:
        studentData = studentFiles.read()
        studentData = studentData.splitlines()
    return [ast.literal_eval(student) for student in studentData]

## @brief Reads a file containing only free choice students and returns their macID's in a list.
#  @param s ("FreeChoice.txt") Name of file being read.
#  @return List of macIds of students with free choice. 
def readFreeChoice(s):
    with open(s, "r") as studentChoice:
        studentData = studentChoice.read()
        studentData = studentData.splitlines()
        freeChoiceLst = [ast.literal_eval(stdnt) for stdnt in studentData]
    return [freeStdnt["macId"] for freeStdnt in freeChoiceLst]

## @brief Reads a file containing capacities of each department students will be allocated to and 
#         returns the name of the department and capacity in a dictionary. 
#  @param s ("Capacity.txt") Name of file being read.
#  @return Dictionary with each department name and capacity
def readDeptCapacity(s):
    capacity = {}
    deptLst = readStdnts(s)
    for dept in deptLst:
        capacity.update(dept)
    return capacity
