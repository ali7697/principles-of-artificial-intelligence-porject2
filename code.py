# reading the inputs
from copy import deepcopy

infile = r"E:\educational\9th Semester\AI\proj\proj2\16.txt"
numbers = []
colors = []
with open(infile) as f:
    m, n = [int(inp) for inp in next(f).split()]
    initial_domain_color = [inp for inp in next(f).split()]
    for i in range(n):
        tmp_colors = []
        tmp_numbers = []
        row = [inp for inp in next(f).split()]
        for j in range(n):
            if row[j][0] != '*':
                a = int(row[j][0])
            else:
                a = row[j][0]
            tmp_numbers.append(a)
            tmp_colors.append(row[j][1])
        numbers.append(tmp_numbers)
        colors.append(tmp_colors)
first_numbers = deepcopy(numbers)
first_colors = deepcopy(colors)
num_degree = []
num_domain = []
color_degree = []
color_domain = []
initial_domain_num = [i for i in range(1, n + 1)]
numbers_array = []
colors_array = []
used_num_domain = []
used_domain_indexes_colors = []
used_indexes = []
used_color_indexes = []
used_color_domain = []
types = []
used_num_degree = []
used_color_degree = []
used_domain_indicator = []
parents = []
used_ind_and_types = []
num_domain_array = []
color_domain_array = []
color_degree_array = []
num_degree_array = []
go_back_counter = 0


# Initializing the domains and degrees
def update_num_degree():
    global num_degree
    num_degree = []
    for i in range(n):
        tmp_num_degree = []
        for j in range(n):
            if numbers[i][j] == '*':
                count = 0
                # checking the rows and columns
                for k in range(n):
                    if numbers[i][k] == '*':
                        count += 1
                    if numbers[k][j] == '*':
                        count += 1
                count = count - 2
                count = [count]
            else:
                count = []
            tmp_num_degree.append(count)
        num_degree.append(tmp_num_degree)


