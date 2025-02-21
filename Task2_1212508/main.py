from queue import Queue, PriorityQueue

"""=====================================Times Calculation==================================================="""


def time_calc(process):
    total_wait_time = 0
    total_turnaround_time = 0
    infinite = 'INFINITE'
    infinite_flag2 = 0
    print("\nTable of times for each process:\n\nProcess| Complete  | Turnaround |Waiting")
    for p in process:  # for loop calculating total waiting and turnaround times, printing table for each process's
        # time
        completion_time = p[5]
        if completion_time != 0:
            turnaround_time = completion_time - p[1]  # turnaround time = complete time - arrival time
        else:
            turnaround_time = 0

        if turnaround_time != 0:
            waiting_time = turnaround_time - p[2]
            infinite_flag = 0
        else:
            waiting_time = infinite
            completion_time = infinite
            turnaround_time = infinite
            infinite_flag = 1

        p[5] = completion_time
        p[6] = turnaround_time
        p[7] = waiting_time
        print(p[0], "\t\t", p[5], "\t\t", p[6], "\t\t", p[7])
        if infinite_flag == 0:
            total_wait_time += waiting_time
            total_turnaround_time += turnaround_time
        else:
            infinite_flag2 = 1

    if infinite_flag2 != 1:
        print("\nAverage Waiting Time: ", int(total_wait_time / 7))
        print("Average Turnaround Time: ", int(total_turnaround_time / 7))
    else:
        print("\nAverage Waiting Time: ", infinite)
        print("Average Turnaround Time: ", infinite)


# =========================================================================================================

"""=========================First Come First Served (F.C.F.S) Algorithm====================================="""


def fcfs(process):
    # FCFS algorith
    # in this algorithm after all finished we notice that will come again in same order
    # Putting Processes in ready Queue in order of coming

    # Creation ready Queue and waiting Queue
    ready_queue = Queue()
    waiting_queue = Queue()
    temp_list = []

    # ready_queue.put(process[0])  # put first process to ready immediately that's arrival time is 0
    for n in range(1, 7, 1):  # for loop to initially set waiting time for each one at the start
        # ( arrive of prev. + burst of prev. + wait of prev.) - arrive of current
        waiting_time = (process[n - 1][1] + process[n - 1][2] + process[n - 1][7]) - process[n][1]
        process[n][7] = waiting_time
        ready_queue.put(process[n])

    gantt_chart = []
    gantt_chart_time = [0]

    p = process[0]
    burst_time = p[2]
    come_back_after = p[3]

    for t in range(8, 201, 1):  # for loop to end limit of time for CPU which is 200 time unit

        while not waiting_queue.empty():  # this loop to set come back of each process
            element = waiting_queue.get()
            temp_list.append(element)
        for element in temp_list:  # for loop to return process to waiting if still waiting or ready if come back
            if t == element[6]:
                # element[8] = t      # assign time of come back to ready queue to calculate waiting time in ready queue
                ready_queue.put(element)
            else:
                waiting_queue.put(element)
        temp_list.clear()

        if t == burst_time:  # now process has finished its burst time
            completion_time = t
            p[5] = completion_time  # set last completion time for each process
            p[6] = come_back_after + completion_time  # save the time of coming back for each process
            # p[7] += (t - p[2] - p[8])  # update waiting time

            gantt_chart_time.append(burst_time)  # for insert the time in chart
            gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart

            waiting_queue.put(p)  # put the process in waiting queue
            if not ready_queue.empty():
                p = ready_queue.get()  # get next process
                burst_time = p[2] + t  # update the time to finish the burst time for the new process
                come_back_after = p[3]
                # p[7] += (t - p[6])  # update waiting time

    print("Gantt Chart:\n")
    k = 0
    for element in gantt_chart_time:
        print(element, end='  |')
        if k < len(gantt_chart):
            print(gantt_chart[k], end='|  ')
        k += 1
    print()
    time_calc(process=process)


# =========================================================================================================

