import colorgram


rgb_colors =[]
colors = colorgram.extract("dots.webp",15)
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    coloor = (r, g, b)
    rgb_colors.append(coloor)

print(rgb_colors)


