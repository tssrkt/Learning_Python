def loc(position):
    LOCATIONS = {
        (0, 0): lambda: print('This is 0 and 0.'),
        (1, 0): lambda: print('This is 1 and 0.'),
        (1, 1): lambda: print('This is 1 and 1.')
    }

    try:
        location_action = LOCATIONS[position]
    except KeyError:
        print('There is nothing here.')
    else:
        location_action()


