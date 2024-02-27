
PROJECT_ID = "project_one"


def verify_param(func):
    def wrapper(self, *args, **kwargs):
        if kwargs.get("project_id"):
            pid = kwargs["project_id"]
        else:
            pid = PROJECT_ID

        result = func(self, project_id=pid)
        return result
    return wrapper


class MyClass:

    @verify_param
    def get_project(self, project_id):
        return [project_id]


print(MyClass().get_project(project_id="project_two"))
