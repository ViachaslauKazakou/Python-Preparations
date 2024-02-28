Concurrency is one approach to drastically increase the performance of your Python programs. Concurrency allows several processes to be completed concurrently, maximizing the utilization of your system’s resources. Concurrency can be achieved in Python by the use of numerous methods and modules, such as threading, multiprocessing, and asynchronous programming. In this article, we will learn about What is concurrency in Python, the processes required to implement it, some good examples, and the output results.

What is Concurrent Programming?
It refers to the ability of the computer to manage multiple tasks at the same time. These tasks might not be compulsory to execute at the exact same moment but they might interleaved or executed in overlapping periods of time. The main goal of concurrency is to handle multiple user inputs, manage several I/O tasks, or process multiple independent tasks.

What is Parallelism?
Parallelism is a subset of concurrency where tasks or processes are executed simultaneously, As we know concurrency is about dealing with multiple tasks, whereas parallelism is about executing them simultaneously to speed computation. The primary goal is to improve computational efficiency and speed up the [performance of the system.

Thread-Based Concurrency: Threading is a technique for producing lightweight threads (sometimes known as “worker threads”) in a single step. Because these threads share the same memory region, they are ideal for I/O-bound activities.
Process-Based Concurrency: Multiprocessing entails the execution of several processes, each with its own memory space. Because it can use several CPU cores, this is appropriate for CPU-bound activities.
Coroutine-Based Concurrency: Asynchronous programming, with ‘asyncio’ , ‘async’, and ‘await’ keywords, is ideal for efficiently managing I/O-bound processes. It enables tasks to pause and hand over control to other tasks during I/O operations without causing the entire program to crash.
Concurrency vs. Parallelism
Concurrency: It refers to the execution of many tasks in overlapping time periods, but not necessarily concurrently. It is appropriate for I/O-bound operations that frequently rely on external resources such as files or network data.


В Python concurrency и parallelism относятся к способам обработки задач, которые могут выполняться одновременно. Однако они имеют разные концепции и применения.

Concurrency (Конкурентность):

Определение: Конкурентность означает выполнение нескольких задач одновременно, но не обязательно одновременно во времени. Это может быть реализовано с помощью механизмов, таких как многопоточность или асинхронное программирование.
Примеры: Многопоточные приложения, асинхронные приложения.
Реализация в Python: В Python конкурентность часто достигается с использованием библиотеки asyncio для асинхронного программирования или модуля threading для многопоточности.
Parallelism (Параллелизм):

Определение: Параллелизм означает выполнение нескольких задач одновременно в реальном времени, в один и тот же момент времени, используя физически параллельные ресурсы, такие как несколько ядер процессора.
Примеры: Многопроцессорные вычисления, распределенные вычисления.
Реализация в Python: Для параллелизма в Python обычно используются библиотеки такие как multiprocessing, которые позволяют запускать различные процессы, выполняющиеся параллельно.
Отличие между конкурентностью и параллелизмом в Python заключается в том, что конкурентность может быть достигнута без реальной параллельной работы, например, когда один поток или процесс переключается между задачами в многозадачной среде, в то время как параллелизм использует фактические параллельные ресурсы для выполнения задач в одно и то же время.



