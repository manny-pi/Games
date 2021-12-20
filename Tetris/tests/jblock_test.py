from sys import path 
path.append("/Users/Omani/Desktop/Personal/Education/Computer Science/Python/Python\
 Projects/PyGame-Projects/Tetris/blocks")

import pygame 
from basicblock import BasicBlock 
from blockattributes import * 
from jblock import JBlock
from pygame import mouse 

# Test the blocks 
def testBlock(): 

    # Initialize pygame 
    pygame.init() 

    # Set game dimensions 
    W, H = 500, 600
    WINDOW = pygame.display.set_mode((W, H), display=0)
    pygame.display.set_caption("jblock_test")
    FRAMES_PER_SECOND = 10
    frames_passed = 0 

    # Create I-Block to test 
    i_init_x, i_init_y = 200, 200
    jblock = JBlock(i_init_x, i_init_y, Color.BLUE, Orientation.UP, 0)
    print(repr(jblock))
    
    # Game clsk 
    clock = pygame.time.Clock() 

    # Game loop
    running = True 
    while running: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

            # Execute if the user left-clicks the mouse 
            if event.type == pygame.MOUSEBUTTONDOWN:
                jblock.changeOrientation()  
                print(jblock)

            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_a: 
                    jblock.goLeft() 

                elif event.key == pygame.K_d:
                    jblock.goRight() 

                print(jblock)
        
        jblock.changeOrientation()  

        # Move the block down
        # - - - - - - - - - -   
        # jblock.goDown() 

        # Clear the window 
        # - - - - - - - - - -   
        WINDOW.fill(Color.BLACK.value)

        # Render graphics 
        # - - - - - - - - - - 
        for block in jblock:     # Render JBlock graphic
            WINDOW.blit(block.surface, (block.x, block.y))
        
        # Update the frame 
        pygame.display.flip() 

        # - - - - - - -
        clock.tick(FRAMES_PER_SECOND)
        frames_passed += 1 

    pygame.quit() 


if __name__ == "__main__":   
    testBlock()
