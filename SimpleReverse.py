def SimpleReverse(string):
    s=""
    for i in string:
        s=i+s
    return s
if __name__ == '__main__':
    string=input()
    print(SimpleReverse(string))
"""
Simple Reverse
Given a string A, you are asked to reverse the string
 and return the reversed string.
"""