## @file CalcModule.py
#  @author Harsh Patel
#  @brief Allocates students to second year programs based on free choice and GPA.
#  @date 1/15/2019

from ReadAllocationData import *
import operator 
import ast

## @brief Sorts the list of student dictionaries based on student GPA in descending order.
#  @param S (studentLst) List of student dictionaries created by function readStdnts(s).
#  @return Sorted list of student dictionaries in descending order based on student GPA score.
def sort(S):
    #from source https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
    sortGpaLst = sorted(S, key=operator.itemgetter('gpa'), reverse=True)
    return sortGpaLst

## @brief Computes average GPA of all males or females depending on the gender selected.
#  @param L (studentLst) List of student dictionaries created by function readStdnts(s).
#  @param g (gender) Gender, male or female, to compute average GPA.
#  @return Average GPA of a specfic gender.
def average(L, g):
    gradeSum = 0 
    numGender = 0
    for studnt in L:
        if (studnt["gender"] == g.lower()):
            gradeSum += studnt["gpa"]
            numGender += 1
    if (numGender > 0):
        return round(gradeSum/numGender, 2)
    else:
        return ("No %s students in program" %(g.lower()))

## @brief Allocates students to a program as long as their GPA is above 4.0.
#  @details Allocates students with a GPA above 4.0 to a program beginning 
#           from allocating free choice students first, then normal students from 
#           highest GPA first. Students will be allocated to their first choice unless its full.
#           If their second choice is full, then they are allocated to their third choice.
#  @param S (studentLst) List of student dictionaries created by function readStdnts(s).
#  @param F (freeChoiceLst) List of macIDs of students with free choice created by readFreeChoice(s).
#  @param C (capacityDict) Dictionary with each department and their corresponding capacities.
#  @return Dctionary with each a list of student dictionaries allocated to each department
def allocate(S, F, C):
    
    allocateDict = {}
    
    #Departments
    Software = []
    Civil = []
    Chemical = []
    Electrical = []
    Materials = []
    Engphys = []
    Mechanical = []

    #Copy of list of student dictionaries created by function readStdnts(s)
    tempLst = S

    #Copy of dictionary with each department and corresponding capacities
    capacityDict = C

    #allocate free choice students
    for freeStdnts in F:
        count = -1
        for normStdnts in tempLst:
            count += 1
            if (normStdnts["macId"] == freeStdnts):
                if(normStdnts["gpa"] > 4.0):
                    allocation = vars()[normStdnts["choices"][0]]
                    allocation.append(normStdnts)
                    capacityDict[normStdnts["choices"][0]] -= 1
                    del(tempLst[count])
                else:
                    del(tempLst[count])
    
    #sort students based on highest GPA first
    highToLow = sort(tempLst)

    #allocate non-free choice students
    for students in highToLow:
        if (students["gpa"] > 4.0):
            progAllo = vars()[students["choices"][0]]
            progAllo1 = vars()[students["choices"][1]]
            progAllo2 = vars()[students["choices"][2]]
            if (capacityDict[students["choices"][0]] > 0):
                progAllo.append(students)
                capacityDict[students["choices"][0]] -= 1
            elif (capacityDict[students["choices"][1]] > 0):
                progAllo1.append(students)
                capacityDict[students["choices"][1]] -= 1
            elif (capacityDict[students["choices"][2]] > 0):
                progAllo2.append(students)
                capacityDict[students["choices"][2]] -= 1
  
    departments = C.keys()

    for program in departments:
        allocateDict[program] = vars()[program]

    return allocateDict

