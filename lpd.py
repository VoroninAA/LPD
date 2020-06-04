with open('./input_file.txt') as input_file:
    num_threads = int(input_file.readline());
    print('Кол-во потоков: ', num_threads)
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

import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)

# left border style
borders = xlwt.Borders()
borders.left = 2
borders.right = 0
borders.top = 2
borders.bottom = 0
up_left_execution_block = xlwt.XFStyle()
up_left_execution_block.borders = borders
borders = xlwt.Borders()
borders.left = 2
borders.right = 0
borders.top = 0
borders.bottom = 2
down_left_execution_block = xlwt.XFStyle()
down_left_execution_block.borders = borders

# middle border style
borders = xlwt.Borders()
borders.left = 0
borders.right = 0
borders.top = 2
borders.bottom = 0
up_middle_execution_block = xlwt.XFStyle()
up_middle_execution_block.borders = borders
borders = xlwt.Borders()
borders.left = 0
borders.right = 0
borders.top = 0
borders.bottom = 2
down_middle_execution_block = xlwt.XFStyle()
down_middle_execution_block.borders = borders

# right border style
borders = xlwt.Borders()
borders.left = 0
borders.right = 2
borders.top = 2
borders.bottom = 0
up_right_execution_block = xlwt.XFStyle()
up_right_execution_block.borders = borders
borders = xlwt.Borders()
borders.left = 0
borders.right = 2
borders.top = 0
borders.bottom = 2
down_right_execution_block = xlwt.XFStyle()
down_right_execution_block.borders = borders

# full block border style
borders = xlwt.Borders()
borders.left = 2
borders.right = 2
borders.top = 2
borders.bottom = 0
up_full_execution_block = xlwt.XFStyle()
up_full_execution_block.borders = borders
borders = xlwt.Borders()
borders.left = 2
borders.right = 2
borders.top = 0
borders.bottom = 2
down_full_execution_block = xlwt.XFStyle()
down_full_execution_block.borders = borders

# waite for answer border style
borders = xlwt.Borders()
borders.bottom = 2
wait_for_answer = xlwt.XFStyle()
wait_for_answer.borders = borders

# waite for execution border style
borders = xlwt.Borders()
borders.bottom = borders.MEDIUM_DASHED
ready_to_execution = xlwt.XFStyle()
ready_to_execution.borders = borders

# background style
borders = xlwt.Borders()
borders.left = borders.HAIR
borders.right = borders.HAIR
borders.top = borders.HAIR
borders.bottom = borders.HAIR
background = xlwt.XFStyle()
background.borders = borders

for i in range(100):
    for j in range(100):
        ws.write(i, j, '', background)

for j in range(len(result)):
    for i in range(len(result[j])):
        if result[j][i] == 'x':
            if i == 0:
                ws.write(1+j*3, 1+i, '', up_left_execution_block)
                ws.write(2 + j * 3, 1 + i, '', down_left_execution_block)
            elif i == len(result[j])-1:
                if result[j][i-1] == 'x':
                    ws.write(1 + j * 3, 1 + i, '', up_right_execution_block)
                    ws.write(2 + j * 3, 1 + i, '', down_right_execution_block)
                else:
                    ws.write(1 + j * 3, 1 + i, '', up_full_execution_block)
                    ws.write(2 + j * 3, 1 + i, '', down_full_execution_block)
            elif result[j][i-1] == 'x' and result[j][i+1] != 'x':
                ws.write(1 + j * 3, 1 + i, '', up_right_execution_block)
                ws.write(2 + j * 3, 1 + i, '', down_right_execution_block)
            elif result[j][i-1] == 'x' and result[j][i+1] == 'x':
                ws.write(1 + j * 3, 1 + i, '', up_middle_execution_block)
                ws.write(2 + j * 3, 1 + i, '', down_middle_execution_block)
            elif result[j][i - 1] != 'x' and result[j][i + 1] == 'x':
                ws.write(1 + j * 3, 1 + i, '', up_left_execution_block)
                ws.write(2 + j * 3, 1 + i, '', down_left_execution_block)
            elif result[j][i - 1] != 'x' and result[j][i + 1] != 'x':
                ws.write(1 + j * 3, 1 + i, '', up_full_execution_block)
                ws.write(2 + j * 3, 1 + i, '', down_full_execution_block)

        elif result[j][i] == '-':
            ws.write_merge(r1=1+j*3, r2=1+j*3, c1=1+i, c2=1+i, label='', style=wait_for_answer)
        elif result[j][i] == '.':
            ws.write_merge(r1=1+j*3, r2=1+j*3, c1=1+i, c2=1+i, label='', style=ready_to_execution)


wb.save('example.xls')