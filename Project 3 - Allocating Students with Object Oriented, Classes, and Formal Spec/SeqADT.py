## @file SeqADT.py
#  @author Harsh Patel
#  @brief SeqADT
#  @date 11/02/2019


## @brief Abstract data type for sequence manipulation
class SeqADT:
    ## @brief SeqADT constructor
    #  @details takes a list of values
    #  @param x list of values
    def __init__(self, x):
        self.s = x
        self.i = 0

    ## @brief start function
    #  @details sets index, i, of list to 0
    def start(self):
        self.i = 0

    ## @brief next function
    #  @details increments index, i, of list
    #  @throw StopIteration if index, i, is equal to the length of list
    #  @returns element of list at index, i, before increment
    def next(self):
        if (self.i >= len(self.s)):
            raise(StopIteration)
        self.i += 1
        return self.s[(self.i) - 1]

    ## @brief end function
    #  @details checks if index reached end of list
    #  @returns boolean value representing if index, i, is at the
    #  end of the list
    def end(self):
        return self.i >= len(self.s)
