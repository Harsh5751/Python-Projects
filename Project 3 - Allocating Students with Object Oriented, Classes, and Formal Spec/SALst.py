## @file SALst.py
#  @author Harsh Patel
#  @brief SALst
#  @date 11/02/2019


from StdntAllocTypes import *
from AALst import *
from DCapALst import *


## @brief Abstract data type that represents a sequence
#  with student information
class SALst:
    s = []

    ## @brief init function
    #  @details Initilizes an empty sequence
    @staticmethod
    def init():
        SALst.s = []

    ## @brief add function
    #  @details Adds a student's information to the sequence
    #  @param m macid of the student
    #  @param i Student information of type SInfoT
    #  @throw KeyError raised if information for student already
    #  exists in the sequence
    @staticmethod
    def add(m, i):
        if {"macid": m, "info": i} in SALst.s:
            raise(KeyError)
        else:
            SALst.s.append({"macid": m, "info": i})

    ## @brief remove function
    #  @details Removes the information of the student in the sequence
    #  @param m macid of the student
    #  @throw KeyError raised if macid not in the sequence
    @staticmethod
    def remove(m):
        if (not(SALst.elm(m))):
            raise(KeyError)
        for student in SALst.s:
            if(student["macid"] == m):
                SALst.s.remove(student)
                break

    ## @brief elem function
    #  @details Checks if student information is in sequence
    #  @param m macid of the student
    #  @return Boolean value representing if information in sequence
    @staticmethod
    def elm(m):
        for student in SALst.s:
            if student["macid"] == m:
                return True
        return False

    ## @brief info function
    #  @details Retrieves a student's information based on macid
    #  @param m macid of the student
    #  @throw ValueError raised if student is not in sequence
    #  @return Information of the specific student of type SInfoT
    @staticmethod
    def info(m):
        for student in SALst.s:
            if student["macid"] == m:
                return student["info"]
        raise(ValueError)

    ## @brief sort function
    #  @details Sorts the students in order of descending gpa
    #  @param f condition that filters macids that don't meet its standards
    #  @return A sequence of macids in order of descending gpa of
    #  the students that passed the condition f
    @staticmethod
    def sort(f):
        stdnt_lst = [stdnt["info"] for stdnt in SALst.s]
        filter_lst = list(filter(f, stdnt_lst))
        id_lst = [stdnt["macid"] for stdnt in SALst.s
                  if stdnt["info"] in filter_lst]

        def get_gpa(m, s):
            for stdnts in s:
                if stdnts["macid"] == m:
                    std_info = stdnts["info"]
                    return std_info.gpa

        for stdnt_pos in range(len(id_lst) - 1):
            stdnt_1 = get_gpa(id_lst[stdnt_pos], SALst.s)
            stdnt_2 = get_gpa(id_lst[stdnt_pos + 1], SALst.s)
            if (stdnt_2 > stdnt_1):
                temp = id_lst[stdnt_pos]
                id_lst[stdnt_pos] = id_lst[stdnt_pos + 1]
                id_lst[stdnt_pos + 1] = temp
        return id_lst

    ## @brief average function
    #  @details calculates the average gpa students that
    #  meet the condition specified
    #  @param f condition that filters students that don't meet its standards
    #  @return Average gpa of students that meet condition f
    def average(f):
        f_set = [stdnt["info"] for stdnt in SALst.s]
        filter_lst = list(filter(f, f_set))
        if len(filter_lst) == 0:
            raise(ValueError)
        tot_gpa = sum(student.gpa for student in filter_lst)
        return tot_gpa / len(filter_lst)

    ## @brief allocate function
    #  @details Allocates students to their respective departments
    #  based on choices selected, Gpa, and freechoice
    def allocate():
        AALst.init()
        F = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in F:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)

        S = SALst.sort(lambda t: not(t.freechoice) and t.gpa >= 4.0)
        for m in S:
            ch = SALst.info(m).choices
            alloc = False
            while not(alloc) and not(ch.end()):
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if not(alloc):
                raise(RuntimeError)
