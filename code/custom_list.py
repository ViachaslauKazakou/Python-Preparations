class FunnyList(list):

    def append(self, item):
        self.insert(0, item)


funny_list = FunnyList("")

funny_list.append(10)
funny_list.append(11)
funny_list.append(12)

print(*funny_list)
print(*sorted(funny_list))
print(*FunnyList())
