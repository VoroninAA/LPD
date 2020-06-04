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
            while (not finished_threads[current_thread_number]) and (thread_list[current_thread_number][current_indexes[current_thread_number]] == 1):
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
        cpu+=1
    return result