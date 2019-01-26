from ReadAllocationData import *
from CalcModule import *
import operator
import ast

def testEqual(test, result, testName):
    if (test == result):
        print("Test Description : %s\n" %(testName))
        print("%s == %s\n" % (test, result))
        print("TEST PASSED!\n")
    else:
        print("Test Description : %s\n" %(testName))
        print("%s != %s\n" % (test, result))
        print("TEST FAILED\n")

#Normal test case to see if List is sorted correctly
def testSort1():
    stdntFile = readStdnts("sortGpaStdnts.txt")
    sortedLst = sort(stdntFile)
    testEqual(sortedLst, [{'macId' : 'patelh75', 'fname' : 'Harsh', 'lname' : 'Patel', 'gender' : 'male', 'gpa' : 10.6, 'choices' : ['Software', 'Mechanical', 'Engphys']},
                          {'macId' : 'cody9', 'fname' : 'Cody', 'lname' : 'Codes', 'gender' : 'male', 'gpa' : 9.2, 'choices' : ['Mechanical', 'Engphys', 'Chemical']},
                          {'macId' : 'brain8', 'fname' : 'Shawn', 'lname' : 'Brain', 'gender' : 'male', 'gpa' : 8.5, 'choices' : ['Software', 'Chemical', 'Materials']}],
             "Sorting File GPA descending")


#Test how order of sorting occurs when some students have the same GPA
def testSort2():
    stdntFile = readStdnts("sortSameGpa.txt")
    sortedFile = sort(stdntFile)
    testEqual(sortedFile, [{'macId' : 'patelh75', 'fname' : 'Harsh', 'lname' : 'Patel', 'gender' : 'male', 'gpa' : 10.5, 'choices' : ['Software', 'Mechanical', 'Engphys']},
                           {'macId' : 'cody9', 'fname' : 'Cody', 'lname' : 'Codes', 'gender' : 'male', 'gpa' : 10.5, 'choices' : ['Mechanical', 'Engphys', 'Chemical']},
                           {'macId' : 'brain8', 'fname' : 'Shawn', 'lname' : 'Brain', 'gender' : 'male', 'gpa' : 8.5, 'choices' : ['Software', 'Chemical', 'Materials']},
                           {'macId' : 'grande4', 'fname' : 'Ariana', 'lname' : 'Grande', 'gender' : 'female', 'gpa' : 8.5, 'choices' : ['Materials', 'Chemical', 'Engphys']}], 
              "Students with Same GPA : Students entered first in the file appear before other student with same GPA in Sorted List")

#Test to see sorted list stays sorted 
def testSort3():
    stdntFile = readStdnts("AlreadySorted.txt")
    sortedFile = sort(stdntFile)
    testEqual(sortedFile, [{'macId' : 'patelh75', 'fname' : 'Harsh', 'lname' : 'Patel', 'gender' : 'male', 'gpa' : 10.5, 'choices' : ['Software', 'Mechanical', 'Engphys']},
                           {'macId' : 'cody9', 'fname' : 'Cody', 'lname' : 'Codes', 'gender' : 'male', 'gpa' : 9.2, 'choices' : ['Mechanical', 'Engphys', 'Chemical']},
                           {'macId' : 'brain8', 'fname' : 'Shawn', 'lname' : 'Brain', 'gender' : 'male', 'gpa' : 8.5, 'choices' : ['Software', 'Chemical', 'Materials']}], 
              "Sorted File remains Sorted in List")

#Test if an empty file will cause any errors or simply return an empty list
def testSort4():
    stdntFile = readStdnts("empty.txt")
    sortedFile = sort(stdntFile)
    testEqual(sortedFile, [], "Empty File returns empty list")

#Normal Test case to calculate average Male GPA
def testAverageMale1():
    stdntFile = readStdnts("students.txt")
    maleAverage = average(stdntFile, "male")
    testEqual(8.22, maleAverage, "Average GPA of male students")

#Normal Test case to calculate average female GPA
def testAverageFemale1():
    stdntFile = readStdnts("students.txt")
    femaleAverage = average(stdntFile, "female")
    testEqual(9.1, femaleAverage, "Average GPA of female students")


#Test Case when no male students are enrolled and user wants average male GPA
def testAverageMale2():
    stdntFile = readStdnts("onlyFemales.txt")
    maleAverage = average(stdntFile, "male")
    testEqual("No male students in program", maleAverage, "Calculating average GPA of male students when no male students in program")

     
#Test Case when no female students are enrolled and user wants average female GPA
def testAverageFemale2():
    stdntFile = readStdnts("onlyMales.txt")
    femaleAverage = average(stdntFile, "female")
    testEqual("No female students in program", femaleAverage, "Calculating average GPA of female students when no female students in program")

