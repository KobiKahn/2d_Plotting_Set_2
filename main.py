import matplotlib.pyplot as plt


def open_file(file_name):
    x_counter = 0
    x = []
    y = []


    with open(file_name) as file:

        for row in file:
            row = row.split()
            x_counter += 1
            if x_counter == 1:
                xlabel = row[0]
                ylabel = row[1]


            else:
                x.append(float(row[0]))
                y.append(float(row[1]))

        return x, y, xlabel, ylabel





def make_rect(cx, cy, width, height):

    y_start = abs((height/2) - cy)
    x_start = abs((width/2) - cx)

    x_coords = [x_start, x_start + width, x_start + width, x_start, x_start]
    y_coords = [y_start, y_start, y_start + height, y_start + height, y_start]

    return x_coords, y_coords

def plot_data(x, y, title, xlabel, ylabel, plot_code):
    counter = 0

    x_num = 0
    y_num = 0

    for int_x in x:
        counter += 1
        x_num += int_x

    for int_y in y:
        y_num += int_y

    x_avg = (x_num / counter)
    y_avg = (y_num / counter)

    centroid = [x_avg, y_avg]

    xmin = min(x)
    xmax = max(x)

    ymin = min(y)
    ymax = max(y)

    user_rect = input('INPUT WIDTH AND HEIGHT FOR RECTANGLE SEPERATED BY A SPACE: ')

    user_rect = user_rect.split()

    user_rect_width = int(user_rect[0])
    user_rect_height = int(user_rect[1])

    width, height = make_rect(x_avg, y_avg, user_rect_width, user_rect_height)

    print(width, height)

    plt.title(f'{title}')

    plt.plot(width, height, '-')

    plt.xlabel = xlabel
    plt.ylabel = ylabel

    plt.plot(x, y, plot_code)

    plt.text(centroid[0], centroid[1], 'Data Centroid')


    plt.axis([xmin, xmax, ymin, ymax])

    plt.show()


## 1b
x, y, xlabel, ylabel = open_file('Jacob Kahn - temp_and_pressure.txt')
plot_data(x, y, 'KOBI\n GRAPH', xlabel, ylabel, '.')


