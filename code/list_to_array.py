class LineToTable:
    def __init__(self, flat_list, rows, cols):
        self.flat_list = flat_list
        self.rows = rows
        self.cols = cols
    
    def resize(self):
        # Преобразуем одномерный список в двумерный с помощью срезов и map
        table = list(map(lambda i: self.flat_list[i * self.cols:(i + 1) * self.cols], range(self.rows)))
        return table, (self.rows, self.cols)


class TableToLine:
    def __init__(self, table):
        self.table = table
        self.rows = len(table)
        self.cols = len(table[0]) if table else 0
    
    def resize(self):
        # Преобразуем двумерный список в одномерный с помощью цепочки map и sum
        flat_list = sum(map(list, self.table), [])
        return flat_list, (self.rows, self.cols)


# Примеры использования
if __name__ == "__main__":
    from pprint import pprint
    # Тест для LineToTable
    line_to_table = LineToTable([1, 2, 3, 4, 5, 6], 2, 3)
    result, dims = line_to_table.resize()
    print("LineToTable:")
    pprint(result)
    print(dims)  # (2, 3)

    # Тест для TableToLine
    table_to_line = TableToLine([[1, 2, 3], [4, 5, 6]])
    result, dims = table_to_line.resize()
    print("TableToLine:")
    pprint(result)
    print(dims)  # (2, 3)