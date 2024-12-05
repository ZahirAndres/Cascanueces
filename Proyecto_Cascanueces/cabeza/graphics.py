"""Basic graphics primitives for OLED display"""
def draw_line(oled, x0, y0, x1, y1, color):
    """Draw a line using Bresenham's algorithm"""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            oled.pixel(x, y, color)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            oled.pixel(x, y, color)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    oled.pixel(x, y, color)

def draw_ellipse(oled, x0, y0, a, b, color):
    """Draw an ellipse using the midpoint algorithm"""
    x = 0
    y = b
    
    # Region 1
    d1 = (b * b) - (a * a * b) + (0.25 * a * a)
    dx = 2 * b * b * x
    dy = 2 * a * a * y
    
    while dx < dy:
        oled.pixel(x0 + x, y0 + y, color)
        oled.pixel(x0 - x, y0 + y, color)
        oled.pixel(x0 + x, y0 - y, color)
        oled.pixel(x0 - x, y0 - y, color)
        
        x += 1
        dx = 2 * b * b * x
        d1 = d1 + dx + (b * b)
        
        if d1 >= 0:
            y -= 1
            dy = 2 * a * a * y
            d1 = d1 - dy
    
    # Region 2
    d2 = ((b * b) * ((x + 0.5) * (x + 0.5))) + \
         ((a * a) * ((y - 1) * (y - 1))) - \
         (a * a * b * b)
         
    while y >= 0:
        oled.pixel(x0 + x, y0 + y, color)
        oled.pixel(x0 - x, y0 + y, color)
        oled.pixel(x0 + x, y0 - y, color)
        oled.pixel(x0 - x, y0 - y, color)
        
        y -= 1
        dy = 2 * a * a * y
        d2 = d2 - dy + (a * a)
        
        if d2 <= 0:
            x += 1
            dx = 2 * b * b * x
            d2 = d2 + dx

def fill_circle(oled, x0, y0, radius, color):
    """Draw a filled circle"""
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if x * x + y * y <= radius * radius:
                oled.pixel(x0 + x, y0 + y, color)