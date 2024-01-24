from pprint import pprint

jobs = {
    "A": {
        "func": "Started A",
        "count": 1,
        "deps": ["A",  "C", "E"]
    },
    "B": {
        "func": "Started B",
        "count": 1,
        "deps": ["B", "C"]
    },
    "C": {
        "func": "Started C",
        "count": 1,
        "deps": ["B", "C"]
    },
    "D": {
        "func": "Started D",
        "count": 1,
        "deps": ["E", "C"]
    },
    "E": {
        "func": "Started D",
        "count": 1,
        "deps": []
    }
}


tasks = []


def run(jobs, name):
    if jobs.get(name):
        print(jobs[name]["func"])
        jobs[name]["count"] += 1
        tasks.append(name)
        print(tasks)
        for item in jobs[name]['deps']:
            if item not in tasks:
                run(jobs, item)


if __name__ == "__main__":

    run(jobs, "D")
    pprint(jobs)
