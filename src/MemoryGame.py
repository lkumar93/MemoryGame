#
# THIS IS AN IMPLEMENTATION OF THE CLASSIC MEMORY GAME IN 2D
#
# COPYRIGHT BELONGS TO THE AUTHOR OF THIS CODE
#
# AUTHOR : LAKSHMAN KUMAR
# AFFILIATION : UNIVERSITY OF MARYLAND, MARYLAND ROBOTICS CENTER
# EMAIL : LKUMAR93@UMD.EDU
# LINKEDIN : WWW.LINKEDIN.COM/IN/LAKSHMANKUMAR1993
#
# THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THE MIT LICENSE
# THE WORK IS PROTECTED BY COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF
# THE WORK OTHER THAN AS AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.
# 
# BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO
# BE BOUND BY THE TERMS OF THIS LICENSE. THE LICENSOR GRANTS YOU THE RIGHTS
# CONTAINED HERE IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND
# CONDITIONS.
#


###########################################
##
##	LIBRARIES
##
###########################################

# implementation of card game - Memory

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

###########################################
##
##	VARIABLES
##
###########################################

exposed = []  
first = 0
second = 0
three = False
numbers = [ 0, 1 ,2 ,3 ,4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13, 14 ,15 ] 


###########################################
##
##	FUNCTIONS
##
###########################################

# helper function to initialize globals
def new_game():
    global exposed , state , turn , memory_deck
    turn = 0
    state = 0
    random.shuffle(memory_deck)
    label.set_text('Turns = ' + str (turn))
    exposed = [ False , False,False ,False ,False ,False ,False ,False ,False ,False ,False ,False ,False ,False ,False ,False  ]
    pass  

     
# define event handlers
def mouseclick(pos):
    # game state logic
    
    global exposed , state , list ,turn , first , second
    if state == 0:
        state = 1
        for n in numbers:
            if exposed[n] == False :
                if pos[0] >=  (52*n) and pos[0] <= (50 + 52*n) :
                    exposed[n] = True
                    first = n
    elif state == 1: 
        state = 2
        for n in numbers:
            if exposed[n] == False :
                if pos[0] >=  (52*n) and pos[0] <= (50 + 52*n) :
                    exposed[n] = True
                    second = n
    else:
        
        if memory_deck[first] == memory_deck[second]:
            pass
        
        else :           
            exposed[first]=False
            exposed[second] = False
         
        turn += 1
        label.set_text('Turns = ' + str (turn))
        state = 1
        for n in numbers:
            if exposed[n] == False:                
                if pos[0] >=  (52*n) and pos[0] <= (50 + 52*n) :
                    exposed[n] = True
                    first = n
                 
# cards are logically 50x100 pixels in size  

def draw(canvas):
    
    m = 0
    global exposed
    
    for n in numbers:
        canvas.draw_polygon([(0 + (52*n) , 0 ), (0 + (52*n), 100),(50 + (52*n),100) , (50 + (52*n), 0)], 1, 'Green','Green')
        
    for l in memory_deck:
        if exposed[m] is True:
            canvas.draw_polygon([(0 + (52*m) , 0 ), (0 + (52*m), 100),(50 + (52*m),100) , (50 + (52*m), 0)], 1, 'Black','Black')
            canvas.draw_text(str(l), (25 +(52*m), 50), 20, 'White')
        m += 1
        
  
    
###########################################
##
##	MAIN FUNCTION
##
###########################################	

if __name__ == '__main__':    
  	    
	# create frame and add a button and labels
	frame = simplegui.create_frame("Memory", 835, 100)
	frame.add_button("Reset", new_game)
	label = frame.add_label("Turns = 0")

	# register event handlers
	frame.set_mouseclick_handler(mouseclick)
	frame.set_draw_handler(draw)

	memory_deck = range(8)
	memory_deck.extend(memory_deck)

	# get things rolling
	new_game()
	frame.start()


