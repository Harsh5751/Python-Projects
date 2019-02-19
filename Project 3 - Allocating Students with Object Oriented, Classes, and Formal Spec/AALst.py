## @file AALst.py
#  @author Harsh Patel
#  @brief AALst
#  @date 11/02/2019


from StdntAllocTypes import *


## @brief Abstract data type that represents the allocated sequence
class AALst:
    s = []

    ## @brief init function
    #  @details Initilizes a sequence with tuples of
    #  department name and empty list
    @staticmethod
    def init():
        for department in DeptT:
            AALst.s.append({"dept": department.name, "LstStdnts": []})

    ## @brief add_stdnt function
    #  @details Adds students to the list of the corresponding department
    #  @param d Department name
    #  @param m macid of the student
    @staticmethod
    def add_stdnt(d, m):
        for department in AALst.s:
            if (department["dept"] == d.name):
                department["LstStdnts"].append(m)

    ## @brief lst_alloc function
    #  @details Retrieves the list of macids of students
    #  allocated to the department
    #  @param d Department name
    #  @return List of macids of students allocated to the department
    @staticmethod
    def lst_alloc(d):
        for department in AALst.s:
            if (department["dept"] == d.name):
                return department["LstStdnts"]

    ## @brief num_alloc function
    #  @details Number of students allocated to a department
    #  @param d Department name
    #  @return length of a list corresponding to a department
    #  represting number of students allocated
    @staticmethod
    def num_alloc(d):
        for department in AALst.s:
            if (department["dept"] == d.name):
                return len(department["LstStdnts"])
