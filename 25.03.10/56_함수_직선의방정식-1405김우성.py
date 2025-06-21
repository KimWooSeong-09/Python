def get_data():
    a1, b1 = map(int, input("(x1, y1) : ").split())
    a2, b2 = map(int, input("(x2, y2) : ").split())
    return a1, b1, a2, b2

def get_line(a1, b1, a2, b2):
    if a1 == a2:
        result = print(f'x = {a1}')
    else:
        slp = (b2 - b1) / (a2 - a1)
        y_i = b1 - slp * a1
        result = print(f'y = {slp}x + ({y_i})')
    return result

# Main
a = get_data()
line = get_line(*a)