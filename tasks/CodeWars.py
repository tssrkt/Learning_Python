









import matplotlib.colors as colors

def rgb(r, g, b):
    r = 255/1000 if r>255 else r/1000
    g = 255/1000 if g>255 else g/1000
    b = 255/1000 if b>255 else b/1000
    return (colors.rgb2hex([1.0*x/255 for x in (r, g, b)]))[1:]

# print(rgb(0,0,0)) # "000000", "testing zero values")
# print(rgb(1,2,3)) # "010203", "testing near zero values")
# print(rgb(255,255,255)) # "FFFFFF", "testing max values")
# print(rgb(254,253,252)) # "FEFDFC", "testing near max values")
# print(rgb(-20,275,125)) # "00FF7D", "testing out of range values")
