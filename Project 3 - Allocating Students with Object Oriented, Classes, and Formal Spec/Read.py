## @file Read.py
#  @author Harsh Patel
#  @brief Reads files and loads data
#  @date 11/02/2019


from StdntAllocTypes import *
from DCapALst import *
from SALst import *


## @brief Reads stduent data from text file
#  @details Populates SALst with student data from the text file
#  @param s String representing name of the text file
def load_stdnt_data(s):
    SALst.init()
    software = DeptT.software
    civil = DeptT.civil
    mechanical = DeptT.mechanical
    materials = DeptT.materials
    electrical = DeptT.electrical
    engphys = DeptT.engphys
    chemical = DeptT.chemical

    with open(s, "r") as student_files:
        student_data = student_files.read()
        student_data = student_data.replace(",", "")
        student_data = student_data.replace("[", "")
        student_data = student_data.replace("]", "")
        student_data = student_data.splitlines()
        for lines in student_data:
            std_data = lines.split()
            macid = std_data[0]
            fir_name = std_data[1]
            las_name = std_data[2]
            if (std_data[3] == "male"):
                gend = GenT.male
            else:
                gend = GenT.female
            gpa = float(std_data[4])
            prog_choic = []
            for i in range(5, len(std_data) - 1):
                program_type = vars()[std_data[i]]
                prog_choic.append(program_type)
            if (std_data[-1] == "True"):
                free_ch = True
            else:
                free_ch = False
            info = SInfoT(fir_name, las_name, gend, gpa,
                          SeqADT(prog_choic), free_ch)
            SALst.add(macid, info)


## @brief Reads department data from text file
#  @details Populates DCapALst with department and capacity data
#  @param s String representing name of the text file
def load_dcap_data(s):
    DCapALst.init()
    software = DeptT.software
    civil = DeptT.civil
    mechanical = DeptT.mechanical
    materials = DeptT.materials
    electrical = DeptT.electrical
    engphys = DeptT.engphys
    chemical = DeptT.chemical

    with open(s, "r") as dept_info:
        dept_info = dept_info.read()
        dept_info = dept_info.replace(",", "")
        dept_info = dept_info.splitlines()
        for lines in dept_info:
            dept_infolst = lines.split()
            department = vars()[dept_infolst[0]]
            capacity = int(dept_infolst[1])
            DCapALst.add(department, capacity)
