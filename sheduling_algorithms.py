def FCFS(thread_list):
    result = [[] for t in thread_list]
    # list that show state of process (active or finished)
    finished_threads = [False for t in thread_list]
    # queue of current process
    queue = [thread_list.index(t) for t in thread_list]
    # list of current indexes of process
    current_indexes = [0 for t in thread_list]

    print(current_indexes)
    cpu = 0
    while not all(finished_threads):
        if queue:
            current_thread_number = queue.pop(0)
            print(current_thread_number)
            while (not finished_threads[current_thread_number]) and (
                    thread_list[current_thread_number][current_indexes[current_thread_number]] == 1):
                for i in range(len(result)):
                    if not finished_threads[i]:
                        if i == current_thread_number:
                            result[i].append('x')
                            current_indexes[i] += 1
                        else:
                            if thread_list[i][current_indexes[i]] == 1:
                                result[i].append('.')
                            else:
                                result[i].append('-')
                                current_indexes[i] += 1
                        if current_indexes[i] >= len(thread_list[i]):
                            finished_threads[i] = True
            print(result)
        else:
            for i in range(len(result)):
                if not finished_threads[i]:
                    if thread_list[i][current_indexes[i]] == 1:
                        result[i].append('.')
                    else:
                        result[i].append('-')
                        current_indexes[i] += 1
                    if current_indexes[i] >= len(thread_list[i]):
                        finished_threads[i] = True

        for i in range(len(thread_list)):
            if not finished_threads[i]:
                if thread_list[i][current_indexes[i]] == 1 and not i in queue:
                    queue.append(i)
        print(queue)
        cpu += 1
    return result



def calculate_stats(result):
    max_len = 0
    sum_len=0
    stats=[]
    finished_threads = [False for l in result]

    for l in result:
        if len(l)>max_len:
            max_len=len(l)
            sum_len+=len(l)

    stats.append('Throughput=' + str(len(result))+ "/" + str(max_len))
    stats.append("Turnaround time="+str(sum_len)+ "/" + str(len(result)))



    eff_loss=0;
    count_not_busy=0
    count_working_threads=0
    for i in range(0,max_len):
        for k in range(0,len(result)):
            if  finished_threads[k]==False:
                count_working_threads+=1
                if result[k][i]!='x':
                    count_not_busy+=1

        if count_working_threads==count_not_busy:
            eff_loss+=1
        count_not_busy = 0
        count_working_threads = 0
        for j in range(0,len(result)):
            if i==len(result[j])-1:
                finished_threads[j]=True


    stats.append("Efficiency=" + str(max_len-eff_loss) + "/" + str(max_len))
    io_count=0
    wait_count=0

    for l in result:
        tag = False
        for i in range(1,len(l)):
            if l[i-1]=='x' and l[i]=='-':
                io_count+=1


            if l[i-1]=='-' and l[i]=='.':
                tag=True
                wait_count+=1
            if l[i-1]=='.' and l[i]=='.' and tag:
                wait_count+=1
    stats.append("Waittime=" + str(wait_count) + "/" + str(io_count))
    task_switches=0


    prev_thread=0
    for k in range(0,len(result)):
        if result[k][0]=='x':
            prev_thread=k

    finished_threads = [False for t in result]
    for i in range(0,max_len):
        for k in range(0,len(result)):
            if  finished_threads[k]==False:
                if result[k][i]=='x':
                    if prev_thread!=k:
                        task_switches+=1
                        prev_thread=k



        for j in range(0,len(result)):
            if i==len(result[j])-1:
                finished_threads[j]=True

    stats.append("Task switches="+str(task_switches))


    return stats



import xlwt


def visualise(result):
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
                    ws.write(1 + j * 3, 1 + i, '', up_left_execution_block)
                    ws.write(2 + j * 3, 1 + i, '', down_left_execution_block)
                elif i == len(result[j]) - 1:
                    if result[j][i - 1] == 'x':
                        ws.write(1 + j * 3, 1 + i, '', up_right_execution_block)
                        ws.write(2 + j * 3, 1 + i, '', down_right_execution_block)
                    else:
                        ws.write(1 + j * 3, 1 + i, '', up_full_execution_block)
                        ws.write(2 + j * 3, 1 + i, '', down_full_execution_block)
                elif result[j][i - 1] == 'x' and result[j][i + 1] != 'x':
                    ws.write(1 + j * 3, 1 + i, '', up_right_execution_block)
                    ws.write(2 + j * 3, 1 + i, '', down_right_execution_block)
                elif result[j][i - 1] == 'x' and result[j][i + 1] == 'x':
                    ws.write(1 + j * 3, 1 + i, '', up_middle_execution_block)
                    ws.write(2 + j * 3, 1 + i, '', down_middle_execution_block)
                elif result[j][i - 1] != 'x' and result[j][i + 1] == 'x':
                    ws.write(1 + j * 3, 1 + i, '', up_left_execution_block)
                    ws.write(2 + j * 3, 1 + i, '', down_left_execution_block)
                elif result[j][i - 1] != 'x' and result[j][i + 1] != 'x':
                    ws.write(1 + j * 3, 1 + i, '', up_full_execution_block)
                    ws.write(2 + j * 3, 1 + i, '', down_full_execution_block)

            elif result[j][i] == '-':
                ws.write_merge(r1=1 + j * 3, r2=1 + j * 3, c1=1 + i, c2=1 + i, label='', style=wait_for_answer)
            elif result[j][i] == '.':
                ws.write_merge(r1=1 + j * 3, r2=1 + j * 3, c1=1 + i, c2=1 + i, label='', style=ready_to_execution)

    wb.save('example.xls')
