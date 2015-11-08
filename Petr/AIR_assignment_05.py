import copy

class puzzle:
    def __init__(self):
        self.state = [[1,4,8],[3,6,2],[0,5,7]]
        self.goal = tuple([[1,2,3],[4,5,6],[7,8,0]])
        self.position = [2,0]
    def move(self,direction): # move empty block
        try:
            if direction =="up":
                buf = self.state[self.position[0]-1][self.position[1]]
                self.state[self.position[0]-1][self.position[1]] = 0
                self.state[self.position[0]][self.position[1]] = buf
                self.position = [self.position[0]-1, self.position[1]]
            elif direction =="down":
                buf = self.state[self.position[0]+1][self.position[1]]
                self.state[self.position[0]+1][self.position[1]] = 0
                self.state[self.position[0]][self.position[1]] = buf
                self.position = [self.position[0]+1, self.position[1]]
            elif direction =="right":
                buf = self.state[self.position[0]][self.position[1]+1]
                self.state[self.position[0]][self.position[1]+1] = 0
                self.state[self.position[0]][self.position[1]] = buf
                self.position = [self.position[0], self.position[1]+1]
            elif direction =="left":
                buf = self.state[self.position[0]][self.position[1]-1]
                self.state[self.position[0]][self.position[1]-1] = 0
                self.state[self.position[0]][self.position[1]] = buf
                self.position = [self.position[0], self.position[1]-1]
        except IndexError:

            pass




    def search_greedy(self):
        next_state = self.state
        heuristics = [100,100,100,100]
        i = 0

        while next_state != []:
            tmp = next_state

            if next_state == self.goal:
                print "success!"
                return 0

            if (self.position[0]> 0 ):
                self.move("up")
                heuristics[0] = self.heuristic(self.state)
                self.move("down")

            else:
                heuristics[0] = 100

            if (self.position[0] < 2  ):
                self.move("down")
                heuristics[1] = self.heuristic(self.state)
                self.move("up")
            else:
                heuristics[1] = 100

            if (self.position[1] < 2  ):
                self.move("right")
                heuristics[2] = self.heuristic(self.state)
                self.move("left")
            else:
                heuristics[2] = 100

            if (self.position[1] > 0  ):
                self.move("left")
                heuristics[3] = self.heuristic(self.state)
                self.move("right")
            else:
                heuristics[3] = 100

            min_index = heuristics.index(min(heuristics))
            print "heur "+ str(heuristics)
            if min_index == 0:
                self.move("up")
            elif min_index ==1:
                self.move("down")
            elif min_index == 2:
                self.move("right")
            elif min_index == 3:
                self.move("left")
            else:
                continue
                
            heuristics = [100,100,100,100]
            i = i + 1
            
            print i
            print self.state
            next_state = self.state



    def heuristic(self,state):
        h = 0
        for row in range(3):
            for col in range(3):
                if state[row][col] != self.goal[row][col]:
                    h = h + 1
        return h
















if __name__ == '__main__':
    board = puzzle()
    board.search_greedy()
