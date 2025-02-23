class ApiService:
    tool="Database"
    
    def __init__(self):
        settings = {'params': 'params'}
    
    @classmethod
    def get_name(cls, name):
        return f"{cls.tool}_{name}"

    def getname(self, name):
        prefix = self.settings
        return f"{self.tool}_{name}"

    
if __name__ == "__main__":
    service = ApiService()
    service.tool = "API"
    print(service.getname("validated"))
    print(ApiService.get_name("validated"))
    print(service.get_name("validated"))
