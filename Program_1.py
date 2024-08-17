
rows = int(input("Rows : "))
cols = int(input("Columns : "))

even_hexagon = [
    " --- ",
    "/   \\",
    "\\   /",
    " --- "
]

odd_hexagon = [
    "   ",
    "___",
    "   ",
    "   "
]

for col in range(cols):
    
    layer_1 = layer_2 = layer_3 = layer_end = ""

    for row in range(rows):
        if row % 2 == 0:
            layer_1 += even_hexagon[0]
            layer_2 += even_hexagon[1]
            layer_3 += even_hexagon[2]
            layer_end += even_hexagon[3]
        else:
            layer_1 += odd_hexagon[0]
            layer_2 += odd_hexagon[1]
            layer_3 += odd_hexagon[2]
            layer_end += odd_hexagon[3]

    # for even number of columns
    if rows % 2 == 0:
        if col < (cols - 1):
            layer_3 += "\\"
        if 1 <= col:
            layer_2 += "/"

    print(layer_1)
    print(layer_2)
    print(layer_3)
    if col == (cols - 1):
        print(layer_end)
