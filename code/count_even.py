import array as arr
import time
from queue import Queue
from typing import List
import threading
def is_even(lst):
    result = filter(lambda x: x % 2 == 0, lst)
    print(result)
    print(type(result))
    print(dir(result))
    print(next(result))
    return list(result)

def create_queue(lst: List):
    qlist = Queue()
    for item in lst:
        qlist.put(item)
    return qlist


def print_names_from_queue(q):
    while True:
        name = q.get()
        print(f"Processing user {name}")
        time.sleep(1)
        q.task_done()
        print(q.qsize())
        if q.empty():
            print(f'Queue has {q.qsize()} elements processing stopping')
            break


def append_queue(que):
    for _ in range(20):
        que.put(f"User{_}")
        print(f"User{_} added to queue")
        time.sleep(2)

if __name__ == "__main__":
    lst = [i for i in range(20)]
    print(is_even(lst))
    x = (i for i in range(20))

    myr = arr.array("i", [1,2,3,4,5])
    users_list = ['John', 'Peter', 'Alice', 'Arni']
    users = create_queue(users_list)
    # print_names_from_queue(users)
    workers = []
    worker_process = threading.Thread(target=print_names_from_queue, args=(users,))
    worker_queue = threading.Thread(target=append_queue, args=(users,))
    worker_process.start()
    worker_queue.start()
    workers.append(worker_process)
    workers.append(worker_queue)

    # self.task_queue.join()
    # Wait for worker threads to finish
    for worker_thread in workers:
        worker_thread.join(timeout=1)

