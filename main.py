import psutil
import platform
import socket
from datetime import datetime


def get_system_info():
    return {
        "Hostname": socket.gethostname(),
        "Platform": platform.system(),
        "Platform Version": platform.version(),
        "Architecture": platform.machine(),
        "Boot Time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    }


def get_cpu_info():
    return {
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
        "CPU Usage": f"{psutil.cpu_percent(interval=1)}%"
    }


def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        "Total Memory": f"{mem.total / (1024 ** 3):.2f} GB",
        "Available Memory": f"{mem.available / (1024 ** 3):.2f} GB",
        "Used Memory": f"{mem.used / (1024 ** 3):.2f} GB",
        "Memory Usage": f"{mem.percent}%"
    }


def get_disk_info():
    disk_usage = psutil.disk_usage('/')
    return {
        "Total Disk": f"{disk_usage.total / (1024 ** 3):.2f} GB",
        "Used Disk": f"{disk_usage.used / (1024 ** 3):.2f} GB",
        "Free Disk": f"{disk_usage.free / (1024 ** 3):.2f} GB",
        "Disk Usage": f"{disk_usage.percent}%"
    }


def get_network_info():
    net_io = psutil.net_io_counters()
    return {
        "Bytes Sent": f"{net_io.bytes_sent / (1024 ** 2):.2f} MB",
        "Bytes Received": f"{net_io.bytes_recv / (1024 ** 2):.2f} MB"
    }


def print_report():
    print("\nSERVER HEALTH REPORT")
    print("======================\n")

    print("System Info:")
    for k, v in get_system_info().items():
        print(f"  {k}: {v}")

    print("\nCPU Info:")
    for k, v in get_cpu_info().items():
        print(f"  {k}: {v}")

    print("\nMemory Info:")
    for k, v in get_memory_info().items():
        print(f"  {k}: {v}")

    print("\nDisk Info:")
    for k, v in get_disk_info().items():
        print(f"  {k}: {v}")

    print("\nNetwork Info:")
    for k, v in get_network_info().items():
        print(f"  {k}: {v}")


if __name__ == '__main__':
    print_report()
