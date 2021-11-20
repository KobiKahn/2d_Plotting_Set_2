import matplotlib.pyplot as plt


############################################################################
# PROBLEM 1

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


# x, y, xlabel, ylabel = open_file('Jacob Kahn - temp_and_pressure.txt')
# plot_data(x, y, 'KOBI\n GRAPH', xlabel, ylabel, '.')

########################################################################################


########################################################################################
### 2


def open_file2(filename):

    data = []

    with open(filename) as file:
        for row in file:
            row = row.split()
            data.append(int(row[0]))

    return data


data = open_file2('Jacob Kahn - test_scores.txt')


def histogram_grade(data):

    bin_locs = [60, 70, 80, 92, 100]



    plt.title('GRADES')

    plt.hist(data, bin_locs)

    plt.show()

# histogram_grade(data)


###############################################################
## PROBLEM 3

def open_file3(filename):

    names = []
    n_sales = []
    tot_sales = []
    x = 0

    with open(filename) as file:
        for row in file:
            x += 1
            row = row.split()

            if x != 1:
                names.append(row[0])
                n_sales.append(int(row[1]))
                tot_sales.append(int(row[2]))
    return names, n_sales, tot_sales


names, n_sales, tot_sales = open_file3('Jacob Kahn - sales_data.txt')


def pie_chart(names, n_sales, tot_sales):




    slice_explode1 = [0,0,0,.1, 0, 0]
    # slice_explode2 = [0, 0, 0, .1, 0, 0]

    plt.subplot(1, 2, 1)

    plt.title('TOTAL SALES')

    plt.pie(n_sales, explode = slice_explode1, labels = names, shadow = True)

    plt.axis('equal')

    plt.subplot(1, 2, 2)

    plt.title('TOTAL DOLLAR AMOUNT')

    plt.pie(tot_sales, explode = slice_explode1, labels = names, shadow = True)

    plt.axis('equal')
    plt.show()


# pie_chart(names, n_sales, tot_sales)

