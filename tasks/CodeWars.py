def generate_hashtag(s):
    return a if 2<len(a:='#' + ''.join(map(str.capitalize, s.split())))<141 else False


def first_non_repeating_letter(s):
    return a[0] if len(a:=[x for x in s if (s.lower()).count(x.lower())==1])>0 else ''

#####################################

def mercury(b, trans=False):
    if trans: b = zip(*b)
    for row in b:
        if 0 in row or sum(row)!=45:
            return True
    return False

def valid_solution(board):
    if mercury(board) or mercury(board, True):
        return False
    x, y = 0, 0
    while x<6 and y<7:
        m = sum([sum(row[y:y+3]) for row in board[x:x+3]])
        if m!=45: return False
        y += 3
        if y>6: x, y = x + 3, 0
    return True

# print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#                                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
#                                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
#                                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
#                                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
#                                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                                    [3, 4, 5, 2, 8, 6, 1, 7, 9]]))  # True