def update_num_domain():
    global num_domain
    num_domain = []
    for i in range(n):
        tmp_num_domain = []
        for j in range(n):
            domain = deepcopy(initial_domain_num)
            if numbers[i][j] == '*':
                for k in range(n):
                    if numbers[i][k] in domain:
                        domain.remove(numbers[i][k])
                    if numbers[k][j] in domain:
                        domain.remove(numbers[k][j])
            else:
                domain = []
            if numbers[i][j] == '*' and i - 1 >= 0:
                # the house doesn't have a number but has a color
                if colors[i - 1][j] != '#':
                    if colors[i - 1][j] == initial_domain_color[0] and numbers[i - 1][j] != '*':
                        for z in range(numbers[i - 1][j], n + 1):
                            if z in domain:
                                domain.remove(z)
                    if colors[i - 1][j] == initial_domain_color[-1] and numbers[i - 1][j] != '*':
                        for z in range(0, numbers[i - 1][j]):
                            if z in domain:
                                domain.remove(z)
                    if colors[i - 1][j] != '#' and colors[i][j] != '#' and numbers[i - 1][j] != '*':
                        if initial_domain_color.index(colors[i - 1][j]) < initial_domain_color.index(colors[i][j]):
                            ind = numbers[i-1][j]
                            for k in range(ind, n+1):
                                if k in domain:
                                    domain.remove(k)
                        elif initial_domain_color.index(colors[i - 1][j]) > initial_domain_color.index(colors[i][j]):
                            ind = numbers[i-1][j]
                            for k in range(1, ind):
                                if k in domain:
                                    domain.remove(k)

            if numbers[i][j] == '*' and i + 1 < n:
                if colors[i + 1][j] != '#':
                    if colors[i + 1][j] == initial_domain_color[0] and numbers[i + 1][j] != '*' :
                        for z in range(numbers[i + 1][j], n + 1):
                            if z in domain:
                                domain.remove(z)
                    if colors[i + 1][j] == initial_domain_color[-1] and numbers[i + 1][j] != '*':
                        for z in range(0, numbers[i + 1][j]):
                            if z in domain:
                                domain.remove(z)
                    if colors[i + 1][j] != '#' and colors[i][j] != '#' and numbers[i + 1][j] != '*':
                        if initial_domain_color.index(colors[i + 1][j]) < initial_domain_color.index(colors[i][j]):
                            ind = numbers[i + 1][j]
                            for k in range(ind, n + 1):
                                if k in domain:
                                    domain.remove(k)
                        elif initial_domain_color.index(colors[i + 1][j]) > initial_domain_color.index(colors[i][j]):
                            ind = numbers[i + 1][j]
                            for k in range(1, ind):
                                if k in domain:
                                    domain.remove(k)

            if numbers[i][j] == '*' and j - 1 >= 0:
                if colors[i][j - 1] != '#':
                    if colors[i][j - 1] == initial_domain_color[0] and numbers[i][j - 1] != '*':
                        for z in range(numbers[i][j - 1], n + 1):
                            if z in domain:
                                domain.remove(z)
                    if colors[i][j - 1] == initial_domain_color[-1] and numbers[i][j - 1] != '*':
                        for z in range(0, numbers[i][j - 1]):
                            if z in domain:
                                domain.remove(z)
                    if colors[i][j-1] != '#' and colors[i][j] != '#' and numbers[i][j - 1] != '*':
                        if initial_domain_color.index(colors[i][j - 1]) < initial_domain_color.index(colors[i][j]):
                            ind = numbers[i][j - 1]
                            for k in range(ind, n + 1):
                                if k in domain:
                                    domain.remove(k)
                        elif initial_domain_color.index(colors[i][j - 1]) > initial_domain_color.index(colors[i][j]):
                            ind = numbers[i][j - 1]
                            for k in range(1, ind):
                                if k in domain:
                                    domain.remove(k)

            if numbers[i][j] == '*' and j + 1 < n:
                if colors[i][j + 1] != '#':
                    if colors[i][j + 1] == initial_domain_color[0] and numbers[i][j + 1] != '*':
                        for z in range(numbers[i][j + 1], n + 1):
                            if z in domain:
                                domain.remove(z)
                    if colors[i][j + 1] == initial_domain_color[-1] and numbers[i][j + 1] != '*':
                        for z in range(0, numbers[i][j + 1]):
                            if z in domain:
                                domain.remove(z)
                    if colors[i][j+1] != '#' and colors[i][j] != '#' and numbers[i][j + 1] != '*':
                        if initial_domain_color.index(colors[i][j + 1]) < initial_domain_color.index(colors[i][j]):
                            ind = numbers[i][j + 1]
                            for k in range(ind, n + 1):
                                if k in domain:
                                    domain.remove(k)
                        elif initial_domain_color.index(colors[i][j + 1]) > initial_domain_color.index(colors[i][j]):
                            ind = numbers[i][j + 1]
                            for k in range(1, ind):
                                if k in domain:
                                    domain.remove(k)
            tmp_num_domain.append(domain)
        num_domain.append(tmp_num_domain)


def update_color_degree():
    global color_degree
    color_degree = []
    for i in range(n):
        tmp_color_degree = []
        for j in range(n):
            if colors[i][j] == '#':
                count = 0
                # checking the rows and columns
                if i - 1 >= 0:
                    if colors[i - 1][j] == '#':
                        count += 1
                if i + 1 <= n - 1:
                    if colors[i + 1][j] == '#':
                        count += 1
                if j - 1 >= 0:
                    if colors[i][j - 1] == '#':
                        count += 1
                if j + 1 <= n - 1:
                    if colors[i][j + 1] == '#':
                        count += 1
                count = [count]
            else:
                count = []
            tmp_color_degree.append(count)
        color_degree.append(tmp_color_degree)


