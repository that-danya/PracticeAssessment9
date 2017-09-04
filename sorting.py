#Sorting


def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    # identify where to stop in range of list while looping
    # identify swaping count variable
    counter = 1
    swap = False

    # while counter is less than list, continue looping
    while counter < len(lst):
        # loop, switching larger to right most position
        for i in range(len(lst) - counter):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True
        # remove sorted items from what to check by decreasing range
        # if swap occurred
        if swap:
            counter += 1
        # if no swap occurred, return lst + win faster
        else:
            return lst

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    # empty list to append to
    new_list = []

    # compare while there is stuff to append in either lists
    while len(list1) > 0 or len(list2) > 0:
        # if one list is empty, append rest of remaining list
        if list1 == []:
            new_list.append(list2.pop(0))
        elif list2 == []:
            new_list.append(list1.pop(0))
        # append the smaller number to new list
        elif list1[0] < list2[0]:
            new_list.append(list1.pop(0))
        else:
            new_list.append(list2.pop(0))

    return new_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    # base case
    if len(lst) < 2:
        return lst

    # find mid point of list + divide into 2 lists
    mid = len(lst)/2
    lista = lst[:mid]
    listb = lst[mid:]

    # recruse both
    return merge_lists(merge_sort(lista), merge_sort(listb))


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
