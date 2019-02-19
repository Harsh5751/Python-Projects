## @file DCapALst.py
#  @author Harsh Patel
#  @brief DCapALst
#  @date 11/02/2019


## @brief DCapALst is an abstract data type
class DCapALst:
    s = []

    ## @brief init function
    #  @details Initializes the sequence to an empty sequence
    @staticmethod
    def init():
        DCapALst.s = []

    ## @brief add function
    #  @details Adds a department and its capacity to the sequence
    #  @param d Department name
    #  @param n Department capacity
    #  @throw KeyError raised if department already exists in the sequence
    @staticmethod
    def add(d, n):
        for department in DCapALst.s:
            if (department["dept"] == d.name):
                raise(KeyError)
        DCapALst.s.append({"dept": d.name, "cap": n})

    ## @brief remove function
    #  @details Removes a department and its capacity from the sequence
    #  @param d Department name
    #  @throw KeyError if department is not in sequence
    @staticmethod
    def remove(d):
        if not(DCapALst.elm(d)):
            raise(KeyError)
        for s_info in DCapALst.s:
            if (d.name == s_info["dept"]):
                DCapALst.s.remove(s_info)
                break

    ## @brief elm function
    #  @details Checks if the department is in the sequence
    #  @param d Department name
    #  @return Boolean value representing if department is in the sequence
    @staticmethod
    def elm(d):
        for department in DCapALst.s:
            if department["dept"] == d.name:
                return True
        return False

    ## @brief capacity function
    #  @details Gets capacity of the department
    #  @param d Department name
    #  @throw KeyError raised if department not in the sequence
    #  @return Returns department capacity
    @staticmethod
    def capacity(d):
        for d_info in DCapALst.s:
            if (d.name == d_info["dept"]):
                return d_info["cap"]
        raise(KeyError)
