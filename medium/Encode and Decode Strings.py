class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        code = ":;".join(strs)

        return code

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        strs = str.split(":;")

        return strs
    


    myTuple = ("John", "Peter", "Vicky")

    x = "#".join(myTuple)

    print(x)