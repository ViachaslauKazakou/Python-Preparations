import asyncio
from dataclasses import dataclass

@dataclass
class Car:
    car: str
    key: bool

    async def start(self):
        check_key = await self._check_key()
        if check_key:
            print(f"car {self.car} started")
            return "started"
        else:
            print(f"No key in  {self.car}  for start")
            return "off"


    async def _check_key(self):
        return True if self.key else False


if __name__ == "__main__":
    car = Car("Ford", False)

    # Run the asynchronous code within an event loop
    asyncio.run(car.start())



