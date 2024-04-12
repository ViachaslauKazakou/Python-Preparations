import gc

# Включение сборщика мусора
gc.enable()
gc.set_threshold(100, 5, 3)
# Создание объектов с циклическими ссылками
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Создаем циклически связанный список
print(len(gc.get_objects()))
node1 = Node(100)
node2 = Node(2)
node3 = Node(3)
node4 = Node(1)
node5 = Node(3)
node6 = Node(33)
node7 = Node(33)

node1.next = node2
node2.next = node3
node3.next = node1
node4.next = node2
node5.next = node3
node5.next = node3
node6.next = node3
node6.next = node2
node6.next = node1

# del node2

# Принудительное выполнение циклического сбора мусора
# gc.set_debug(gc.DEBUG_LEAK)
print(len(gc.get_objects()))
print(gc.get_count())
stats = gc.get_stats()
node6 = Node(6)
node6.next = node5
node7.next = node1
node7.next = node2
print(gc.get_stats())
print(gc.get_count())
gc.collect()
print(gc.get_stats())
print(gc.get_count())
# Получить список всех объектов в текущем пространстве имен
print(len(gc.get_objects()))