import cv2
import multiprocessing as mp
import datetime
import time

VIDEO_PATH = "input.mp4"  # Путь к входному видеофайлу
OUTPUT_PATH = 'output.mp4'
NUM_WORKERS = 16
MAX_QUEUE_SIZE = 100


def neg(freim):
    img_bgr = freim
    height, width, _ = img_bgr.shape
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pixel = img_bgr[i, j]
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
            img_bgr[i, j] = pixel
    return img_bgr


def reader(cap_path, input_queue, stop_event):
    cap = cv2.VideoCapture(cap_path)
    frame_id = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        input_queue.put((frame_id, frame))
        frame_id += 1
    cap.release()
    stop_event.set()  # Сигнализируем, что чтение завершено


def worker(input_queue, output_queue, stop_event):
    while not stop_event.is_set() or not input_queue.empty():
        try:
            frame_id, frame = input_queue.get(timeout=1)
            processed = neg(frame)
            output_queue.put((frame_id, processed))
        except:
            continue


def writer(output_queue, stop_event, total_frames, output_path, frame_size, fps):
    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        frame_size
    )
    buffer = {}
    next_frame_id = 0

    while not stop_event.is_set() or not output_queue.empty() or buffer:
        try:
            frame_id, frame = output_queue.get(timeout=1)
            buffer[frame_id] = frame
        except:
            continue

        while next_frame_id in buffer:
            out.write(buffer.pop(next_frame_id))
            next_frame_id += 1

    out.release()


if __name__ == '__main__':
    mp.set_start_method('spawn')  # Особенно важно на Windows

    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("Не удалось открыть видео")
        exit()

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    input_queue = mp.Queue(MAX_QUEUE_SIZE)
    output_queue = mp.Queue(MAX_QUEUE_SIZE)
    stop_event = mp.Event()

    print("Запуск потоков...")

    reader_process = mp.Process(target=reader, args=(VIDEO_PATH, input_queue, stop_event))
    writer_process = mp.Process(target=writer, args=(
        output_queue, stop_event, total_frames, OUTPUT_PATH, (width, height), fps
    ))
    workers = [
        mp.Process(target=worker, args=(input_queue, output_queue, stop_event))
        for _ in range(NUM_WORKERS)
    ]

    start = datetime.datetime.now()

    reader_process.start()
    writer_process.start()
    for w in workers:
        w.start()

    reader_process.join()
    for w in workers:
        w.join()
    stop_event.set()
    writer_process.join()

    end = datetime.datetime.now()
    print("Обработка завершена. Время:", end - start)
