from pymongo import MongoClient

# client = MongoClient('mongodb://admin:admin@localhost:27017/')
# db = client['test_database']
# collection = db['ip_address']

class MongoView:
    
    def __init__(self):
        self.client = MongoClient('mongodb://admin:admin@localhost:27017/')
        self.db = self.client['test_database']
        
    def read_all_ip(self):
        collection = self.db['ip_address']
        result = collection.find({'name':'John'})
        print("Results: ===========")
        for item in result:
            print(item.get("_id"))
            print(item.get("name"))
        
    def insert_data(self, key, value):
        collection = self.db['ip_address']
        data = {"name": "John", "city": "Ohio"}
        collection.insert_one(data)
        
    def find_data(self, key):
        collection = self.db['ip_address']
        print(collection.find_one(key))



if __name__ == '__main__':
    client = MongoView()
    client.insert_data("id", "122334")
    client.read_all_ip()
    client.find_data({'name':'John'})