def update_color_domain():
    global color_domain
    color_domain = []
    for i in range(n):
        tmp_color_domain = []
        for j in range(n):
            if colors[i][j] == '#':
                domain = deepcopy(initial_domain_color)
                # checking the rows and columns
                if i - 1 >= 0:
                    if colors[i - 1][j] in domain:
                        domain.remove(colors[i - 1][j])
                    # the house doesn't have a color but has a number
                    if numbers[i - 1][j] != '*' and numbers[i][j] != '*' and colors[i-1][j] != '#':
                        if numbers[i - 1][j] < numbers[i][j]:
                            ind = initial_domain_color.index(colors[i - 1][j])
                            for k in range(ind + 1, m):
                                if initial_domain_color[k] in domain:
                                    domain.remove(initial_domain_color[k])
                        elif numbers[i - 1][j] > numbers[i][j]:
                            ind = initial_domain_color.index(colors[i - 1][j])
                            for k in range(ind):
                                if initial_domain_color[k] in domain:
                                    domain.remove(initial_domain_color[k])

                if i + 1 <= n - 1:
                    if colors[i + 1][j] in domain:
                        domain.remove(colors[i + 1][j])
                    if numbers[i + 1][j] != '*' and numbers[i][j] != '*' and colors[i+1][j] != '#':
                        if numbers[i + 1][j] < numbers[i][j]:
                            ind = initial_domain_color.index(colors[i + 1][j])
                            for k in range(ind + 1, m):
                                if initial_domain_color[k] in domain:
                                    domain.remove(initial_domain_color[k])
                        elif numbers[i + 1][j] > numbers[i][j]:
                            ind = initial_domain_color.index(colors[i + 1][j])
                            for k in range(ind):
                                if initial_domain_color[k] in domain:
                                    domain.remove(initial_domain_color[k])
                if j - 1 >= 0:
                    if colors[i][j - 1] in domain:
                        domain.remove(colors[i][j - 1])
                    if numbers[i][j - 1] != '*' and numbers[i][j] != '*' and colors[i][j - 1] != '#':
                        if numbers[i][j - 1] < numbers[i][j]:
                            ind = initial_domain_color.index(colors[i][j - 1])
                            for k in range(ind + 1, m):
                                if initial_domain_color[k] in domain:
                                    domain.remove(initial_domain_color[k])
                        elif numbers[i][j - 1] > numbers[i][j]:
                            ind = initial_domain_color.index(colors[i][j - 1])
                            for k in range(ind):
                                if initial_domain_color[k] in domain:
                                    domain.remove(initial_domain_color[k])

                if j + 1 <= n - 1:
                    if colors[i][j + 1] in domain:
                        domain.remove(colors[i][j + 1])
                    if numbers[i][j + 1] != '*' and numbers[i][j] != '*' and colors[i][j + 1] != '#':
                        if numbers[i][j + 1] < numbers[i][j]:
                            ind = initial_domain_color.index(colors[i][j + 1])
                            for k in range(ind + 1, m):
                                if initial_domain_color[k] in domain:
                                    domain.remove(initial_domain_color[k])
                        elif numbers[i][j + 1] > numbers[i][j]:
                            ind = initial_domain_color.index(colors[i][j + 1])
                            for k in range(ind):
                                if initial_domain_color[k] in domain:
                                    domain.remove(initial_domain_color[k])
            else:
                domain = []
            tmp_color_domain.append(domain)
        color_domain.append(tmp_color_domain)


def update_all():
    update_num_degree()
    update_num_domain()
    update_color_degree()
    update_color_domain()


def find_mrv_indexes_numbers():
    min_domain = 1000
    indexes = []
    for i in range(n):
        for j in range(n):
            if len(num_domain[i][j]) > 0:
                if len(num_domain[i][j]) < min_domain:
                    min_domain = len(num_domain[i][j])
                    indexes = [[i, j]]
                else:
                    if len(num_domain[i][j]) == min_domain:
                        indexes.append([i, j])
    return indexes


def find_mrv_indexes_colors():
    min_domain = 1000
    indexes = []
    for i in range(n):
        for j in range(n):
            if len(color_domain[i][j]) < min_domain and len(color_domain[i][j]) > 0:
                min_domain = len(color_domain[i][j])
                indexes = [[i, j]]
            else:
                if len(color_domain[i][j]) == min_domain:
                    indexes.append([i, j])
    return indexes


def find_degree_indexes_numbers():
    maxx = -1
    indexes = []
    for i in range(n):
        for j in range(n):
            if len(num_degree[i][j]) > 0:
                if num_degree[i][j][0] > maxx:
                    maxx = num_degree[i][j][0]
                    indexes = [[i, j]]
                else:
                    if num_degree[i][j][0] == maxx:
                        indexes.append([i, j])
    return indexes