"""=============================Shortest Job First (S.J.F) Algorithm========================================"""


def sjf(process):
    # Shortest Job First Algorithm

    # Creation ready Queue and waiting Queue
    ready_queue = Queue()
    waiting_queue = Queue()
    gantt_chart = []
    gantt_chart_time = [0]

    burst_list = []
    temp_list = []

    for j in range(1, 7, 1):  # for loop to initially set waiting time for each one at the start
        burst_list.append(process[j])

    burst_list.sort(key=lambda x: x[2])
    for p in burst_list:
        ready_queue.put(p)

    p = process[0]
    burst_time = p[2]
    come_back_after = p[3]

    for t in range(8, 201, 1):  # for loop to end limit of time for CPU which is 200 time unit
        while not waiting_queue.empty():  # this loop to set come back of each process
            element = waiting_queue.get()
            temp_list.append(element)
        for element in temp_list:  # for loop to return process to waiting if still waiting or ready if come back
            if t == element[6]:
                ready_queue.put(element)
            else:
                waiting_queue.put(element)
        temp_list.clear()

        if t == burst_time:  # now process has finished its burst time
            completion_time = t
            p[5] = completion_time  # set last completion time for each process
            p[6] = come_back_after + completion_time  # save the time of coming back for each process

            gantt_chart_time.append(burst_time)  # for insert the time in chart
            gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart

            waiting_queue.put(p)  # put the process in waiting queue
            if not ready_queue.empty():
                burst_list.clear()
                while not ready_queue.empty():  # deque all processes in ready queue to resort them
                    proc = ready_queue.get()
                    burst_list.append(proc)  # adding all burst times of processes that is in ready queue

                burst_list.sort(key=lambda x: x[2])  # sort based on burst time ascending
                for burst in burst_list:  # this for loop to resort the processes in ready queue depend on burst time
                    ready_queue.put(burst)
                burst_list.clear()
                p = ready_queue.get()  # get next process
                come_back_after = p[3]
                burst_time = p[2] + t  # update the time to finish the burst time for the new process

    print("Gantt Chart:\n")
    k = 0
    for element in gantt_chart_time:
        print(element, end='  |')
        if k < len(gantt_chart):
            print(gantt_chart[k], end='|  ')
        k += 1
    print()
    time_calc(process=process)


# =========================================================================================================

"""===========================Shortest Remaining Time First (S.R.T.F) Algorithm============================="""


