# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # 这道题其实不难。就是把matrix 变形一下。
        # 值得注意的有以下几点：
        # 1. 因为matrix 在backtrace的时候没有这么麻烦，直接reset x,y的坐标就好。但是这里必须要有一个reset的过程。就是robot 要转180度然后move一个格子，再转180度。这样reset回之前的状态
        # 2. 这里面非常巧妙的一个地方是m_x, m_y = -m_y, m_x， 经过4个rotation，正好的把四个方向有rotate一遍。从(0, 1)开始每次向左转。经过四次 swap。正好是四个方向。所以初始的m_x, m_y 必须是 (0, 1) 而且swap前要turn left
        
        def reset_move(robot):
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        
        def dfs(robot, visited, x, y, m_x, m_y):
            robot.clean()
            visited.add((x, y))
            
            for _ in range(4):
                n_x = x + m_x
                n_y = y + m_y
                
                if (n_x, n_y) not in visited and robot.move():
                    dfs(robot, visited, n_x, n_y, m_x, m_y)
                    reset_move(robot)
                
                robot.turnLeft()
                m_x, m_y = -m_y, m_x
        
        dfs(robot, set(), 0, 0, 0, 1)