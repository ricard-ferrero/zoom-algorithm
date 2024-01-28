from pygame import Rect as R
from pygame import draw as d

X = 0
Y = 1

W_WIDTH = 1280
W_HEIGHT = 720
WINDOW = (W_WIDTH, W_HEIGHT)

RECT_WIDTH = 250
RECT_HEIGHT = 100

class Rect():
    FACTOR = 0.1
    def __init__(self, rect_dict):
        self.name = rect_dict['name']
        self.color = rect_dict['color']
        self.init_coordenates = {
            'left': rect_dict['left'],
            'top': rect_dict['top'],
            'width': rect_dict['width'],
            'height': rect_dict['height']
        }
        self.re_init()

    def re_init(self):
        self.left = self.init_coordenates['left']
        self.top = self.init_coordenates['top']
        self.width = self.init_coordenates['width']
        self.height = self.init_coordenates['height']
    
    def draw(self, surface):
        # pg.draw.rect(screen, color, rect_form)
        d.rect(surface, self.color, self.__rect())

    def do_zoom(self, vp, direction): # vp => Vanishing Point (x, y)
        if direction == 'in':
            self.__zoom_it(vp, 1)
        elif direction == 'out':
            self.__zoom_it(vp, -1)
        else:
            raise ValueError(f'DoZoom: direction must be "in" or "out" {self}')


    ### PRIVATE

    # Returns a dot coordenates (x,y). It represents
    # one of the 4 corners.
    # Described by
    # row (0=> top corners, 1=> bottom corners)
    # col (0=> left corners, 1=> right corners)
    def __get_corner(self, row, col):
        if row!=0 and row!=1 or col!=0 and col!=1:
            raise ValueError(f'Corner: incorrect coordenates {self}')
        x = self.left + self.width * col
        y = self.top + self.height * row
        return (x, y)

    def __rect(self):
        # Rect(left, top, width, height)
        return R(int(self.left), int(self.top), int(self.width), int(self.height))

    def __get_vector(self, vp, corner): # vp => Vanishing Point (x, y)
        x = corner[X] - vp[X]
        y = corner[Y] - vp[Y]
        return (x, y)

    def __get_zoom_vector(self, vector, direction):
        x = round(vector[X] * self.FACTOR * direction, 2)
        y = round(vector[Y] * self.FACTOR * direction, 2)
        return (x, y)

    # DoZoom needs only two corners:
    # Corner(0,0) -> to manipulate 'top' and 'left'
    # Corner(1,1) -> to manipulate 'height' and 'width'
    def __zoom_it(self, vp, direction): # vp => Vanishing Point (x, y) | direction: +1=> zoom in, -1=> zoom out
        if direction != 1 and direction != -1:
            raise ValueError(f'Zoom: direction must be 1 or -1 {self}')
        # Get important corners (to manipulate coordinates of the rectangle)
        corner_00 = self.__get_corner(0,0)
        corner_11 = self.__get_corner(1,1)
        # Get important vectors from important corners (to manipulate the coordinates of both corners)
        vector_00 = self.__get_vector(vp, corner_00)
        vector_11 = self.__get_vector(vp, corner_11)
        # Get zoom vectors (are the vectors to increase or decrase the coordinates of both corners)
        z_vector_00 = self.__get_zoom_vector(vector_00, direction)
        z_vector_11 = self.__get_zoom_vector(vector_11, direction)

        # Corner(0,0) => manipulate 'left' and 'top'
        new_left = self.left + z_vector_00[X]
        new_top = self.top + z_vector_00[Y]
        # Corner(1,1) => manipulate 'width' and 'height'
        new_width = (self.left + self.width) + z_vector_11[X] - new_left
        new_height = (self.top + self.height) + z_vector_11[Y] - new_top

        self.left = new_left
        self.top = new_top
        self.width = new_width
        self.height = new_height




rect_red = Rect({
    'name': 'RED',
    'color': (255,0,0),
    'left': W_WIDTH//3 - RECT_WIDTH//2,
    'top': W_HEIGHT//3 - RECT_HEIGHT//2,
    'width': RECT_WIDTH,
    'height': RECT_HEIGHT
})

rect_blue = Rect({
    'name': 'BLUE',
    'color': (0,0,255),
    'left': 2*W_WIDTH//3 - RECT_WIDTH//2,
    'top': W_HEIGHT//3 - RECT_HEIGHT//2,
    'width': RECT_WIDTH,
    'height': RECT_HEIGHT
})

rect_green = Rect({
    'name': 'GREEN',
    'color': (0,255,0),
    'left': W_WIDTH//2 - RECT_WIDTH//2,
    'top': 2*W_HEIGHT//3 - RECT_HEIGHT//2,
    'width': RECT_WIDTH,
    'height': RECT_HEIGHT
})

rects = [rect_red, rect_blue, rect_green]