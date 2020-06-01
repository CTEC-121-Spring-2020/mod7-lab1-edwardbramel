"""
CTEC 121
Eddy
Moduel 7 lab 1
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main():
    # sec 1 define a string
    '''
    myStr = "hello world"

    print()
    print(myStr)
    print(myStr[6])
    print(myStr[len(myStr)-1])
    print(myStr[-5])
    print()
    print(myStr[-len(myStr)])
    """
    word1 = "hello"
    word2 = "world"
    myStr2 = word1 + " " + word2
    print(myStr2)

    print(myStr2[6:len(myStr2)])
'''
    # section 2
    '''
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    print()
    n = int(input("enter a month number (1-12): "))
    pos = (n-1) * 3
    print(pos)
    print()
    monthAbr = months[pos:pos+3]
    print(monthAbr)
    '''
    '''
    # lists
    # create an empty list
    mylist1 = []
    print("mylist: ", mylist1)

    mylist2 = [1, 2, 3, 4, 5]
    print("mylist2:", mylist2)

    mylist3 = [42, "forty-two", 3.14]
    print("mylist3: ", mylist3)

    print("third element of mylist2: ", mylist2[2])

    # initialization example
    for i in range(1, 6):
        mylist1.append(i)
    print("mylist: ", mylist1)

    # illustrate insert()
    mylist1.insert(2, 3.14)
    print("mylist: ", mylist1)
    print()

    # illustrate sort()
    mylist1.sort()
    print("mylist: ", mylist1)
    '''
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    n = int(input("endter a month number: "))
    print(months[n-1])
    print()


main()
