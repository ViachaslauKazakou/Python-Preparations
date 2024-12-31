import multiprocessing

def sum_of_squares(start, end, queue):
    try:
        result = sum(i * i for i in range(start, end))
        queue.put(result)
    except Exception as e:
        queue.put(f"Error: {str(e)}")

if __name__ == "__main__":
    range_start = 0
    range_end = 10000000
    num_processes = 4

    chunk_size = (range_end - range_start) // num_processes
    processes = []
    queues = []

    # Create processes with their own queues
    for i in range(num_processes):
        queue = multiprocessing.Queue()
        queues.append(queue)
        start = range_start + i * chunk_size
        end = start + chunk_size
        process = multiprocessing.Process(
            target=sum_of_squares,
            args=(start, end, queue)
        )
        processes.append(process)
        process.start()

    # Collect results
    results = []
    for process, queue in zip(processes, queues):
        process.join()
        result = queue.get()
        if isinstance(result, str) and result.startswith("Error:"):
            print(result)
            continue
        results.append(result)

    total_sum = sum(results)
    print(f"Total sum of squares: {total_sum}")
