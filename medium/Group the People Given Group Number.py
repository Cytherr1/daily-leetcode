class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groups = []
        size = 1

        while groupSizes.count(0) != len(groupSizes):

            if size in groupSizes:

                tempGroup = []

                while size in groupSizes:

                    i = groupSizes.index(size)
                    tempGroup.append(i)
                    groupSizes[i] = 0

                    if len(tempGroup) == size:
                        groups.append(tempGroup)
                        tempGroup = []
                
                groups.append(tempGroup)
                
            size += 1

        for i in groups:
            if i == []:
                groups.remove(i)
        
        return groups