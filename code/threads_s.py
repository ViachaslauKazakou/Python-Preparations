import threading
import time

# Создаем семафор с ограничением на 2 потока
semaphore = threading.Semaphore(5)

# Функция, которую будут выполнять потоки
def worker(thread_id):
    print(f"Поток {thread_id} ожидает разрешения семафора")

    # Попытка получить разрешение от семафора
    semaphore.acquire()
    print(f"Поток {thread_id} получил разрешение семафора и начинает работу")

    # Эмулируем работу потока
    for i in range(5):
        print(f"Поток {thread_id}: шаг {i}")
        time.sleep(1)

    print(f"Поток {thread_id} завершил работу и освободил семафор")
    semaphore.release()


# Создаем и запускаем 5 потоков
if __name__ == "__main__":
    start_time = time.time()
    print("start working")
    threads = []
    for i in range(1, 11):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    # Ожидаем завершения всех потоков

    for thread in threads:
        thread.join()

    print(f"Все потоки завершили работу: {time.time()-start_time}")
