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
            # print(current_thread_number)
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
                for i in range(len(thread_list)):
                    if not finished_threads[i] and i != current_thread_number:
                        if thread_list[i][current_indexes[i]] == 1 and not i in queue:
                            queue.append(i)
            # print(result)
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

def StandartPriotiry(thread_list):
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
            current_thread_number = min(queue)
            queue.pop(queue.index(current_thread_number))
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


def RR(thread_list, quantum):
    result = [[] for t in thread_list]
    # list that show state of process (active or finished)
    finished_threads = [False for t in thread_list]
    # queue of current process
    queue = [thread_list.index(t) for t in thread_list]
    # list of current indexes of process
    current_indexes = [0 for t in thread_list]

    print(current_indexes)
    cpu = 0
    prev_thread_number=-1
    while not all(finished_threads):
        if queue:
            if current_indexes[prev_thread_number]<len(thread_list[prev_thread_number]):
              if thread_list[prev_thread_number][current_indexes[prev_thread_number]] == 1 and prev_thread_number!=-1:
                    queue.pop(queue.index((prev_thread_number)))
                    queue.append(prev_thread_number)


            for q in queue:
                if q!=prev_thread_number:
                    current_thread_number=q
                    queue.pop(queue.index(q))
                    break


            prev_thread_number=current_thread_number
            print(current_thread_number)
            step=0
            while (not finished_threads[current_thread_number]) and (step<quantum) and  (thread_list[current_thread_number][current_indexes[current_thread_number]] == 1):
                step+=1
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




def RR_Priority(thread_list, quantum):
    result = [[] for t in thread_list]
    # list that show state of process (active or finished)
    finished_threads = [False for t in thread_list]
    # queue of current process
    queue = [thread_list.index(t) for t in thread_list]
    # list of current indexes of process
    current_indexes = [0 for t in thread_list]

    print(current_indexes)
    cpu = 0
    prev_thread_number=-1
    while not all(finished_threads):
        if queue:
            if current_indexes[prev_thread_number]<len(thread_list[prev_thread_number]):
              if thread_list[prev_thread_number][current_indexes[prev_thread_number]] == 1 and prev_thread_number!=-1:
                    queue.pop(queue.index((prev_thread_number)))
                    queue.append(prev_thread_number)

            thread_found=False
            for q in queue:
                if q!=prev_thread_number and (q==0 or q==1):
                    current_thread_number=q
                    queue.pop(queue.index(q))
                    thread_found=True
                    break


            for q in queue:
                if q == prev_thread_number and (q == 0 or q == 1) and not thread_found:
                    current_thread_number = q
                    queue.pop(queue.index(q))
                    thread_found=True
                    break

            if not thread_found:
                current_thread_number=2
                queue.pop(queue.index((2)))

            prev_thread_number=current_thread_number
            print(current_thread_number)
            step=0
            while (not finished_threads[current_thread_number]) and (step<quantum) and  (thread_list[current_thread_number][current_indexes[current_thread_number]] == 1):
                step+=1
                if current_thread_number==2:
                    step+=1
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
    sum_len = "("
    for t in result:
        sum_len += str(len(t)) + " + "
    sum_len = sum_len[:-3]
    sum_len += ")"
    stats=[]
    finished_threads = [False for l in result]

    for l in result:
        if len(l)>max_len:
            max_len=len(l)

    stats.append('Throughput=' + str(len(result))+ "/" + str(max_len))
    stats.append("Turnaround time="+ sum_len + "/" + str(len(result)))



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

    wait_count_list = []
    for l in result:
        tag = False
        tag2 = False
        for i in range(1,len(l)):
            if l[i-1]=='x' and l[i]=='-':
                io_count+=1
                wait_count = 0
                tag2 = True

            if l[i-1]=='-' and l[i]=='.':
                tag=True
                tag2=True
                wait_count+=1
            if l[i-1]=='.' and l[i]=='.' and tag:
                wait_count+=1
            elif tag2 and l[i]=='x':
                tag2 = False
                wait_count_list.append(wait_count)
    wait_output = "("
    for w in wait_count_list:
        wait_output += str(w) + " + "
    wait_output = wait_output[:-3]
    wait_output += ")"
    stats.append("Waittime=" + wait_output + "/" + str(io_count))
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
