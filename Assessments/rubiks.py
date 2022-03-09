class Cube:
    SIDE_COLORS = ['G', 'W', 'B', 'Y', 'O', 'R']

    UP_ROTATION = [0, 1, 2, 3]
    RIGHT_ROTATION = [0, 5, 2, 4]
    SIDE_ROTATION = [4, 5]
    TOP_ROTATION = [1, 3]

    def __init__(self, n : int):
        self.cube = self.get_cube(n)
        self.n = n

    def get_cube(self, n : int):
        return {(side, row, col) : self.SIDE_COLORS[side] for side in range(len(self.SIDE_COLORS)) for row in range(n) for col in range(n)}

    def __str__(self):
        side_output = []

        for side in range(len(self.SIDE_COLORS)):
            face = [[self.cube[(side, row, col)] for col in range(self.n)] for row in range(self.n)]
            side_output.append('\n'.join(str(row) for row in face))

        return '\n\n'.join(side for side in side_output)

    def __rotate_face_right(self, side : int):
        # https://leetcode.com/problems/rotate-image/

        n = self.n

        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = self.cube[(side, n - 1 - j, i)]
                self.cube[(side, n - 1 - j, i)] = self.cube[(side, n - 1 - i, n - j - 1)]
                self.cube[(side, n - 1 - i, n - j - 1)] = self.cube[(side, j, n - 1 - i)]
                self.cube[(side, j, n - 1 - i)] = self.cube[(side, i, j)]
                self.cube[(side, i, j)] = tmp

    def __rotate_face_left(self, side : int):
        assert(side >= 0 and side < len(self.SIDE_COLORS))

        for i in range(len(self.RIGHT_ROTATION) - 1):
            self.__rotate_face_right(side)

    def rotate_up(self, col : int):
        assert(col >= 0 and col < self.n)

        prev_side = self.UP_ROTATION[0]

        for i in range(1, len(self.UP_ROTATION)):
            curr_side = self.UP_ROTATION[i]

            for row in range(self.n):
                self.cube[(prev_side, row, col)], self.cube[(curr_side, row, col)] = self.cube[(curr_side, row, col)], self.cube[(prev_side, row, col)]

        if col == 0:
            self.__rotate_face_right(self.SIDE_ROTATION[0])
        elif col == self.n - 1:
            self.__rotate_face_right(self.SIDE_ROTATION[1])

    def rotate_right(self, row : int):
        assert(row >= 0 and row < self.n)

        prev_side = self.RIGHT_ROTATION[0]

        for i in range(1, len(self.RIGHT_ROTATION)):
            curr_side = self.RIGHT_ROTATION[i]

            for col in range(self.n):
                self.cube[(prev_side, row, col)], self.cube[(curr_side, row, col)] = self.cube[(curr_side, row, col)], self.cube[(prev_side, row, col)]

        if row == 0:
            self.__rotate_face_left(self.TOP_ROTATION[0])
        elif row == self.n - 1:
            self.__rotate_face_left(self.TOP_ROTATION[1])
    
    def rotate_down(self, col : int):
        assert(col >= 0 and col < self.n)

        for i in range(len(self.UP_ROTATION) - 1):
            self.rotate_up(col)
        
    def rotate_left(self, row : int):
        assert(row >= 0 and row < self.n)

        for i in range(len(self.RIGHT_ROTATION) - 1):
            self.rotate_right(row)


def main():
    cube = Cube(3)

    cube.rotate_up(1)
    cube.rotate_right(0)
    cube.rotate_left(2)

    print("Cube:")
    print(cube)

main()