def find_degree_indexes_colors():
    maxx = -1
    indexes = []
    for i in range(n):
        for j in range(n):
            if len(color_degree[i][j]) > 0:
                if color_degree[i][j][0] > maxx:
                    maxx = color_degree[i][j][0]
                    indexes = [[i, j]]
                else:
                    if color_degree[i][j][0] == maxx:
                        indexes.append([i, j])
    return indexes


def find_index():
    mrv_num_indexes = find_mrv_indexes_numbers()
    mrv_color_indexes = find_mrv_indexes_colors()
    if len(mrv_num_indexes) > 0 and len(mrv_color_indexes) > 0:
        if len(num_domain[mrv_num_indexes[0][0]][mrv_num_indexes[0][1]]) <= len(
                color_domain[mrv_color_indexes[0][0]][mrv_color_indexes[0][1]]):
            the_type = "num"
            if len(mrv_num_indexes) > 1:
                max_degree = 0
                selected_index_num = [mrv_num_indexes[0]]
                for index in mrv_num_indexes:
                    if len(num_degree[index[0]][index[1]]) > 0:
                        if num_degree[index[0]][index[1]][0] > max_degree:
                            max_degree = num_degree[index[0]][index[1]][0]
                            selected_index_num = [index]
                        else:
                            if num_degree[index[0]][index[1]][0] == max_degree:
                                selected_index_num.append(index)
                if len(selected_index_num) > 1:
                    # compare the color domains
                    min_len = 1000
                    selected_index_num_next = [selected_index_num[0]]
                    for index in selected_index_num:
                        if len(color_domain[index[0]][index[1]]) < min_len:
                            min_len = len(color_domain[index[0]][index[1]])
                            selected_index_num_next = [index]
                        else:
                            if len(color_domain[index[0]][index[1]]) == min_len:
                                selected_index_num_next.append(index)
                    if len(selected_index_num_next) > 1:
                        max_color_degree = 0
                        final_num_indexes = [selected_index_num_next[0]]
                        for index in selected_index_num_next:
                            if len(color_degree[index[0]][index[1]]) > 0:
                                if color_degree[index[0]][index[1]][0] > max_color_degree:
                                    max_color_degree = color_degree[index[0]][index[1]][0]
                                    final_num_indexes = [index]
                                else:
                                    if color_degree[index[0]][index[1]][0] == max_color_degree:
                                        final_num_indexes.append(index)
                        final_index = final_num_indexes[0]
                    else:
                        final_index = selected_index_num_next[0]
                else:
                    final_index = selected_index_num[0]
            else:
                final_index = mrv_num_indexes[0]
        else:
            the_type = "color"
            if len(mrv_color_indexes) > 1:
                max_degree = 0
                selected_index_color = [mrv_color_indexes[0]]
                for index in mrv_color_indexes:
                    if len(color_degree[index[0]][index[1]]) > 0:
                        if color_degree[index[0]][index[1]][0] > max_degree:
                            max_degree = color_degree[index[0]][index[1]][0]
                            selected_index_color = [index]
                        else:
                            if color_degree[index[0]][index[1]][0] == max_degree:
                                selected_index_color.append(index)
                if len(selected_index_color) > 1:
                    # compare the num domains
                    min_len = 1000
                    selected_index_color_next = [selected_index_color[0]]
                    for index in selected_index_color:
                        if len(num_domain[index[0]][index[1]]) < min_len:
                            min_len = len(num_domain[index[0]][index[1]])
                            selected_index_color_next = [index]
                        else:
                            if len(num_domain[index[0]][index[1]]) == min_len:
                                selected_index_color_next.append(index)
                    if len(selected_index_color_next) > 1:
                        max_num_degree = 0
                        final_color_indexes = [selected_index_color_next[0]]
                        for index in selected_index_color_next:
                            if len(num_degree[index[0]][index[1]]) > 0:
                                if num_degree[index[0]][index[1]][0] > max_num_degree:
                                    max_num_degree = num_degree[index[0]][index[1]][0]
                                    final_color_indexes = [index]
                                else:
                                    if color_degree[index[0]][index[1]][0] == max_num_degree:
                                        final_color_indexes.append(index)
                        final_index = final_color_indexes[0]
                    else:
                        final_index = selected_index_color_next[0]
                else:
                    final_index = selected_index_color[0]
            else:
                final_index = mrv_color_indexes[0]

    else:
        if len(mrv_num_indexes) > 0:
            the_type = "num"
            if len(mrv_num_indexes) > 1:
                max_degree = 0
                selected_index_num = [mrv_num_indexes[0]]
                for index in mrv_num_indexes:
                    if len(num_degree[index[0]][index[1]]) > 0:
                        if num_degree[index[0]][index[1]][0] > max_degree:
                            max_degree = num_degree[index[0]][index[1]][0]
                            selected_index_num = [index]
                        else:
                            if num_degree[index[0]][index[1]][0] == max_degree:
                                selected_index_num.append(index)
                if len(selected_index_num) > 1:
                    # compare the color domains
                    min_len = 1000
                    selected_index_num_next = [selected_index_num[0]]
                    for index in selected_index_num:
                        if len(color_domain[index[0]][index[1]]) < min_len:
                            min_len = len(color_domain[index[0]][index[1]])
                            selected_index_num_next = [index]
                        else:
                            if len(color_domain[index[0]][index[1]]) == min_len:
                                selected_index_num_next.append(index)
                    if len(selected_index_num_next) > 1:
                        max_color_degree = 0
                        final_num_indexes = [selected_index_num_next[0]]
                        for index in selected_index_num_next:
                            if len(color_degree[index[0]][index[1]]) > 0:
                                if color_degree[index[0]][index[1]][0] > max_color_degree:
                                    max_color_degree = color_degree[index[0]][index[1]][0]
                                    final_num_indexes = [index]
                                else:
                                    if color_degree[index[0]][index[1]][0] == max_color_degree:
                                        final_num_indexes.append(index)
                        final_index = final_num_indexes[0]
                    else:
                        final_index = selected_index_num_next[0]
                else:
                    final_index = selected_index_num[0]
            else:
                final_index = mrv_num_indexes[0]
        else:
            the_type = "color"
            if len(mrv_color_indexes) > 1:
                max_degree = 0
                selected_index_color = [mrv_color_indexes[0]]
                for index in mrv_color_indexes:
                    if len(color_degree[index[0]][index[1]]) > 0:
                        if color_degree[index[0]][index[1]][0] > max_degree:
                            max_degree = color_degree[index[0]][index[1]][0]
                            selected_index_color = [index]
                        else:
                            if color_degree[index[0]][index[1]][0] == max_degree:
                                selected_index_color.append(index)
                if len(selected_index_color) > 1:
                    # compare the num domains
                    min_len = 1000
                    selected_index_color_next = [selected_index_color[0]]
                    for index in selected_index_color:
                        if len(num_domain[index[0]][index[1]]) < min_len:
                            min_len = len(num_domain[index[0]][index[1]])
                            selected_index_color_next = [index]
                        else:
                            if len(num_domain[index[0]][index[1]]) == min_len:
                                selected_index_color_next.append(index)
                    if len(selected_index_color_next) > 1:
                        max_num_degree = 0
                        final_color_indexes = [selected_index_color_next[0]]
                        for index in selected_index_color_next:
                            if len(num_degree[index[0]][index[1]]) > 0:
                                if num_degree[index[0]][index[1]][0] > max_num_degree:
                                    max_num_degree = num_degree[index[0]][index[1]][0]
                                    final_color_indexes = [index]
                                else:
                                    if color_degree[index[0]][index[1]][0] == max_num_degree:
                                        final_color_indexes.append(index)
                        final_index = final_color_indexes[0]
                    else:
                        final_index = selected_index_color_next[0]
                else:
                    final_index = selected_index_color[0]
            else:
                final_index = mrv_color_indexes[0]
    return [final_index, the_type]


