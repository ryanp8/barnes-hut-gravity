import pygame
from config import Config
from body import Body
from node import Node
import math
import random

pygame.init()
screen = pygame.display.set_mode([Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT])

# Initial velocity around a point
def vi(body, cx, cy):
    x = body.x
    y = body.y
    dx = x - cx
    dy = y - cy

    mx = abs(dy)
    my = abs(dx)
    mag = math.sqrt(mx**2 + my**2)
    
    s = 1

    if mag > 0:
    
        if cx < x:
            body.vx = s * -mx / mag
        else:
            body.vx = s * mx / mag
        
        if cy < y:
            body.vy = s * -my / mag
        else:
            body.vy = s * my / mag



def calculate_node_mass(root):

    if not root:
        return 0

    elif root.isLeaf:
        return 0
    
        
    elif root.body:
        root.mass = root.body.mass
        return root.body.mass
        
    else:
        m = 0
        m += calculate_node_mass(root.nw)
        m += calculate_node_mass(root.ne)
        m += calculate_node_mass(root.sw)
        m += calculate_node_mass(root.se)
        root.mass = m
        return m

    
def calculate_center_x(root):
    if not root or not root.mass:
        return 0
    
    if root.body:
        return root.body.x * root.body.mass

    m = 0
    m += calculate_center_x(root.nw)
    m += calculate_center_x(root.ne)
    m += calculate_center_x(root.sw)
    m += calculate_center_x(root.se)

    return m

def calculate_center_y(root):
    if not root or not root.mass:
        return 0
    
    if root.body:
        return root.body.y * root.body.mass

    m = 0
    m += calculate_center_y(root.nw)
    m += calculate_center_y(root.ne)
    m += calculate_center_y(root.sw)
    m += calculate_center_y(root.se)

    return m


def calculate_center_mass(root):
    if root:
        if root.mass:
            root.massx = calculate_center_x(root) / root.mass
            root.massy = calculate_center_y(root) / root.mass
        calculate_center_mass(root.nw)
        calculate_center_mass(root.ne)
        calculate_center_mass(root.sw)
        calculate_center_mass(root.se)


def calculate_net_force(root, body):
    
    if root:
        if root.body and root.body != body:
            d = math.sqrt((root.body.x - body.x)**2 + (root.body.y - body.y)**2)
            body.calculate_force(root.body.x, root.body.y, root.body.mass, d)
        elif not root.isLeaf:
            d = math.sqrt((root.massx - body.x)**2 + (root.massy - body.y)**2)
            if d > 0 and root.width / d < Config.THETA:
                body.calculate_force(root.massx, root.massy, root.mass, d)
            else:
                calculate_net_force(root.nw, body)
                calculate_net_force(root.ne, body)
                calculate_net_force(root.sw, body)
                calculate_net_force(root.se, body)


def draw_bounds(root, screen):
    if root:
        root.draw(screen)
        draw_bounds(root.nw, screen)
        draw_bounds(root.ne, screen)
        draw_bounds(root.sw, screen)
        draw_bounds(root.se, screen)


def insert_tree(root, body, bodies):

    if not root:
        return 

    if root.isLeaf:
        root.body = body
        root.isLeaf = False
    
    elif root.body:
        if abs(root.body.x - body.x) <= 1 and abs(root.body.y - body.y) <= 1:
            if root.body.mass < body.mass:
                # root.body.r = body.r
                root.body.x = body.x
                root.body.y =body.y
                root.body.vx = body.vx
                root.body.vy = body.vy
            root.body.mass += body.mass
            bodies.remove(body)
        else:
            tmp = root.body
            root.body = None
            w = root.width / 2
            x = root.x
            y = root.y
            root.nw = Node(None, x, y, w)
            root.ne = Node(None, x + w, y, w)
            root.se = Node(None, x + w, y + w, w)
            root.sw = Node(None, x, y + w, w)

            insert_tree(root, tmp, bodies)
            insert_tree(root, body, bodies)
    
    else:
        x = root.x
        y = root.y
        width = root.width / 2
        next_check = None
        if body.x >= 0 and body.x <= Config.SCREEN_WIDTH and body.y >= 0 and body.y <= Config.SCREEN_HEIGHT:
            if body.x < x + width:
                if body.y >= y and body.y < y + width:
                    next_check = root.nw
                else:
                    next_check = root.sw
            else:
                if body.y < y + width:
                    next_check = root.ne
                else:
                    next_check = root.se

        insert_tree(next_check, body, bodies)

    return root
    

def main():


    bodies = set()
    # for _ in range(5000):
    #     bodies.add(Body(random.random() * 10, 
    #     Config.SCREEN_WIDTH / 2* random.random(), 
    #     Config.SCREEN_HEIGHT * random.random() / 2))

    
    # for _ in range(1000):
    #     bodies.add(Body(random.random() * 1000, 
    #         Config.SCREEN_WIDTH / 2 + Config.SCREEN_WIDTH / 2 * random.random(), 
    #         Config.SCREEN_HEIGHT / 2 + Config.SCREEN_HEIGHT * random.random() / 2))

    for _ in range(2000):
        bodies.add(Body(random.random() * 1000, 
            Config.SCREEN_WIDTH * random.random(), 
            Config.SCREEN_HEIGHT * random.random()))

    

    # l = [Body(5000, 600, 600), Body(5000, 200, 600), Body(5000, 300, 200), Body(5000, 700, 100), Body(5000, 800, 600)]
    # l = [Body(5000, 600, 600)]



    # for b in l:
    #     bodies.add(b)
    
    sun = Body(100000, 200, 200)
    bodies.add(sun)

    sun2 = Body(100000, 700, 700)
    bodies.add(sun2)

    for body in bodies:
        vi(body, sun.x, sun.y)



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill([0, 0, 0])


        # tree = Tree(Node(None, 0, 0, 800))
        root = Node(None, 0, 0, Config.SCREEN_WIDTH)
        tmp = set(bodies)
        for body in tmp:
            if body in bodies:
                insert_tree(root, body, bodies)
                # tree.insert(body, bodies)
                body.draw(screen)

        # tree.calculate_node_mass()
        # tree.calculate_center_mass()

        calculate_node_mass(root)
        calculate_center_mass(root)

        for body in bodies:
            calculate_net_force(root, body)
            # tree.calculate_net_force()
        
        for body in bodies:
            body.update()
        
        draw_bounds(root, screen)


        pygame.display.update()


if __name__ == '__main__':
    main()