import sys
import random
import time

try:
    import bext, colorama
except ImportError:
    print('Please download bext and colorama')
    sys.exit()


class Drop:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = -1
        self.drop_type = random.randint(0,1)
        self.timeout = random.randint(0,3)
        self.wait_count = random.randint(0,3)

    def renew(self):
        self.__init__()

    def move(self):
        if drop.wait_count < drop.timeout:
            drop.wait_count += 1
            return False
        else:
            drop.wait_count = 0
            drop.y += 1
            return True

    def draw(self):
        if self.drop_type == 1:
            symbol = str(random.randint(1,9))
            con_print(self.x, self.y, GREEN, symbol)
            self.zero_draw()
        else:
            con_print(self.x, self.y, GREEN, ' ')
    
    def zero_draw(self):
        if self.y < height:
            con_print(self.x, self.y+1, LGREEN, '0')


def is_rb_corner(x, y):
    if x == width and y == height:
        return True
    else:
        return False


def con_print(x, y, color, symbol):
    if not is_rb_corner(x, y):
        bext.goto(x, y)
        sys.stdout.write(color)
        print(symbol, end='')


bext.title('Matrix')
bext.clear()
bext.hide()

width, height = bext.size()
width -=1
height -= 1

LGREEN = colorama.Fore.LIGHTGREEN_EX
GREEN =  colorama.Fore.GREEN


drops = []
for i in range(1, width*2//3):
    drop = Drop()
    drops.append(drop)

if __name__ == '__main__':
    while True:
        for drop in drops:
            if drop.move():
                drop.draw()
                if drop.y >= height:
                    drop.renew()
        key = bext.getKey(blocking=False)
        if key == 'esc':
            bext.clear()
            sys.exit()
        time.sleep(0.01)

