import sys
print(sys.executable)
print("start")
import os
from db_provider import Session
from sqlalchemy import select
from models import BlockedID, Description
import random
import string
from functools import wraps
import time



def timer(func):
    """ Return calc time of execution wrapped function"""

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start = time.time()
        result = func(self, *args, **kwargs)
        print(f"Execution time: {time.time() - start}")
        return result

    return wrapper


class DbFinder:

    def __init__(self):
        pass

    def get_all_id(self):
        with Session() as session:
            stmt = select(BlockedID)
            result = session.execute(stmt).all()
        print(result)

    @timer
    def get_id(self, ipid):
        stmt = (
            select(BlockedID)
            .join(Description, Description.blocked_id == BlockedID.id, isouter=True)
            .where(BlockedID.ip_id == ipid))
        with Session() as session:

            print("="*120)
            print(stmt)
            result = session.execute(stmt).one()
            print("-" * 120)
            print(result)
            
    @timer
    def get_descr(self):
        stmt = (
            select(Description)
            .join(BlockedID)
            .where()
        )

    def add_ip(self):
        with Session() as session:
            data_bunch = []
            for i in range(1000):
                data_bunch.append(BlockedID(ip_id=self.create_random_string(), title=self.create_random_string()))
            session.add_all(data_bunch)
            session.commit()

    def add_description(self, idip, url):
        stmt = Description(blocked_ip=idip, url=url)
        with Session as session:
            session.add(stmt)
            session.commit()

    def create_random_string(self):
        char = string.ascii_letters + "1234567890"
        return ''.join(random.choice(char) for _ in range(30))

    def start(self):
        print(f"Seaacher running with:")


if __name__ == "__main__":
    print("Start finder")

    finder = DbFinder()
    # DbFinder().get_all_id()
    finder.get_id("mIiVBR23U2dooVjRzmCn0eC8a4XMcg")
    finder.get_id("wHx0pgTK4kOoI9nc7dp9b9NV7uBqnn")
    finder.get_id("1234456")
    # finder.add_description(1, "http://my.com/123")