def srtf(process):
    # Shortest Remaining Time First Algorithm "Preemptive" version of Shortest Job First Algorithm

    # Creation ready Queue and waiting Queue
    ready_queue = Queue()
    waiting_queue = Queue()
    gantt_chart = []
    gantt_chart_time = [0]
    temp_list = []
    proc_list = []

    process[0][8] = process[0][2]
    for j in range(1, 7, 1):
        process[j][8] = process[j][2]  # initializing remaining time
        proc_list.append(process[j])

    # burst_list.sort(key=lambda x: x[8])     # sort based on remaining time ascending
    p = process[0]

    for t in range(201):  # for loop to end limit of time for CPU which is 200 time unit
        for element in proc_list:  # put processes depend on arrival time, it will be finished when all arrived
            if t == element[1]:  # process arrived now
                ready_queue.put(element)

        # ======================================Come Back====================================
        while not waiting_queue.empty():  # this loop to set come back of each process
            element = waiting_queue.get()
            temp_list.append(element)
        for element in temp_list:  # for loop to return process to waiting if still waiting or ready if come back
            if t == element[6]:
                ready_queue.put(element)
            else:
                waiting_queue.put(element)
        temp_list.clear()
        # ==================================================================================

        if not ready_queue.empty():
            temp_list.clear()
            while not ready_queue.empty():  # deque all processes in ready queue to resort them
                proc = ready_queue.get()
                temp_list.append(proc)  # adding all burst times of processes that is in ready queue

            next_proc = temp_list[0]
            min_proc = min(temp_list, key=lambda x: x[8])  # shortest remaining time

            # ======================================Remaining Time Elapsed====================================
            if p[8] == 0:  # check if process has finished its remaining time
                completion_time = t
                p[5] = completion_time  # set last completion time for each process
                p[6] = p[3] + completion_time  # save the time of coming back for each process

                gantt_chart_time.append(completion_time)  # for insert the time in chart
                gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart

                p[8] = p[2]  # reset remaining time by burst time

                waiting_queue.put(p)  # put the process in waiting queue
                p = min_proc
                temp_list.remove(min_proc)  # so that we got it
            # ===============================================================================================

            elif next_proc[8] < p[8]:  # if the next process its remaining time less than current process
                temp_list.remove(next_proc)  # so that we got it
                temp_list.append(p)  # return current process to ready again

                gantt_chart_time.append(t)  # for insert the time in chart
                gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart

                p = next_proc  # replacing with the shortest remaining time

            elif min_proc[8] < p[8]:  # if there is a process its remaining time less than current process
                temp_list.remove(min_proc)  # so that we got it
                temp_list.append(p)  # return current process to ready again

                gantt_chart_time.append(t)  # for insert the time in chart
                gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart

                p = min_proc  # replacing with the shortest remaining time

            for element in temp_list:  # this for loop to resort the processes in ready queue depend on remaining time
                ready_queue.put(element)
            temp_list.clear()

        p[8] -= 1  # remaining time elapsed by one

    print("Gantt Chart:\n")
    k = 0
    for element in gantt_chart_time:
        print(element, end='  |')
        if k < len(gantt_chart):
            print(gantt_chart[k], end='|  ')
        k += 1
    print()
    time_calc(process=process)


# =========================================================================================================

"""==============================Round Robin (R.R) Algorithm================================================"""


def rr(process):
    # Round Robin Algorithm with Time Quantum 5 ( q = 5 )

    # Creation ready Queue and waiting Queue
    ready_queue = Queue()
    waiting_queue = Queue()
    gantt_chart = []
    gantt_chart_time = [0]

    temp_list = []
    proc_list = []

    time_quantum = 5  # time quantum of R.R , we will add this temporarily in waiting time index

    process[0][7] = time_quantum
    process[0][8] = process[0][2]
    for j in range(1, 7, 1):  # for loop to initially add each process to process list from P2
        process[j][8] = process[j][2]  # initializing remaining time
        process[j][7] = time_quantum  # initializing (q) for all processes
        proc_list.append(process[j])

    p = process[0]

    for t in range(201):  # for loop to end limit of time for CPU which is 200 time unit
        for element in proc_list:  # put processes depend on arrival time, it will be finished when all arrived
            if t == element[1]:  # process arrived now
                ready_queue.put(element)

        # ======================================Come Back====================================
        while not waiting_queue.empty():  # this loop to set come back of each process
            element = waiting_queue.get()
            temp_list.append(element)
        for element in temp_list:  # for loop to return process to waiting if still waiting or ready if come back
            if t == element[6]:
                ready_queue.put(element)
            else:
                waiting_queue.put(element)
        temp_list.clear()
        # ==================================================================================

        if not ready_queue.empty():
            temp_list.clear()
            while not ready_queue.empty():  # deque all processes in ready queue to resort them
                proc = ready_queue.get()
                temp_list.append(proc)  # adding all burst times of processes that is in ready queue

            next_proc = temp_list[0]
            # ======================================Remaining Time Elapsed====================================
            if p[8] == 0:  # check if process has finished its remaining time
                completion_time = t
                p[5] = completion_time  # set last completion time for each process
                p[6] = p[3] + completion_time  # save the time of coming back for each process

                gantt_chart_time.append(completion_time)  # for insert the time in chart
                gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart

                p[8] = p[2]  # reset remaining time by burst time
                p[7] = time_quantum  # reset time quantum by original count

                waiting_queue.put(p)  # put the process in waiting queue
                p = next_proc
                temp_list.remove(next_proc)  # so that we got it
            # ===============================================================================================

            elif p[7] == 0:  # check if time quantum elapsed
                p[7] = time_quantum  # reset time quantum by original count
                temp_list.remove(next_proc)  # so that we got it
                temp_list.append(p)  # return current process to ready again

                gantt_chart_time.append(t)  # for insert the time in chart
                gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart

                p = next_proc  # replacing with the shortest remaining time

            for element in temp_list:  # this for loop to resort the processes in ready queue depend on remaining time
                ready_queue.put(element)
            temp_list.clear()

        p[8] -= 1  # remaining time elapsed by one
        p[7] -= 1  # time quantum elapsed by one

    print("Gantt Chart:\n")
    k = 0
    for element in gantt_chart_time:
        print(element, end='  |')
        if k < len(gantt_chart):
            print(gantt_chart[k], end='|  ')
        k += 1
    print()
    time_calc(process=process)


