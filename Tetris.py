import pygame, random
pygame.init()

win = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Classic Tetris")
clock = pygame.time.Clock()
run = True
frames = 0
textcolor = [0, 0, 0]
blocksize = 25
lost = False
FPS = 60

shapes = ["I", "Z", "S", "T", "L"]

world = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class Player:
    def __init__(self, shape):
        self.newshape = "I"
        self.color = 2
        self.rotatecount = 0
        self.rect1 = pygame.Rect(150, 25, blocksize, blocksize)
        self.rect2 = pygame.Rect(150, 50, blocksize, blocksize)
        self.rect3 = pygame.Rect(150, 75, blocksize, blocksize)
        self.rect4 = pygame.Rect(150, 100, blocksize, blocksize)
        self.rects = [self.rect1, self.rect2, self.rect3, self.rect4]
        self.pressedr = False
        self.pressedl = False

    def move(self):
        global FPS
        newRects = self.rects
        # MOVING DOWN
        if frames % 60 == 0:
            newRects = []
            for rect in self.rects:
                newRects.append(pygame.Rect(rect.x, rect.y+25, blocksize, blocksize))
            if isPossible(newRects):
                self.rects = newRects
            else:
                self.die()
        # MOVING LEFT AND RIGHT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and not self.pressedl:
            newRects = []
            for rect in self.rects:
                newRects.append(pygame.Rect(rect.x-25, rect.y, blocksize, blocksize))
            if isPossible(newRects):
                self.rects = newRects
                self.pressedl = True

        if keys[pygame.K_d] and not self.pressedr:
            newRects = []
            for rect in self.rects:
                newRects.append(pygame.Rect(rect.x+25, rect.y, blocksize, blocksize))
            if isPossible(newRects):
                self.rects = newRects
                self.pressedr = True

        # SPEEDING UP
        if keys[pygame.K_s]:
            FPS = 600
        else:
            FPS = 60

        if frames % 30 == 0:
            self.pressedr = False
            self.pressedl = False

    def rotate(self):
        pass

    def die(self):
        for rect in self.rects:
            world[rect.y//25][rect.x//25] = self.color
        self.newshape = shapes[random.randint(0, len(shapes)-1)]
        # RESPAWNING AS NEW SHAPE AT TOP
        if self.newshape == "I":
            self.rect1 = pygame.Rect(150, 25, blocksize, blocksize)
            self.rect2 = pygame.Rect(150, 50, blocksize, blocksize)
            self.rect3 = pygame.Rect(150, 75, blocksize, blocksize)
            self.rect4 = pygame.Rect(150, 100, blocksize, blocksize)
            self.rects = [self.rect1, self.rect2, self.rect3, self.rect4]
            self.color = 2
            self.rotatecount = 0
        if self.newshape == "L":
            self.rect1 = pygame.Rect(150, 25, blocksize, blocksize)
            self.rect2 = pygame.Rect(150, 50, blocksize, blocksize)
            self.rect3 = pygame.Rect(150, 75, blocksize, blocksize)
            self.rect4 = pygame.Rect(125, 75, blocksize, blocksize)
            self.rects = [self.rect1, self.rect2, self.rect3, self.rect4]
            self.color = 3
            self.rotatecount = 0
        if self.newshape == "T":
            self.rect1 = pygame.Rect(150, 25, blocksize, blocksize)
            self.rect2 = pygame.Rect(150, 50, blocksize, blocksize)
            self.rect3 = pygame.Rect(125, 25, blocksize, blocksize)
            self.rect4 = pygame.Rect(175, 25, blocksize, blocksize)
            self.rects = [self.rect1, self.rect2, self.rect3, self.rect4]
            self.color = 4
            self.rotatecount = 0
        if self.newshape == "S":
            self.rect1 = pygame.Rect(150, 25, blocksize, blocksize)
            self.rect2 = pygame.Rect(150, 50, blocksize, blocksize)
            self.rect3 = pygame.Rect(125, 50, blocksize, blocksize)
            self.rect4 = pygame.Rect(125, 25, blocksize, blocksize)
            self.rects = [self.rect1, self.rect2, self.rect3, self.rect4]
            self.color = 5
            self.rotatecount = 0
        if self.newshape == "Z":
            self.rect1 = pygame.Rect(150, 25, blocksize, blocksize)
            self.rect2 = pygame.Rect(150, 50, blocksize, blocksize)
            self.rect3 = pygame.Rect(125, 25, blocksize, blocksize)
            self.rect4 = pygame.Rect(175, 50, blocksize, blocksize)
            self.rects = [self.rect1, self.rect2, self.rect3, self.rect4]
            self.color = 6
            self.rotatecount = 0

    def draw(self):
        if not lost:
            for rect in self.rects:
                if self.color == 2:
                    pygame.draw.rect(win, (255, 0, 0), (rect.x, rect.y, blocksize, blocksize))
                    pygame.draw.rect(win, (200, 200, 200), (rect.x, rect.y, blocksize, blocksize), width=1)
                elif self.color == 3:
                    pygame.draw.rect(win, (0, 255, 0), (rect.x, rect.y, blocksize, blocksize))
                    pygame.draw.rect(win, (200, 200, 200), (rect.x, rect.y, blocksize, blocksize), width=1)
                elif self.color == 4:
                    pygame.draw.rect(win, (0, 0, 255), (rect.x, rect.y, blocksize, blocksize))
                    pygame.draw.rect(win, (200, 200, 200), (rect.x, rect.y, blocksize, blocksize), width=1)
                elif self.color == 5:
                    pygame.draw.rect(win, (128, 0, 128), (rect.x, rect.y, blocksize, blocksize))
                    pygame.draw.rect(win, (200, 200, 200), (rect.x, rect.y, blocksize, blocksize), width=1)
                elif self.color == 6:
                    pygame.draw.rect(win, (0, 255, 255), (rect.x, rect.y, blocksize, blocksize))
                    pygame.draw.rect(win, (200, 200, 200), (rect.x, rect.y, blocksize, blocksize), width=1)
        else:
            for rect in self.rects:
                pygame.draw.rect(win, (255, 255, 255), (rect.x, rect.y, blocksize, blocksize))

P = Player("L")


def drawWorld():
    ycounter = 0
    for row in world:
        xcounter = 0
        for tile in row:
            if tile == 1:
                pygame.draw.rect(win, (0, 0, 0), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize))
                pygame.draw.rect(win, (200, 200, 200), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize), width=1)
            elif tile == 2:
                pygame.draw.rect(win, (255, 0, 0), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize))
                pygame.draw.rect(win, (200, 200, 200), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize), width=1)
            elif tile == 3:
                pygame.draw.rect(win, (0, 255, 0), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize))
                pygame.draw.rect(win, (200, 200, 200), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize), width=1)
            elif tile == 4:
                pygame.draw.rect(win, (0, 0, 255), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize))
                pygame.draw.rect(win, (200, 200, 200), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize), width=1)
            elif tile == 5:
                pygame.draw.rect(win, (128, 0, 128), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize))
                pygame.draw.rect(win, (200, 200, 200), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize), width=1)
            elif tile == 6:
                pygame.draw.rect(win, (0, 255, 255), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize))
                pygame.draw.rect(win, (200, 200, 200), (xcounter*blocksize, ycounter*blocksize, blocksize, blocksize), width=1)
            xcounter += 1
        ycounter += 1
    pygame.draw.line(win, (200, 200, 200), (0, 125), (300, 125))