def go_one_step_back():
    global numbers
    global colors
    global go_back_counter
    global color_domain
    global num_domain
    global color_degree
    global num_degree
    global num_domain_array
    global color_domain_array
    global num_degree_array
    global color_degree_array
    go_back_counter += 1
    print(go_back_counter)
    if len(used_ind_and_types) >= 1:
        used_ind_and_types.pop()
        numbers_array.pop()
        colors_array.pop()
        numbers = numbers_array[-1]
        colors = colors_array[-1]
        used_num_domain.pop()
        num_domain_array.pop()
        num_domain = num_domain_array[-1]
        used_color_domain.pop()
        color_domain_array.pop()
        color_domain = color_domain_array[-1]
        used_num_degree.pop()
        num_degree_array.pop()
        num_degree = num_degree_array[-1]
        used_color_degree.pop()
        color_degree_array.pop()
        color_degree = color_degree_array[-1]
        used_domain_indicator.pop()
        return 0
    else:
        return -1


def try_another_value(index, t):
    global colors
    global numbers
    global used_domain_indicator
    if t == 'num':
        aaa = used_domain_indicator[-1]
        aa = aaa + 1
        bb = len(used_num_domain[-1])
        if aa < bb:
            used_domain_indicator[-1] += 1
            numbers[index[0]][index[1]] = used_num_domain[-1][used_domain_indicator[-1]]
            return 0
        else:
            return -1
    else:
        if used_domain_indicator[-1] + 1 < len(used_color_domain[-1]):
            used_domain_indicator[-1] += 1
            colors_array[-1][index[0]][index[1]] = used_color_domain[-1][used_domain_indicator[-1]]
            return 0
        else:
            return -1


