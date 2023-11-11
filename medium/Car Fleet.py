class Solution:
    def carFleet(self, target, position, speed):

        n = len(position)
        stack = []

        posSpeed = [(position[i], speed[i]) for i in range(n)]
        posSpeed.sort(key = lambda x: x[0], reverse=True)

        for i in posSpeed:

            time = (target - i[0]) / i[1]
        
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)


        
    



