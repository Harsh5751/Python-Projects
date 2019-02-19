import pytest
from SALst import *
from DCapALst import *
from SeqADT import *

class TestSeqADT:
    def test_start_none(self):
        seqADT1 = SeqADT([1,2,3])
        assert print(seqADT1.start()) == None

    def test_first_next_element_0(self):
        seqADT2 = SeqADT(["Hey",2,3,4,5])
        assert seqADT2.next() == "Hey"

    def test_second_next_element_1(self):
        seqADT3 = SeqADT(["Hey", True, 8, 9])
        seqADT3.next() 
        assert seqADT3.next() == True

    def test_exception_next(self):
        seqADT3 = SeqADT(["Hey", True, 8])
        seqADT3.next()
        seqADT3.next()
        seqADT3.next()
        with pytest.raises(StopIteration):
            seqADT3.next()

    def test_end_not_end(self):
        seqADT4 = SeqADT([1,"Hello", 2])
        seqADT4.next()
        seqADT4.next()
        assert seqADT4.end() == False

    def test_end_at_end(self):
        seqADT5 = SeqADT([1,"Hello", 2])
        seqADT5.next()
        seqADT5.next()
        seqADT5.next()
        assert seqADT5.end() == True

    def test_end_over_end(self):
        seqADT6 = SeqADT([1,"Hello", 2])
        seqADT6.next()
        seqADT6.next()
        seqADT6.next()
        with pytest.raises(StopIteration):
            seqADT6.next()
            seqADT6.end()

    def test_empty(self):
        empty = SeqADT([])
        with pytest.raises(StopIteration):
            empty.next()

    def test_empty2(self):
        empty2 = SeqADT([])
        assert empty2.end() == True

class TestDCapALst:

    def test_add_normal(self):
        s = DCapALst
        s.init()
        s.add(DeptT.software, 5)
        assert s.s == [{"dept":"software", "cap":5}]

    def test_add_same(self):
        s = DCapALst
        s.init()
        s.add(DeptT.software, 5)
        with pytest.raises(KeyError):
            s.add(DeptT.software, 7)
        
    def test_remove_normal(self):
        s = DCapALst
        s.init()
        s.add(DeptT.software, 5)
        s.add(DeptT.chemical, 9)
        s.remove(DeptT.chemical)
        assert s.s == [{"dept":"software", "cap":5}]

    def test_remove_not_present(self):
        s = DCapALst
        s.init()
        s.add(DeptT.software, 5)
        s.add(DeptT.chemical, 9)
        with pytest.raises(KeyError):
            s.remove(DeptT.civil)

    def test_elem_normal(self):
        s = DCapALst
        s.init()
        s.add(DeptT.software, 5)
        s.add(DeptT.chemical, 9)
        assert s.elm(DeptT.chemical) == True

    def test_elem_not_there(self):
        s = DCapALst
        s.init()
        s.add(DeptT.software, 5)
        s.add(DeptT.chemical, 9)
        assert s.elm(DeptT.civil) == False

    def test_capacity_normal(self):
        s = DCapALst
        s.init()
        s.add(DeptT.software, 5)
        s.add(DeptT.chemical, 9)
        assert s.capacity(DeptT.software) == 5

    def test_capacity_not_there(self):
        s = DCapALst
        s.init()
        s.add(DeptT.software, 5)
        s.add(DeptT.chemical, 9)
        with pytest.raises(KeyError):
            s.capacity(DeptT.civil)