# =========================================================================================================

"""=====================================Preemptive Priority================================================"""


def priority_pre(process):
    """Preemptive Priority Scheduling, with aging; where priority is decremented by
1 if the process remains in the ready queue for 5 time units."""

    ready_queue = Queue()
    waiting_queue = Queue()
    temp_list = []
    proc_list = []
    gantt_chart = []
    gantt_chart_time = [0]
    time_elapsed = 5

    process[0][8] = process[0][2]
    for j in range(1, 7, 1):  # for loop to initially add each process to process list from P2
        process[j][8] = process[j][2]  # initializing remaining time
        proc_list.append(process[j])

    p = process[0]

    for t in range(201):  # for loop to end limit of time for CPU which is 200 time unit
        for element in proc_list:  # put processes depend on arrival time, it will be finished when all arrived
            if t == element[1]:  # process arrived now
                ready_queue.put(element)

        # ======================================Come Back====================================
        while not waiting_queue.empty():  # this loop to set come back of each process
            element = waiting_queue.get()
            temp_list.append(element)
        for element in temp_list:  # for loop to return process to waiting if still waiting or ready if come back
            if t == element[6]:
                ready_queue.put(element)
            else:
                waiting_queue.put(element)
        temp_list.clear()
        # ==================================================================================

        if not ready_queue.empty():
            temp_list.clear()
            while not ready_queue.empty():  # deque all processes in ready queue to update elapsed time in it
                proc = ready_queue.get()
                temp_list.append(proc)  # adding all burst times of processes that is in ready queue

            next_proc = min(temp_list, key=lambda x: x[4])  # get the highest priority process
            # ======================================Remaining Time Elapsed====================================
            if p[8] == 0:  # check if process has finished its remaining time
                completion_time = t
                p[5] = completion_time  # set last completion time for each process
                p[6] = p[3] + completion_time  # save the time of coming back for each process

                gantt_chart_time.append(completion_time)  # for insert the time in chart
                gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart

                p[8] = p[2]  # reset remaining time by burst time
                p[7] = 0    # reset elapsed time to 0

                waiting_queue.put(p)  # put the process in waiting queue
                p = next_proc
                p[7] = 0  # reset elapsed time to 0 since we got the process from ready queue
                temp_list.remove(next_proc)  # so that we got it
            # ===============================================================================================
            elif next_proc[4] < p[4]:  # compare priority
                temp_list.remove(next_proc)  # so that we got it
                gantt_chart_time.append(t)  # for insert the time in chart
                gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart
                p[7] = 0  # reset elapsed time to 0 since we got the process from ready queue

                if p[0] == process[3][0] and temp_list[0][0] == 1:   # if the process is P4 and first one is P1
                    temp_list.insert(0, p)
                else:
                    temp_list.append(p)

                p = next_proc  # replacing with next process that's the highest priority
                p[7] = 0  # reset elapsed time to 0 since we got the process from ready queue

            for element in temp_list:  # this for loop to resort the processes in ready queue depend on remaining time
                ready_queue.put(element)
            temp_list.clear()
        # =========================================Update Priority=========================================
            while not ready_queue.empty():  # deque all processes in ready queue to update elapsed time in it
                proc = ready_queue.get()
                if t > proc[1]:  # if they arrived actually
                    proc[7] += 1  # increase elapsed time in ready by 1
                unit = int(proc[7] / time_elapsed)
                if unit >= 1:
                    if proc[4] == 1:  # if priority equals 1
                        proc[4] -= 1
                    elif proc[4] > 1:  # if priority greater than 1
                        if proc[4] - unit > 0:  # if result of subtraction greater than 0, then subtract normally
                            proc[4] -= unit  # decrementing the priority
                        elif proc[4] - unit <= 0:  # if less than or equal 0, then set to high priority '0'
                            proc[4] = 0

                temp_list.append(proc)  # adding all burst times of processes that is in ready queue

            for element in temp_list:  # this for loop to resort the processes in ready queue depend on remaining time
                ready_queue.put(element)
            temp_list.clear()
        # =========================================Update Priority=========================================
        p[8] -= 1  # remaining time elapsed by one

    print("Gantt Chart:\n")
    k = 0
    for element in gantt_chart_time:
        print(element, end='  |')
        if k < len(gantt_chart):
            print(gantt_chart[k], end='|  ')
        k += 1
    print()
    time_calc(process=process)