#Test case for normal allocation of students into selected programs
def testAllocate1():
    stdntFile = readStdnts("students.txt")
    freeChoice = readFreeChoice("freeChoice.txt")
    capacityFile = readDeptCapacity("depCapacity.txt")
    testEqual({"Software" : [{'macId' : 'patelh75', 'fname' : 'Harsh', 'lname' : 'Patel', 'gender' : 'male', 'gpa' : 10.6, 'choices' : ['Software', 'Mechanical', 'Engphys']},
                             {'macId' : 'brain8', 'fname' : 'Shawn', 'lname' : 'Brain', 'gender' : 'male', 'gpa' : 8.5, 'choices' : ['Software', 'Chemical', 'Materials']},
                             {'macId' : 'Jacky3', 'fname' : 'Jack', 'lname' : 'Jacky', 'gender' : 'male', 'gpa' : 7.2, 'choices' : ['Software', 'Electrical', 'Engphys']}], 
               "Electrical" : [{'macId' : 'kenway1', 'fname' : 'Edward', 'lname' : 'Kenway', 'gender' : 'male', 'gpa' : 9.8, 'choices' : ['Electrical', 'Engphys', 'Chemical']}], 
               "Materials" : [{'macId' : 'grande4', 'fname' : 'Ariana', 'lname' : 'Grande', 'gender' : 'female', 'gpa' : 9.5, 'choices' : ['Materials', 'Chemical', 'Engphys']}],
               "Engphys" : [{'macId' : 'pam4', 'fname' : 'Pammy', 'lname' : 'Pam', 'gender' : 'female', 'gpa' : 8.2, 'choices' : ['Engphys', 'Electrical', 'Civil']}],
               "Chemical" : [{'macId' : 'jen2', 'fname' : 'Jenny', 'lname' : 'Jen', 'gender' : 'female', 'gpa' : 11.2, 'choices' : ['Chemical', 'Civil', 'Engphys']}],
               "Mechanical" : [{'macId' : 'cody9', 'fname' : 'Cody', 'lname' : 'Codes', 'gender' : 'male', 'gpa' : 9.2, 'choices' : ['Mechanical', 'Engphys', 'Chemical']}],
               "Civil" : [{'macId' : 'jessie1', 'fname' : 'Jes', 'lname' : 'Jessie', 'gender' : 'female', 'gpa' : 7.5, 'choices' : ['Civil', 'Software', 'Materials']}]}, 
              allocate(stdntFile, freeChoice, capacityFile), "Normal Student Allocation")


#more free choice students then number of seats of popular program so they should be allocated even if seats are full
#non-free choice students selecting that filled program will be allocated to their second choice
def testAllocate2():
    stdntFile = readStdnts("studentTestAllocate.txt")
    freeChoice = readFreeChoice("freeChoiceAllSoftware.txt")
    capacityFile = readDeptCapacity("depCapacity.txt")
    testEqual({"Software" : [{'macId' : 'patelh75', 'fname' : 'Harsh', 'lname' : 'Patel', 'gender' : 'male', 'gpa' : 10.6, 'choices' : ['Software', 'Mechanical', 'Engphys']},
                             {'macId' : 'brain8', 'fname' : 'Shawn', 'lname' : 'Brain', 'gender' : 'male', 'gpa' : 8.5, 'choices' : ['Software', 'Chemical', 'Materials']},
                             {'macId' : 'cody9', 'fname' : 'Cody', 'lname' : 'Codes', 'gender' : 'male', 'gpa' : 9.2, 'choices' : ['Software', 'Engphys', 'Chemical']},
                             {'macId' : 'jen2', 'fname' : 'Jenny', 'lname' : 'Jen', 'gender' : 'female', 'gpa' : 11.2, 'choices' : ['Software', 'Civil', 'Engphys']},
                             {'macId' : 'jessie1', 'fname' : 'Jes', 'lname' : 'Jessie', 'gender' : 'female', 'gpa' : 7.5, 'choices' : ['Software', 'Engphys', 'Materials']}], 
               "Electrical" : [{'macId' : 'kenway1', 'fname' : 'Edward', 'lname' : 'Kenway', 'gender' : 'male', 'gpa' : 9.8, 'choices' : ['Electrical', 'Engphys', 'Chemical']},
                               {'macId' : 'Jacky3', 'fname' : 'Jack', 'lname' : 'Jacky', 'gender' : 'male', 'gpa' : 7.2, 'choices' : ['Software', 'Electrical', 'Engphys']}], 
               "Materials" : [{'macId' : 'grande4', 'fname' : 'Ariana', 'lname' : 'Grande', 'gender' : 'female', 'gpa' : 9.5, 'choices' : ['Materials', 'Chemical', 'Engphys']}],
               "Engphys" : [{'macId' : 'pam4', 'fname' : 'Pammy', 'lname' : 'Pam', 'gender' : 'female', 'gpa' : 8.2, 'choices' : ['Engphys', 'Electrical', 'Civil']}],
               "Chemical" : [],
               "Mechanical" : [],
               "Civil" : []}, 
              allocate(stdntFile, freeChoice, capacityFile), "More free choice students enrolled in a certain department then capacity of program")

#Test case to see if empty list or file raises any errors
def testAllocate3():
    stdntFile = readStdnts("empty.txt")
    freeChoice = readFreeChoice("empty.txt")
    capacityFile = readDeptCapacity("depCapacity.txt")
    testEqual({"Software" : [], "Electrical" : [], "Materials" : [], 
               "Engphys" : [], "Chemical" : [], "Mechanical" : [], "Civil" : []}, 
              allocate(stdntFile, freeChoice, capacityFile), "Empty file returns Empty dictionary with department names and empty lists")


def test():
    testSort1()
    testSort2()
    testSort3()
    testSort4()
    testAverageMale1()
    testAverageFemale1()
    testAverageMale2()
    testAverageFemale2()
    testAllocate1()
    testAllocate2()
    testAllocate3()
test()