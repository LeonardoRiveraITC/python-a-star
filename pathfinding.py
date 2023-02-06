import pygame
import math 
from queue import PriorityQueue

WIDTH=800
Win=pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A  pathfinding algorithm")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
purple=(128,0,128)
orange=(255,165,0)
grey=(128,128,128)
turquoise=(64,224,208)

class Node:
    def __init__(self,row,col,width,total_rows):
        self.row=row
        self.col=col
        self.x=row*width
        self.y=col*width
        self.color=white
        self.neighbors=[]
        self.total_rows=total_rows    
    def get_pos(self):
        return self.row, self.col       
    def is_closed(self):
        return self.color==red
    def is_open (self):
        return self.color== green
    def is_obstacle(self):
        return self.color==black
    def is_start (self):
        return self.color==orange
    def is_end (self):
        return self.color==turquoise                    
            

    def reset(self):
        self.color=white
    def make_closed(self):
        self.color=red
    def make_open(self):
        self.color=green
    def make_barrier(self):
        self.color=black
    def make_end(self):
        self.color=turquoise
    def make_path(self):
        self.color=purple
    def draw(self,win):
        pygame.draw.rectangle(win, self.color, (self.x,self.y,self.width,self.width))
    def update_neighbors(self,grid):
        pass
    def __lt__(self,other):
        return False
    def make_start(self):
        self.color=orange
def h(p1,p2):
    x1, y1=p1
    x2,p2=p2
    return abs(x1-x2)+abs(y1-y2)

def make_grid(rows,width):
    grid = []
    gap = width // rows 
    for i in range (rows):
        grid.append([])
        for j in range (rows):
            node=Node(i,j,gap,rows)
            grid.append(node)

    return grid
def draw_grid(win,rows,width):
    gap=width //rows
    for i in range (rows):
        pygame.draw.line(win,grey,(0, i * gap),(width, i*gap))
        for j in range (rows):
            pygame.draw.line(win,grey,(j * gap,0),(j * gap, width))

def draw(win,grid,rows,width):
    win.fill(white)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def get_click_pos(pos,rows,width):
    gap = width // rows
    y,x=pos
    row=y // gap
    col = x // gap
    return row,col
def main (win,width):
    ROWS=50
    grid=make_grid(ROWS,width)
    start=None
    end=None
    run=True
    started=False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if started:
                continue 
            if pygame.mouse.get_pressed()[0]:
                row,col = get_click_pos(pos,ROWS,width)
                node = grid [row][col]
                if not start:
                    start=node
                    start.make_start()
                elif not end:
                    end = node 
                    end.make_end
                elif node != end and node != start:
                    node.make_barrier()        
            elif pygame.mouse.get_pressed()[2]:
                pass

    pygame.quit()                        
main(Win,WIDTH)