# =========================================================================================================


"""=====================================Non-Preemptive Priority================================================"""


def priority_nonpre(process):
    """Non-Preemptive Priority Scheduling, with aging; where priority is decremented by
1 if the process remains in the ready queue for 5 time units."""

    ready_queue = Queue()
    waiting_queue = Queue()
    temp_list = []
    proc_list = []
    gantt_chart = []
    gantt_chart_time = [0]
    time_elapsed = 5

    process[0][8] = process[0][2]
    for j in range(1, 7, 1):  # for loop to initially add each process to process list from P2
        process[j][8] = process[j][2]  # initializing remaining time
        proc_list.append(process[j])

    p = process[0]

    for t in range(201):  # for loop to end limit of time for CPU which is 200 time unit
        for element in proc_list:  # put processes depend on arrival time, it will be finished when all arrived
            if t == element[1]:  # process arrived now
                ready_queue.put(element)

        # ======================================Come Back====================================
        while not waiting_queue.empty():  # this loop to set come back of each process
            element = waiting_queue.get()
            temp_list.append(element)
        for element in temp_list:  # for loop to return process to waiting if still waiting or ready if come back
            if t == element[6]:
                ready_queue.put(element)
            else:
                waiting_queue.put(element)
        temp_list.clear()
        # ==================================================================================

        if not ready_queue.empty():
            temp_list.clear()
            while not ready_queue.empty():  # deque all processes in ready queue to update elapsed time in it
                proc = ready_queue.get()
                temp_list.append(proc)  # adding all burst times of processes that is in ready queue

            temp_list = sorted(temp_list, key=lambda x: x[4])
            max_pri = min(temp_list, key=lambda x: x[4])  # get the highest priority process

            # ======================================Remaining Time Elapsed====================================
            if p[8] == 0:  # check if process has finished its remaining time

                completion_time = t
                p[5] = completion_time  # set last completion time for each process
                p[6] = p[3] + completion_time  # save the time of coming back for each process

                gantt_chart_time.append(completion_time)  # for insert the time in chart
                gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart

                p[8] = p[2]  # reset remaining time by burst time
                p[7] = 0    # reset elapsed time to 0

                waiting_queue.put(p)  # put the process in waiting queue
                p = max_pri
                p[7] = 0  # reset elapsed time to 0 since we got the process from ready queue
                temp_list.remove(max_pri)  # so that we got it
            # ===============================================================================================

            elif max_pri[4] < p[4]:  # if there is a process its remaining time less than current process
                temp_list.remove(max_pri)  # so that we got it
                temp_list.append(p)  # return current process to ready again

                gantt_chart_time.append(t)  # for insert the time in chart
                gantt_chart.append("P" + str(p[0]))  # insert process to Gant chart

                p = max_pri  # replacing with the highest priority
                p[7] = 0

            for element in temp_list:  # this for loop to resort the processes in ready queue depend on remaining time
                ready_queue.put(element)
            temp_list.clear()
            # =========================================Update Priority=========================================
            while not ready_queue.empty():  # deque all processes in ready queue to update elapsed time in it
                proc = ready_queue.get()
                if t > proc[1]:  # if they arrived actually
                    proc[7] += 1  # increase elapsed time in ready by 1
                unit = int(proc[7] / time_elapsed)
                if unit >= 1:
                    if proc[4] == 1:  # if priority equals 1
                        proc[4] -= 1
                    elif proc[4] > 1:  # if priority greater than 1
                        if proc[4] - unit > 0:  # if result of subtraction greater than 0, then subtract normally
                            proc[4] -= unit  # decrementing the priority
                        elif proc[4] - unit <= 0:  # if less than or equal 0, then set to high priority '0'
                            proc[4] = 0

                temp_list.append(proc)  # adding all burst times of processes that is in ready queue

            for element in temp_list:  # this for loop to resort the processes in ready queue depend on remaining time
                ready_queue.put(element)
            temp_list.clear()
        # =========================================Update Priority=========================================
        p[8] -= 1  # remaining time elapsed by one

    print("Gantt Chart:\n")
    k = 0
    for element in gantt_chart_time:
        print(element, end='  |')
        if k < len(gantt_chart):
            print(gantt_chart[k], end='|  ')
        k += 1
    print()
    time_calc(process=process)

