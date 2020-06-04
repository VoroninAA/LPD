with open('./input_file.txt') as input_file:
    num_threads = int(input_file.readline());
    print('Кол-во потоков: ', num_threads)
    threads_list = []
    for line in input_file:
        line = line[:-1]
        bin_line = []
        for char in line:
            if char == '0':
                bin_line.append(1)
            else:
                bin_line.append(0)
        threads_list.append(bin_line)
    for thread in threads_list:
        print('Поток ' + str(threads_list.index(thread)) + ': ', thread)

import sheduling_algorithms
sheduling_algorithms.FCFS(threads_list)