"""Eye drawing and animation functions"""
from time import sleep
from graphics import draw_line, draw_ellipse, fill_circle

def draw_eyelashes(oled, x, y, width):
    """Draw eyelashes around the eye"""
    # Upper eyelashes
    for i in range(-width+10, width-10, 8):
        draw_line(oled, x + i, y - 18, x + i, y - 23, 1)
    
    # Lower eyelashes
    for i in range(-width+10, width-10, 8):
        draw_line(oled, x + i, y + 18, x + i, y + 21, 1)

def draw_eye(oled, x, y, direction=0, blink_state=0, is_right_eye=False):
    """Draw an enhanced eye with eyelids, eyelashes and pupil"""
    oled.fill(0)  # Clear display (black background)
    
    if blink_state == 0:  # Eye fully open
        # Draw outer eye shape (larger ellipse)
        draw_ellipse(oled, x, y, 35, 20, 1)  # 1 = white
        
        # Draw eyelashes
        draw_eyelashes(oled, x, y, 35)
        
        # Calculate pupil position based on direction (same direction for both eyes)
        pupil_offset = direction * 10
        
        # Draw pupil (larger filled circle)
        fill_circle(oled, x + pupil_offset, y, 8, 1)  # White pupil
        
        # Add highlight (small black dot in pupil)
        fill_circle(oled, x + pupil_offset - 3, y - 3, 3, 0)  # 0 = black
    
    elif blink_state == 1:  # Eye partially closed
        draw_ellipse(oled, x, y, 35, 10, 1)
    
    elif blink_state == 2:  # Eye almost closed
        draw_ellipse(oled, x, y, 35, 5, 1)
    
    elif blink_state == 3:  # Eye closed
        # Draw a simple line for closed eye
        draw_line(oled, x - 35, y, x + 35, y, 1)
    
    oled.show()

def draw_both_eyes(oled1, oled2, direction=0, blink_state=0):
    """Draw both eyes simultaneously"""
    draw_eye(oled1, 64, 32, direction, blink_state, False)  # Left eye
    draw_eye(oled2, 64, 32, direction, blink_state, True)   # Right eye

def blink(oled1, oled2):
    """Perform one blink animation for both eyes"""
    # Normal to closed
    for state in [1, 2, 3]:
        draw_both_eyes(oled1, oled2, 0, state)
        sleep(0.05)
    # Closed to normal
    for state in [2, 1, 0]:
        draw_both_eyes(oled1, oled2, 0, state)
        sleep(0.05)