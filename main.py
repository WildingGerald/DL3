import string
from abc import ABC, abstractmethod
from typing import List

import main


class Process:
    process_id_counter = 1

    def __init__(self, burst_time: int, priority: int = 0):
        self.waiting_time = None
        self.turnaround_time = None
        self.burst_time = burst_time
        self.priority = priority
        self.process_id = main.Process.process_id_counter
        main.Process.process_id_counter += 1

    def set_waiting_time(self, waiting_time):
        self.waiting_time = waiting_time

    def set_turnaround_time(self, turnaround_time):
        self.turnaround_time = turnaround_time

    def __repr__(self):
        return f"Process Id: {self.process_id}"


class Algorithm(ABC):

    def __init__(self, type_of_algorithm: string):
        self.avg_waiting_time = None
        self.avg_turnaround_time = None
        self.algorythm_type = type_of_algorithm
        self.total_waiting_time = 0
        self.total_turnaround_time = 0

    def calculate_avg(self, que: List):
        for i in range(len(que)):
            if i == 0:
                que[i].set_waiting_time(0)
                que[i].set_turnaround_time(que[i].burst_time)
                self.total_waiting_time = que[i].burst_time
                self.total_turnaround_time = que[i].burst_time
            elif i == len(que)-1:
                que[i].set_waiting_time(que[i - 1].waiting_time + que[i].burst_time)
                que[i].set_turnaround_time(que[i].waiting_time + que[i].burst_time)
                self.total_turnaround_time += que[i].burst_time
            else:
                que[i].set_waiting_time(que[i - 1].waiting_time + que[i].burst_time)
                self.total_waiting_time += que[i].waiting_time
                que[i].set_turnaround_time(que[i].waiting_time + que[i].burst_time)
                self.total_turnaround_time += que[i].burst_time
            self.avg_waiting_time = self.total_waiting_time / len(que)
            self.avg_turnaround_time = self.total_turnaround_time / len(que)

    def __repr__(self):
        return f"Algorithm {self.algorythm_type}:\n" \
               f"Average waiting Time: {self.avg_waiting_time}\n" \
               f"Average turnaround time: {self.avg_turnaround_time}\n"

    @abstractmethod
    def sort(self, que: List):
        pass


class FirstComeFirstServe(Algorithm):
    def __init__(self):
        super(FirstComeFirstServe, self).__init__("First Come First Serve")

    def sort(self, que: List):
        # firstComeFirstServe doesn't require additional sorting
        for x in que:
            print(repr(x))


class ShortestJobFirst(Algorithm):
    def __init__(self):
        super(ShortestJobFirst, self).__init__("Shortest Job First")

    def sort(self, que: List):
        que.sort(reverse=False, key=lambda process: process.burst_time)
        for x in que:
            print(repr(x))


class PriorityScheduling(Algorithm):
    def __init__(self):
        super(PriorityScheduling, self).__init__("Priority Scheduling")

    def sort(self, que: List):
        que.sort(reverse=False, key=lambda process: process.priority)
        for x in que:
            print(repr(x))


def test_algorithm(alg: Algorithm, que: List):
    alg.sort(que)
    alg.calculate_avg(que)
    print(repr(alg))


if __name__ == '__main__':

    print("Number of Processes: ", end="")
    number_of_processes = int(input())
    que = []
    for i in range(number_of_processes):
        print(f"Burst time for process {i + 1}: ", end="")
        burst_time = int(input())
        print(f"Priority for process {i + 1}: ", end="")
        que.append(Process(burst_time, (input())))
    print()

    first_come_first_serve = FirstComeFirstServe()
    shortest_job_first = ShortestJobFirst()
    priority_scheduling = PriorityScheduling()

    test_algorithm(first_come_first_serve, que.copy())
    test_algorithm(shortest_job_first, que.copy())
    test_algorithm(priority_scheduling, que.copy())
