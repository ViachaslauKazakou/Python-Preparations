# filter incorrect login. login must contain only letters, numbers and "_"
import re
def filter_login(logins):
    # if not isinstance(logins, list):
    #     raise TypeError("Expected a list of logins")
    pattern = re.compile(r'^\w+$')
    return [login for login in logins if pattern.match(login)]

# def filter_login(logins):
#     pattern = re.compile(r'^\w+$')
#     return [login for login in logins if pattern.match(login)]
#     return [login for login in logins if login.isalnum() and '_' in login]

if __name__ == "__main__":
    logins = ['admin', 'us_er', 'gue-st', 'root', 'superus*er', 'u12s&er', 'ro.ot']
    print(filter_login(logins))