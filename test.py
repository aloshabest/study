def make_decart_point(x, y):
    return {'x': x, 'y': y}

def make_segment(p1, p2):
    start = p1
    end = p2
    return start, end


def get_mid_piont_of_segment(segment):
    start = segment[0]
    end = segment[1]
    x = (start['x'] + end['x']) / 2
    y = (start['y'] + end['y']) / 2

    return {'x': x, 'y': y}


segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
print(get_mid_piont_of_segment(segment))