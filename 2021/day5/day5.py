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
        
        self.x_origin = self.point_a.x
        self.x_end = self.point_b.x

        self.y_origin = self.point_a.y
        self.y_end = self.point_b.y

        self.max_pos = max(self.x_origin, self.x_end, self.y_origin, self.y_end)
    

    def __repr__(self):
        return f'{self.point_a} -> {self.point_b}'
    
    def get_all_points(self):
        points = []

        start_x = self.x_origin
        stop_x = self.x_end

        start_y = self.y_origin
        stop_y = self.y_end

        if self.is_straight_line():
            if start_x > stop_x:
                print('swapping points')
                start_x, stop_x, = stop_x, start_x
            if start_y > stop_y:
                start_y, stop_y = stop_y, start_y
            
            slope = 1
            print(f'{start_x},{start_y} to {stop_x},{stop_y}')
            for x in range(start_x, stop_x + 1):
                for y in range(start_y, stop_y + 1):
                    points.append(Point(x, y))
            print(points)
        else:
            print('finding for diagonal line')
            print(start_x)
            print(stop_x)
            if start_x > stop_x:
                print('swapping points')
                start_x, stop_x, = stop_x, start_x
                start_y, stop_y = stop_y, start_y
            
            slope = (stop_y - start_y) // (stop_x - start_x)
            print(f'{start_x},{start_y} to {stop_x},{stop_y}')
            for x, y in zip(range(start_x, stop_x), range(start_y, stop_y, slope)):
                points.append(Point(x, y))
            points.append(Point(stop_x, stop_y))

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
print(board)
print(board.get_num_overlaps(2))


all_lines = []
max_pos = 0
with open(input_filename) as input_file:
    for line in input_file:
        created_line = get_line_from_text(line)
        all_lines.append(created_line)
        if created_line.max_pos > max_pos:
            max_pos = created_line.max_pos

# for line in all_lines:
    # print(line)
    # print(line.get_all_points())

full_board = Board(all_lines, max_pos)
print(full_board)
print(full_board.get_num_overlaps(2))