def isPossible(rects):
    """Returns whether or not a set of blocks (here used to mimic the new movement of a block) interferes with the world"""
    ycounter = 0
    for row in world:
        xcounter = 0
        for tile in row:
            if not tile == 0:
                for rect in rects:
                    if rect.x / 25 == xcounter and rect.y / 25 == ycounter:
                        return False
            xcounter += 1
        ycounter += 1
    return True


def textOnScreen(x, y, text1, text2, big, color=(220, 200, 200)):
    font = pygame.font.Font('freesansbold.ttf', big)
    txt = str(text1) + str(text2)
    text = font.render(txt, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    win.blit(text, textRect)


def isLost():
    global lost
    for i in world[4]:
        if i > 1:
            lost = True
            textOnScreen(150, 90, "GAME OVER", "", 30, color=(255, 0, 0))


def placeLower(r):
    """Places a given row in the world data list one row lower (shifts a row of blocks down into empty row)"""
    global world
    counter = 0
    for i in world[r]:
        if not i == 0:
            world[r + 1][counter] = i
        counter += 1
    for j in range(1, len(world[r])-1):
        world[r][j] = 0


def findPlace(s, lst):
    """returns the place something is given in a list"""
    counter = 0
    for i in lst:
        if i == s:
            return counter
        else:
            counter += 1


def isRowFull():
    """Checks if a row of blocks is full and if it is it clears it out"""
    global pushDown
    # Getting a copy of the world data without the walls, top and bottom
    worldcopy = []
    for i in range(1, len(world)-1):
        worldcopy.append(world[i])

    rowcount = 0
    for row in worldcopy:
        count = 0
        for i in row:
            if not i == 0:
                count += 1
        if count == 12: # Full row of blocks
            for i in range(1, len(row)-1):
                row[i] = 0

            while not rowcount == 1:
                placeLower(rowcount)
                rowcount -= 1

        rowcount += 1


def redrawWin():
    global frames
    if not lost:
        win.fill((255, 255, 255))
        drawWorld()
        P.move(), P.rotate()
        isRowFull()
    P.draw()
    isLost()
    pygame.display.update()
    frames += 1


def main():
    global run
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if run:
            redrawWin()


main()