class TestSALst:

    def test_add_normal(self):
        t = SALst
        t.init()
        m = "patelh75"
        i = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        t.add(m,i)
        assert (t.s[0]["macid"] == m and t.s[0]["info"] == i) 

    def test_add_already_added(self):
        t = SALst
        t.init()
        m = "patelh75"
        i = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        t.add(m,i)
        with pytest.raises(KeyError):
            t.add(m,i)

    def test_add_another(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        i = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        t.add(m,i)
        t.add(m1,i1)
        assert (t.s == [{"macid":m,"info":i},{"macid":m1,"info":i1}])

    def test_remove_normal(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        i = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        t.add(m,i)
        t.add(m1,i1)
        t.remove(m1)
        assert (t.s == [{"macid":m,"info":i}])

    def test_remove_already_removed(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        i = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        t.add(m,i)
        t.add(m1,i1)
        t.remove(m1)
        with pytest.raises(KeyError):
            t.remove(m1)

    def test_elm_normal(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        i = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        t.add(m,i)
        t.add(m1,i1)
        assert t.elm(m) == True

    def test_elm_not_there(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        i = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        t.add(m,i)
        assert t.elm(m1) == False

    def test_info_normal(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        i = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        t.add(m,i)
        t.add(m1,i1)
        assert t.info(m) == i

    def test_info_not_there(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        i = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        t.add(m,i)
        with pytest.raises(ValueError):
            t.info(m1)

    def test_sort_normal(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        m2 = "me2"
        i = SInfoT("first", "last", GenT.male, 10.5, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        i2 = SInfoT("firstttt", "lastttt", GenT.male, 12.0, SeqADT([DeptT.materials, DeptT.chemical]), True)
        t.add(m,i)
        t.add(m1,i1)
        t.add(m2,i2)
        lst = t.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        assert lst == [m2,m]

    def test_sort_another_condition(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        m2 = "me2"
        i = SInfoT("first", "last", GenT.male, 10.5, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        i2 = SInfoT("firstttt", "lastttt", GenT.male, 12.0, SeqADT([DeptT.materials, DeptT.chemical]), True)
        t.add(m,i)
        t.add(m1,i1)
        t.add(m2,i2)
        lst = t.sort(lambda t: t.freechoice)
        assert lst == [m2,m]

    def test_average_male(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        m2 = "me2"
        i = SInfoT("first", "last", GenT.male, 10.5, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        i2 = SInfoT("firstttt", "lastttt", GenT.male, 12.0, SeqADT([DeptT.materials, DeptT.chemical]), True)
        t.add(m,i)
        t.add(m1,i1)
        t.add(m2,i2)
        avg = t.average(lambda t: t.gender == GenT.male)
        assert avg == (10.5 + 12) / 2

    def test_average_no_male(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        m2 = "me2"
        i = SInfoT("first", "last", GenT.female, 10.5, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        i2 = SInfoT("firstttt", "lastttt", GenT.female, 12.0, SeqADT([DeptT.materials, DeptT.chemical]), True)
        t.add(m,i)
        t.add(m1,i1)
        t.add(m2,i2)
        with pytest.raises(ValueError):
            avg = t.average(lambda t: t.gender == GenT.male)

    def test_average_female(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        m2 = "me2"
        i = SInfoT("first", "last", GenT.male, 10.5, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.female, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        i2 = SInfoT("firstttt", "lastttt", GenT.male, 12.0, SeqADT([DeptT.materials, DeptT.chemical]), True)
        t.add(m,i)
        t.add(m1,i1)
        t.add(m2,i2)
        avg = t.average(lambda t: t.gender == GenT.female)
        assert avg == 11.0
       
    def test_average_no_female(self):
        t = SALst
        t.init()
        m = "patelh75"
        m1 = "hero1"
        m2 = "me2"
        i = SInfoT("first", "last", GenT.male, 10.5, SeqADT([DeptT.civil, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.male, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        i2 = SInfoT("firstttt", "lastttt", GenT.male, 12.0, SeqADT([DeptT.materials, DeptT.chemical]), True)
        t.add(m,i)
        t.add(m1,i1)
        t.add(m2,i2)
        with pytest.raises(ValueError):
            avg = t.average(lambda t: t.gender == GenT.female)

    def test_allocate_normal(self):
        t = SALst
        n = DCapALst
        n.init()
        n.add(DeptT.software, 2)
        n.add(DeptT.civil, 2)
        n.add(DeptT.materials, 2)
        t.init()
        m = "patelh75"
        m1 = "hero1"
        m2 = "me2"
        i = SInfoT("first", "last", GenT.male, 10.5, SeqADT([DeptT.software, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.male, 11.0, SeqADT([DeptT.civil, DeptT.chemical]), False)
        i2 = SInfoT("firstttt", "lastttt", GenT.male, 12.0, SeqADT([DeptT.materials, DeptT.chemical]), True)
        t.add(m,i)
        t.add(m1,i1)
        t.add(m2,i2)
        t.allocate()
        assert AALst.num_alloc(DeptT.software) == 1 and AALst.num_alloc(DeptT.civil) == 1 and AALst.num_alloc(DeptT.materials) == 1

    def test_allocate_no_room(self):
        t = SALst
        n = DCapALst
        n.init()
        n.add(DeptT.software, 1)
        n.add(DeptT.civil, 0)
        n.add(DeptT.materials, 0)
        n.add(DeptT.chemical, 0)
        t.init()
        m = "patelh75"
        m1 = "hero1"
        m2 = "me2"
        i = SInfoT("first", "last", GenT.male, 11.5, SeqADT([DeptT.software, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.male, 11.0, SeqADT([DeptT.software, DeptT.chemical]), False)
        i2 = SInfoT("firstttt", "lastttt", GenT.male, 12.0, SeqADT([DeptT.materials, DeptT.chemical]), True)
        t.add(m,i)
        t.add(m1,i1)
        t.add(m2,i2)
        with pytest.raises(RuntimeError):
            t.allocate()

    def test_allocate_go_to_second(self):
        t = SALst
        n = DCapALst
        n.init()
        n.add(DeptT.mechanical, 2)
        n.add(DeptT.chemical, 2)
        n.add(DeptT.engphys, 1)
        t.init()
        m = "patelh75"
        m1 = "hero1"
        m2 = "me2"
        i = SInfoT("first", "last", GenT.male, 11.5, SeqADT([DeptT.engphys, DeptT.chemical]), True)
        i1 = SInfoT("fsdfirst", "lasdfst", GenT.male, 11.0, SeqADT([DeptT.mechanical, DeptT.chemical]), False)
        i2 = SInfoT("firstttt", "lastttt", GenT.male, 10.0, SeqADT([DeptT.engphys, DeptT.chemical]), False)
        t.add(m,i)
        t.add(m1,i1)
        t.add(m2,i2)
        t.allocate()
        assert AALst.num_alloc(DeptT.engphys) == 1 and AALst.num_alloc(DeptT.mechanical) == 1 and AALst.num_alloc(DeptT.chemical) == 1