import copy

class Solution:
    def __init__(self):
        
        self.orientations = ["N", "E", "S", "W"]

        self.open_file()
        self.init_cursor()

        print(f"The guard will visit \033[95m{self.next_move()+1} \033[0mdistinct positions before leaving the mapped area")



    def open_file(self):
        with open("input", 'r') as file:
            self.data = [line.replace("\n","") for line in file.readlines()]
        self.map = copy.deepcopy([[0 for e in line] for line in self.data])

    def init_cursor(self):
        cursor_line = [line for line in self.data if "^" in line][0]

        lin, col = self.data.index(cursor_line), cursor_line.index("^")

        self.position = lin, col

        self.orientation = "N"

    def get_viewing(self):
        return (self.position[0]+((self.orientation == "S") - 1*(self.orientation == "N")),self.position[1]+((self.orientation == "E") - 1*(self.orientation == "W")))

    def next_move(self):

        out = 0
        while not(out):
            try:
                viewing = self.get_viewing()
                if self.data[viewing[0]][viewing[1]] == "#":
                    # Tourner à droite 
                    self.orientation = self.orientations[(self.orientations.index(self.orientation) + 1 ) % 4]
                else:
                    self.map[self.position[0]][self.position[1]] = 1
                    self.position = viewing
            except Exception as e:
                out = 1

        return sum([sum(line) for line in self.map])


if __name__=="__main__":
    Solution()

