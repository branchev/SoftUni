from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from typing import List

from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name:str, capacity:int, memory:int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name:str, capacity:int, memory:int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        try:
            hw = [h for h in System._hardware if h.name == hardware_name][0]
            sw = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hw.install(sw)
            System._software.append(sw)
        except IndexError:
            return "Hardware does not exist"
        except Exception as exc:
            return str(exc)

    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        try:
            hw = [h for h in System._hardware if h.name == hardware_name][0]
            sw = LightSoftware(name, capacity_consumption, memory_consumption)
            hw.install(sw)
            System._software.append(sw)
        except IndexError:
            return "Hardware does not exist"
        except Exception as exc:
            return str(exc)

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        try:
            hw = [h for h in System._hardware if h.name == hardware_name][0]
            sw = [s for s in System._software if s.name == software_name][0]
            hw.uninstall(sw)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        output = "System Analysis\n"
        count_of_hardware_components = len(System._hardware)
        output += f"Hardware Components: {count_of_hardware_components}\n"
        count_of_software_components = len(System._software)
        output += f"Software Components: {count_of_software_components}\n"
        total_memory = sum([x.memory for x in System._hardware])
        total_used_memory = sum([x.memory_consumption for x in System._software])
        output += f"Total Operational Memory: {total_used_memory} / {total_memory}\n"
        total_used_space = sum([x.capacity_consumption for x in System._software])
        total_capacity = sum([x.capacity for x in System._hardware])
        output += f"Total Capacity Taken: {total_used_space} / {total_capacity}"
        return output

    @staticmethod
    def system_split():
        output = ""
        for hw_component in System._hardware:
            output += f"Hardware Component - {hw_component.name}\n"
            exp_sw_components = [
                x for x in hw_component.software_components if x.__class__.__name__ == "ExpressSoftware"
                ]
            output += f"Express Software Components: {len(exp_sw_components)}\n"
            l_sw_components = [
                x for x in hw_component.software_components if x.__class__.__name__ == "LightSoftware"
            ]
            output += f"Light Software Components: {len(l_sw_components)}\n"
            total_memory_used = [x.memory_consumption for x in hw_component.software_components]
            output += f"Memory Usage: {sum(total_memory_used)} / {hw_component.memory}\n"
            total_capacity_used = [x.capacity_consumption for x in hw_component.software_components]
            output += f"Capacity Usage: {sum(total_capacity_used)} / {hw_component.capacity}\n"
            output += f"Type: {hw_component.type}\n"
            names_of_sw_components = [x.name for x in hw_component.software_components]
            if names_of_sw_components:
                output += f"Software Components: {', '.join(names_of_sw_components)}"
            else:
                output += f"Software Components: None"
        return output

