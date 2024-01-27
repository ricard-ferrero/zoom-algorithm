from pygame import Rect as R
from pygame import draw as d

W_WIDTH = 1280
W_HEIGHT = 720
WINDOW = (W_WIDTH, W_HEIGHT)

RECT_WIDTH = 250
RECT_HEIGHT = 100

class Rect():
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

    def re_construct(self, vp): # vp => Vanishing Point (x, y)
        pass

    # Returns a dot coordenates (x,y). It represents
    # one of the 4 corners.
    # Described by
    # row (0=> top corners, 1=> bottom corners)
    # col (0=> left corners, 1=> right corners)
    def __corner(self, row, col):
        if row!=0 and row!=1 or col!=0 and col!=1:
            raise ValueError(f'Corner: incorrect coordenates {self}')
        x = self.left + self.width * col
        y = self.top + self.height * row
        return (x, y)

    def __rect(self):
        # Rect(left, top, width, height)
        return R(self.left, self.top, self.width, self.height)

    def __get_vector(self, vp, corner): # vp => Vanishing Point (x, y)
        X = 0
        Y = 1
        x_vector = corner[X] - vp[X]
        y_vector = corner[Y] - vp[Y]
        return (x_vector, y_vector)

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