def step_forward(index, the_type):
    global num_domain
    global color_domain
    global num_degree
    global color_degree
    global colors_array
    global numbers_array
    global num_domain_array
    global color_domain_array
    global num_degree_array
    global color_degree_array
    global colors
    global numbers
    if [index, the_type] not in used_ind_and_types:
        numbers_array.append(deepcopy(numbers))
        colors_array.append(deepcopy(colors))
        num_domain_array.append(deepcopy(num_domain))
        color_domain_array.append(deepcopy(color_domain))
        num_degree_array.append(deepcopy(num_degree))
        color_degree_array.append(deepcopy(color_degree))
        used_ind_and_types.append([index, the_type])
        used_num_domain.append(deepcopy(num_domain[index[0]][index[1]]))
        used_color_domain.append(deepcopy(color_domain[index[0]][index[1]]))
        used_num_degree.append(deepcopy(num_degree[index[0]][index[1]]))
        used_color_degree.append(deepcopy(color_degree[index[0]][index[1]]))
        used_domain_indicator.append(-1)
    colors = deepcopy(colors_array[-1])
    numbers = deepcopy(numbers_array[-1])
    num_domain = deepcopy(num_domain_array[-1])
    color_domain = deepcopy(color_domain_array[-1])
    num_degree = deepcopy(num_degree_array[-1])
    color_degree = deepcopy(color_degree_array[-1])
    if the_type == 'num':
        if used_domain_indicator[-1] + 1 < len(used_num_domain[-1]):
            while True:
                ff = 0
                k = try_another_value(index, 'num')
                if k == -1:
                    break
                prev_num_domain = deepcopy(num_domain)
                prev_num_degree = deepcopy(num_degree)
                prev_color_domain = deepcopy(color_domain)
                prev_color_degree = deepcopy(color_degree)
                num_domain[index[0]][index[1]] = []
                update_all()
                for i in range(len(num_domain)):
                    for j in range(len(num_domain)):
                        if len(num_domain[i][j]) == 0 and numbers[i][j] == '*':
                            ff = 1
                            break
                if ff == 1:
                    num_domain = deepcopy(prev_num_domain)
                    num_degree = deepcopy(prev_num_degree)
                    color_domain = deepcopy(prev_color_domain)
                    color_degree = deepcopy(prev_color_degree)
                    continue
                for i in range(len(color_domain)):
                    for j in range(len(color_domain)):
                        if len(color_domain[i][j]) == 0 and colors[i][j] == '#':
                            ff = 1
                            break
                if ff == 1:
                    num_domain = deepcopy(prev_num_domain)
                    num_degree = deepcopy(prev_num_degree)
                    color_domain = deepcopy(prev_color_domain)
                    color_degree = deepcopy(prev_color_degree)
                    continue
                flag = 1
                for g in range(n):
                    if '*' not in numbers[g] and '#' not in colors[g]:
                        continue
                    else:
                        flag = 0
                        break
                if flag == 0:
                    numbers_array[-1] = deepcopy(numbers)
                    colors_array[-1] = deepcopy(colors)
                    num_domain_array[-1] = deepcopy(num_domain)
                    color_domain_array[-1] = deepcopy(color_domain)
                    num_degree_array[-1] = deepcopy(num_degree)
                    color_degree_array[-1] = deepcopy(color_degree)
                    return 2  # it means move forward
                else:
                    return 1
            res = go_one_step_back()
            if res == 0:
                return 3
            else:
                return -1
        else:
            res = go_one_step_back()
            if res == 0:
                return 3
            else:
                return -1
    else:
        if used_domain_indicator[-1] + 1 < len(used_color_domain[-1]):
            while True:
                ff = 0
                k = try_another_value(index, 'color')
                if k == -1:
                    break
                prev_num_domain = deepcopy(num_domain)
                prev_num_degree = deepcopy(num_degree)
                prev_color_domain = deepcopy(color_domain)
                prev_color_degree = deepcopy(color_degree)
                color_domain[index[0]][index[1]] = []
                colors[index[0]][index[1]] = deepcopy(colors_array[-1][index[0]][index[1]])
                update_all()
                for i in range(len(num_domain)):
                    for j in range(len(num_domain)):
                        if len(num_domain[i][j]) == 0 and numbers[i][j] == '*':
                            ff = 1
                            break
                        if ff == 1:
                            break
                if ff == 1:
                    num_domain = deepcopy(prev_num_domain)
                    num_degree = deepcopy(prev_num_degree)
                    color_domain = deepcopy(prev_color_domain)
                    color_degree = deepcopy(prev_color_degree)
                    continue
                for i in range(len(num_domain)):
                    for j in range(len(num_domain)):
                        if len(color_domain[i][j]) == 0 and colors[i][j] == '#':
                            ff = 1
                            break
                    if ff == 1:
                        break
                if ff == 1:
                    num_domain = deepcopy(prev_num_domain)
                    num_degree = deepcopy(prev_num_degree)
                    color_domain = deepcopy(prev_color_domain)
                    color_degree = deepcopy(prev_color_degree)
                    continue
                flag = 1
                for g in range(n):
                    if '*' not in numbers[g] and '#' not in colors[g]:
                        continue
                    else:
                        flag = 0
                        break
                if flag == 0:
                    numbers_array[-1] = deepcopy(numbers)
                    colors_array[-1] = deepcopy(colors)
                    num_domain_array[-1] = deepcopy(num_domain)
                    color_domain_array[-1] = deepcopy(color_domain)
                    num_degree_array[-1] = deepcopy(num_degree)
                    color_degree_array[-1] = deepcopy(color_degree)
                    return 2
                else:
                    return 1
            res = go_one_step_back()
            if res == 0:
                return 3
            else:
                return -1
        else:
            res = go_one_step_back()
            if res == 0:
                return 3
            else:
                return -1


update_all()
first_color_domain = deepcopy(color_domain)
first_color_degree = deepcopy(color_degree)
first_number_domain = deepcopy(num_domain)
first_number_degree = deepcopy(num_degree)
ind, t = find_index()
step = 0
while True:
    step += 1
    print('step : {}'.format(step))
    a = step_forward(ind, t)
    if a == 2:
        ind, t = find_index()
        continue
    elif a == 3:
        ind = used_ind_and_types[-1][0]
        t = used_ind_and_types[-1][1]
    if a == 1 or a == -1:
        break
if a == -1:
    print("failed")

for i in range(n):
    for j in range(n):
        print("{}{} ".format(numbers[i][j], colors[i][j]), end="")
    print("\n")
