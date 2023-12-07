import gc

# Включение сборщика мусора
gc.enable()

# Создание объектов с циклическими ссылками
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Создаем циклически связанный список
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(1)
node5 = Node(3)
node1.next = node2
node2.next = node3
node3.next = node1
node4.next = node2
node5.next = node3

# Принудительное выполнение циклического сбора мусора
# gc.collect()
# gc.set_debug(gc.DEBUG_LEAK)
stats = gc.get_stats()
gc.set_threshold(700, 10, 10)
node6 = Node(6)
node7 = Node(7)
node6.next = node1
node7.next = node3
print(stats)
gc.collect()
print(gc.get_stats())
# Получить список всех объектов в текущем пространстве имен
# print(gc.get_objects())