# =========================================================================================================


# Creation a table for our processes number and their arrival, burst time
# come back after and priority mentioned in the project, to add to that completion, turnaround and waiting time
# last index just for calculating either waiting time or remaining time
processes = [
    [1, 0, 10, 2, 3, 0, 0, 0, 0],
    [2, 1, 8, 4, 2, 0, 0, 0, 0],
    [3, 3, 14, 6, 3, 0, 0, 0, 0],
    [4, 4, 7, 8, 1, 0, 0, 0, 0],
    [5, 6, 5, 3, 0, 0, 0, 0, 0],
    [6, 7, 4, 6, 1, 0, 0, 0, 0],
    [7, 8, 6, 9, 2, 0, 0, 0, 0]
]

print("=============================First Come First Served (F.C.F.S) Algorithm==================================\n")

fcfs(process=processes)

for i in range(7):  # for loop to reinitialize complete, turnaround and waiting times
    processes[i][5] = processes[i][6] = processes[i][7] = processes[i][8] = 0

print("\n=============================Shortest Job First (S.J.F) Algorithm========================================\n")

sjf(process=processes)

for i in range(7):  # for loop to reinitialize complete, turnaround and waiting times
    processes[i][5] = processes[i][6] = processes[i][7] = processes[i][8] = 0

print("\n===========================Shortest Remaining Time First (S.R.T.F) Algorithm=============================\n")

srtf(process=processes)

for i in range(7):  # for loop to reinitialize complete, turnaround and waiting times
    processes[i][5] = processes[i][6] = processes[i][7] = processes[i][8] = 0

print("\n==============================Round Robin (R.R) Algorithm================================================\n")

rr(process=processes)

for i in range(7):  # for loop to reinitialize complete, turnaround and waiting times
    processes[i][5] = processes[i][6] = processes[i][7] = processes[i][8] = 0

print("\n=====================================Preemptive Priority================================================\n")

priority_pre(process=processes)

for i in range(7):  # for loop to reinitialize complete, turnaround and waiting times
    processes[i][5] = processes[i][6] = processes[i][7] = processes[i][8] = 0

print("\n=====================================Non-Preemptive Priority================================================\n")

priority_nonpre(process=processes)

