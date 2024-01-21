import os
import random
import time
from functools import wraps


def timer(func):
    """ Return calc time of execution wrapped function"""
    @wraps(func) 
    
    def wrapper(self, *args, **kwargs):
        start = time.time()
        result = func(self, *args, **kwargs)
        print(f"Execution time: {time.time() - start}")
        return result
    return wrapper


class SimpleFinder:

    def __init__(self):
        pass

    def add_ip(self):
        name = random.randint(40000, 49999)
        # name = 49342
        print(f"Function started. got Ip: {name}")
        file_name = self.get_filename(name)
        if self._if_exist(file_name):
            # print(f"File {file_name} exists")
            self.add_butch(file_name, name)
        else:
            # print(f"File {file_name} does not exists")
            self.create_butch(file_name, name)

    def get_filename(self, name):
        first_name = str(int(name / 10000))
        return "".join((first_name, "0000"))

    def _if_exist(self, filename):
        files_list = (os.listdir("file_finder/storage"))
        if filename in files_list:
            return True
        return False
    
    def create_butch(self, file_name, name):
        with open(f"file_finder/storage/{file_name}", "w+") as f:
            f.write(str(name))
            f.write(" ")

    def add_butch(self, file_name, name):
        with open(f"file_finder/storage/{file_name}", "a+") as f:
            f.write(str(name))
            f.write(" ")

    @timer
    def find_ip(self, name):
        filename = self.get_filename(name)
        if filename:
            print(f"Found file {filename} for checking ip {name}")
            with open(f"file_finder/storage/{filename}") as f:
                while line := f.readline():
                    print(line)
                    print("-" * 100)
                    if name in line.strip().split(" "):
                        print(f"This ip({name}) was blocked for download")
                        break

                # data_ip = f.read()
                # if data_ip:
                #     ip_list = data_ip.split(' ')
                #     print(f"Count of records: {len(ip_list)}")
                #     if str(name) in ip_list:
                #         print(f"This ip({name}) was blocked for download")
                #         return
        print(f"This ip({name}) can be download!!!")


if __name__ == "__main__":

    # res = SimpleFinder()
    # res.add_ip()
    print(timer.__doc__)
    print("="*120)
    print("Start script")
    # for i in range(100000):
    #     res = SimpleFinder()
    #     res.add_ip()
    # SimpleFinder().add_ip()
    res = SimpleFinder().find_ip(49342)
