from random import randint

data = []
for i in range(randint(20, 30)):
    data.append(randint(0, 20))

print(data, '\n')
max_data = max(data)

horiz_bar_chart = []
for i in data:
    horiz_bar_chart.append(('█' * i).rjust(max_data))

vert_bar_chart = zip(*horiz_bar_chart)

for el in vert_bar_chart:
    print(''.join(el))

for plank in range(max_data, 0, -1):
    row = str(plank).rjust(3) + ' |'
    for column in range(len(data)):
        if data[column] == plank:
            row += '█'
            # if plank > 3 * max_data // 4:
            #     row += '█'
            # elif plank > 2 * max_data // 4:
            #     row += '▓'
            # elif plank > 1 * max_data // 4:
            #     row += '▒'
            # else:
            #     row += '░'
            data[column] -= 1
        else:
            row += '_'
        row += '|'
    print(row)
