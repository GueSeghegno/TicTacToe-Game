import pygame

pygame.init()

S_WIDTH = 600
S_HEIGHT = 600
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
R_SPACE = S_WIDTH // 3
running = True

cross = pygame.image.load("x.png")
o = pygame.image.load("o.png")
cross = pygame.transform.scale(cross, (200, 200))
o = pygame.transform.scale(o, (200, 200))

pygame.display.set_caption("Tic Tac Toe")


def DrawGrid(color):
    x, y = 0, 0

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, color, (x, y, R_SPACE, R_SPACE), 1)
            x += R_SPACE
        y += R_SPACE
        x = 0


def FinalMessageX(text, size):
    font = pygame.font.SysFont("comicsans", size)
    text = font.render(text, 1, (255, 255, 255))
    screen.blit(text, ((S_WIDTH / 2) - (text.get_width()) / 2, (S_HEIGHT / 2) - (text.get_height()) / 2))


class Grid():
    def __init__(self):
        self.grid = [[0 for n in range(3)] for j in range(3)]

    def Print(self):
        for i in self.grid:
            print(i)
        print("\n")

    def ChangeGrid(self, pos, player):
        self.pos = pos[0] // R_SPACE, pos[1] // R_SPACE
        if self.grid[self.pos[1]][self.pos[0]] == 0:
            self.grid[self.pos[1]][self.pos[0]] = player
            return True

    def DrawImages(self, surface):
        if self.grid[self.pos[1]][self.pos[0]] == "x":
            surface.blit(cross, (self.pos[0] * 200, self.pos[1] * 200))
        if self.grid[self.pos[1]][self.pos[0]] == "o":
            surface.blit(o, (self.pos[0] * 200, self.pos[1] * 200))

    def CheckWin(self):
        for i in self.grid:
            if all(x == "x" for x in i):
                return "win X"
            if all(x == "o" for x in i):
                return "win O"  # ok
        for i in range(3):
            if all(x[i] == "x" for x in self.grid):
                return "win X"
        for i in range(3):
            if all(x[i] == "o" for x in self.grid):
                return "win O"
        if all(x[i] == "x" for i, x in enumerate(self.grid)):
            return "win X"
        if all(x[i] == "o" for i, x in enumerate(self.grid)):
            return "win O"
        if all(x[-1 * (i - 2)] == "x" for i, x in enumerate(self.grid)):
            return "win X"
        if all(x[-1 * (i - 2)] == "o" for i, x in enumerate(self.grid)):
            return "win O"
        if all(self.grid[i][j] != 0 for i in range(len(self.grid)) for j in range(3)):
            return "tie"


gridogg = Grid()
player = "x"
color = (255, 255, 255)
game = True
menu = True
while running:
    while menu:
        screen.fill((0, 0, 0))
        FinalMessageX("press space to start", 70)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill((255, 0, 0))
                    menu = False
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    if game:
        DrawGrid(color)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gridogg.ChangeGrid(pos, player):
                if player == "o":
                    player = "x"
                elif player == "x":
                    player = "o"
            gridogg.ChangeGrid(pos, player)
            gridogg.Print()
            gridogg.DrawImages(screen)
            if gridogg.CheckWin() == "win X":
                screen.fill((0, 0, 0))
                color = (0, 0, 0)
                FinalMessageX("Cross Wins", 70)
                game = False
            if gridogg.CheckWin() == "win O":
                screen.fill((0, 0, 0))
                color = (0, 0, 0)
                FinalMessageX("O wins", 70)
                game = False
            if gridogg.CheckWin() == "tie":
                screen.fill((0, 0, 0))
                color = (0, 0, 0)
                FinalMessageX("Tie, you both suck", 70)
                game = False

    pygame.display.update()
