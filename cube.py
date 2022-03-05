class Cube:
    def __init__(self, size=3):
        # scramble state of the cube (default solved)
        self.size = size
        self.faces = 6 # Surfaces on a cube

        self.cube = self._generateCube()
        self.print()

    """
    Generate an NxNxN cube in a solved state

    returns: list of NxN arrays with the color state of each cube face
    """
    def _generateCube(self):
        cube = list()
        color = WHITE # Keep track of colors
        for k in range(0, self.faces):
            face = []
            for i in range(0, self.size):
                face.append([])
                for j in range(0, self.size):
                    face[i].append(color)
            color += 1
            cube.append(face)
        return cube

    def print(self):
        contentSize = 2*self.size + 2 # Size of each face to print (# of characters) 
        prefix = ''
        border = "-" * contentSize
        for k in range(0, self.faces):
            if k == 0 or k == 5:
                prefix = ' ' * contentSize
            else:
                prefix=''
                print("%s" % border, end='')
            for i in range(0, self.size):
                row = "%s|" % (prefix)
                for j in range(0, self.size):
                    row = "%s%i " % (row, self.cube[k][i][j])
                row += "|"
                print(row)

        print("%s%s" % (prefix, border))

# Color constants
WHITE=0
ORANGE=1
GREEn=2
RED=3
BLUE=4
YELLOW=5
