with open('./input_file.txt') as input_file:
    threads_list = []
    for line in input_file:
        line = list(filter(lambda x: x!='\n', line))
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
result = sheduling_algorithms.FCFS(threads_list)
stats=sheduling_algorithms.calculate_stats(result)
print(stats)

sheduling_algorithms.visualise(result)
