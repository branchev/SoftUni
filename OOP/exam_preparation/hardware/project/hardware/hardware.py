from project.software.software import Software
from typing import List


class Hardware:
    def __init__(self, name: str, type: str, capacity:int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    def install(self, software: Software):
        if self.available_memory >= software.memory_consumption and \
                self.available_capacity >= software.capacity_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def available_memory(self):
        return self.memory - sum([x.memory_consumption for x in self.software_components])

    @property
    def available_capacity(self):
        return self.capacity - sum([x.capacity_consumption for x in self.software_components])
