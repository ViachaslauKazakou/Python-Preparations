from dataclasses import dataclass
from typing import List, Dict

import attr


def ged():
    return 15

@dataclass
class Request:
    session: str

    def get(self):
        return f"Got {self.session}, data= {self.get_data(12)}"

    def __getitem__(self, item):
        return getattr(self, item)

    def get_data(self, data):
        return ged() + data


@attr.attrs(slots=True, auto_attribs=True)
class Datacenter:
    id: int
    # location_id: int
    total_cpu_mhz: int
    # total_cpu_cores: int
    # total_clients: int
    # total_memory_mb: int
    updated_at: int
    nodes: List[Dict]
    isas: List[str]

    def to_json(self) -> Dict:
        return attr.asdict(
            self,
            filter=attr.filters.exclude(
                attr.fields(Datacenter).updated_at,
                attr.fields(Datacenter).nodes,
            ),
        )


if __name__ == "__main__":
    # a = Request("session23456")
    # print(dir(a))
    # print(a.session)
    # print(a.get())
    # print(a["session"])

    dt = Datacenter(1, 2, 4, [],[1])
    res = dt.to_json()
    print(res)

