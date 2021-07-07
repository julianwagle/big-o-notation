from random import shuffle

class BigONotation:
    '''
    The following are examples of functions with 
    run times denoted by Big O notation.

    Example Usage A: 
        >>> from big_o import *; BigONotation()
    Example Usage B: 
        >>> BigONotation()
    '''
    def __init__(self):
        self.test_list = []

        self.get_new_list()
        print('Constant time: O(1)')
        self.print_val()

        self.get_new_list()
        print('Logarithmic time: O(log n)')
        self.divide_val()

        self.get_new_list()
        print('Linear time: O(n)')
        self.print_all_vals()

        self.get_new_list()
        print('Linearithmic/Quasilinear time: O(n log n)')
        self.quick_sort(
            test_list = self.test_list,
            low = 0,
            high = len(self.test_list) - 1,
            )

        self.get_new_list()
        print('Polynomial/Quadratic time: O(n ** 2)')
        self.bubble_sort()

        self.get_new_list()
        print('Exponential time: O(10 ** n)')
        self.bruteforce_the_list()

        self.get_new_list()
        print('calculation = O(1 + n / 2 + 10)')
        self.complex_function()

    def get_new_list(self):
        # note: dont set higher than 10
        sample = list(range(10))
        shuffle(sample)
        self.test_list = sample
        print(f'\nnew list: {self.test_list}')


    # Constant time: O(1)
    def print_val(self, i=1):
        print(self.test_list[i])
        

    # Logarithmic time: O(log n)
    def divide_val(self, i=1):
        while self.test_list[i] > 1:
            self.test_list[i] /= 2
            print(self.test_list[i])


    # Linear time: O(n)
    def print_all_vals(self):
        for val in self.test_list:
            print(val)


    # Linearithmic/Quasilinear time: O(n log n)
    def quick_sort(self, test_list, low, high):
        print(test_list)
        if len(test_list) == 1:
            return test_list
        # note: loop only occurs if condition
        if low < high:
            i = low - 1
            pivot = test_list[high]
            for j in range(low, high):
                if test_list[j] <= pivot:
                    i += 1
                    test_list[i], test_list[j] = test_list[j], test_list[i]
            test_list[i+1], test_list[high] = test_list[high], test_list[i+1]
            self.quick_sort(test_list, low=low, high=i)
            self.quick_sort(test_list, low=i+2, high=high)


    # Polynomial/Quadratic time: O(n ** 2)
    def bubble_sort(self):
        for i in range(len(self.test_list)):
            # note: loops occur regardless of conditions
            for j in range(i+1, len(self.test_list)):
                if self.test_list[j] < self.test_list[i]:
                    self.test_list[j], self.test_list[i] = self.test_list[i], self.test_list[j]
                print(self.test_list)


    # Exponential time: O(10 ** n)
    def bruteforce_the_list(self):
        list_copy = []
        for i in self.test_list:
            for j in range(10):
                print(list_copy)
                if j == i:
                    list_copy.append(j)


    # calculation = O(1 + n / 2 + 10)
    def complex_function(self, i=1):
        '''
        This func prints the first list item: O(1)
        Then prints the first 1/2 of list: O(n/2)
        Then prints an int 10X
        '''

        print(self.test_list[i])

        middle = int(len(self.test_list) / 2)
        for val in self.test_list[:middle]:
            print(val)

        for i in range(10):
            print(i)
