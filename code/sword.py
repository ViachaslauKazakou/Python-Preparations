import json
 
class Weapons:
    def __init__(self):
        self.sword = True
        self.bow = False
 
    def func(self):
        return "ok"
 
    @property
    def all_weapons(self):
        return bool(self.sword and self.bow)
 
class User:
    def __init__(self, _dict=None):
        if _dict:
            self.__dict__ = _dict
            return
        self.name = "Вася"
        self.weapons = Weapons()
 
    def test(self):
        return "test-user"
 
class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return obj.__dict__
        if isinstance(obj, Weapons):
            return obj.__dict__
 
def save_to_json(user):
    filename = "data.json"
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(user, file, ensure_ascii=False, indent=4, cls=MyJSONEncoder)
 
def load_json():
    with open("data.json", 'r', encoding='utf-8') as file:
        data = json.load(file, object_hook=User)
    return data
 
u = User()
save_to_json(u)
 
u2 = load_json()  # type: User
print(type(u2))
print(u2.test())
print(u2)
print(u2.weapons.sword)
print(u2.weapons.func())  # func error
print(u2.weapons.all_weapons)  # property error