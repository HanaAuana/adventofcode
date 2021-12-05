input_filename = 'input.txt'

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def __repr__(self) -> str:
        return f'{self.x},{self.y}'


class Line:
    
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        
        self.x_origin = min(self.point_a.x, self.point_b.x)
        self.x_end = max(self.point_a.x, self.point_b.x)

        self.y_origin = min(self.point_a.y, self.point_b.y)
        self.y_end = max(self.point_a.y, self.point_b.y)

        self.max_pos = max(self.x_origin, self.x_end, self.y_origin, self.y_end)
    

    def __repr__(self):
        return f'{self.point_a} -> {self.point_b}'
    
    def get_all_points(self):
        points = []
        
        for x in range(self.x_origin, self.x_end+1):
            for y in range(self.y_origin, self.y_end+1):
                points.append(Point(x, y))
        return points
    
    def is_straight_line(self):
        return self.x_origin == self.x_end or self.y_origin == self.y_end

class Board:
    def __init__(self, lines, side_size):
        self.lines = lines
        self.size = side_size + 1
        self.positions = self.generate_positions()
    
    def __str__(self):
        board_str = ''
        for r in range(self.size):
            row = ''
            for c in range(self.size):
                row += str(self.positions[r][c])
            row += '\n'
            board_str += row
        return board_str

    def generate_positions(self):
        positions = [[0 for i in range(self.size)] for j in range(self.size)]
        for line in self.lines:
            line_points = line.get_all_points()
            for point in line_points:
                positions[point.x][point.y] += 1
        return positions
    
    def get_num_overlaps(self, threshold):
        num_overlaps = 0
        for row in self.positions:
            for pos in row:
                if pos >= threshold:
                    num_overlaps += 1
        return num_overlaps
        

def get_line_from_text(text):
    points = text.split('->')
    x1, y1 = points[0].split(',')
    x2, y2 = points[1].split(',')

    return Line(Point(x1,y1), Point(x2, y2))

all_lines = []
straight_lines = []
max_pos = 0

with open(input_filename) as input_file:
    for line in input_file:
        created_line = get_line_from_text(line)
        if created_line.is_straight_line():
            straight_lines.append(created_line)
            if created_line.max_pos > max_pos:
                max_pos = created_line.max_pos
            

board = Board(straight_lines, max_pos)
print(board.get_num_overlaps(2))


