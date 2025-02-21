# CPU Scheduling Simulator

A simulation project that implements various CPU scheduling algorithms to compute Gantt charts, average waiting times, and average turnaround times for a given set of processes.

## Summary
This project simulates the scheduling of a set of processes over a period of 200 time units. Each process is characterized by an arrival time, burst time, a “come back” delay (representing the time after which the process reenters the ready queue), and an initial priority. The simulation supports six scheduling algorithms: First Come First Served (FCFS), Shortest Job First (SJF), Shortest Remaining Time First (SRTF), Round Robin (with a time quantum of 5), Preemptive Priority Scheduling with aging (where a process’s priority is decremented by 1 every 5 time units spent in the ready queue), and Non-preemptive Priority Scheduling with aging. For each algorithm, the program displays a Gantt chart along with the calculated average waiting time and average turnaround time.

## Specifications
- **Process Attributes:**
  - **Process ID**
  - **Arrival Time**
  - **Burst Time**
  - **Come Back Time:** The delay after which the process returns to the ready queue once its burst is complete.
  - **Priority:** An initial value that can be aged (decremented) if the process waits in the ready queue.

- **Simulation Duration:**
  - The simulation runs for 200 time units.

- **Scheduling Algorithms:**
  1. **First Come First Served (FCFS):** Processes are executed in order of arrival.
  2. **Shortest Job First (SJF):** Processes are scheduled in ascending order of burst time.
  3. **Shortest Remaining Time First (SRTF):** A preemptive variant of SJF that always selects the process with the smallest remaining burst time.
  4. **Round Robin (RR):** Uses a time quantum of 5; processes are cycled through, with any unfinished burst continuing in subsequent rounds.
  5. **Preemptive Priority Scheduling (with aging):** Processes are preempted if a process with a higher priority (lower numerical value) arrives or ages (priority decremented by 1 for every 5 time units in the ready queue).
  6. **Non-Preemptive Priority Scheduling (with aging):** Processes are scheduled based on priority (with aging) but run to completion once started.

- **Outputs:**
  - **Gantt Chart:** A timeline showing the order and duration of process execution.
  - **Average Waiting Time:** The mean time that processes wait in the ready queue.
  - **Average Turnaround Time:** The mean time from process arrival to its completion.

- **Implementation Details:**
  - The simulation is implemented in Python using queues and priority queues.
  - After each scheduling algorithm runs, process metrics (completion time, turnaround time, and waiting time) are computed and printed.
  - The simulator resets the process times between algorithms to ensure independent evaluation.

- **Evaluation:**
  - The program prints a table summarizing the completion, turnaround, and waiting times for each process.
  - It then displays the Gantt chart and the computed average times for each scheduling algorithm.

## Author

Qusay Taradeh
