import psutil

from src.util import namedtuple_to_dict

metrics_dict = {"cpu": {}, "memory": {}, "disk": {}}


def get_memory_metrics():
    """
    Collects memory metrics and returns a list of objects.
    """
    memory_metrics = []
    memory_dict = {}
    memory_metrics.append(psutil.virtual_memory())
    memory_metrics.append(psutil.swap_memory())

    for metric in memory_metrics:
        memory_dict.update(namedtuple_to_dict(metric))

    metrics_dict["memory"] = memory_dict


def get_cpu_metrics():
    """
    Collects CPU metrics and returns a list of objects.
    """
    cpu_metrics = []
    cpu_dict = {}
    cpu_metrics.append(psutil.cpu_stats())
    cpu_metrics.append(psutil.cpu_freq())
    cpu_metrics.append(psutil.cpu_times())

    for metric in cpu_metrics:
        cpu_dict.update(namedtuple_to_dict(metric))

    metrics_dict["cpu"] = cpu_dict


def get_disk_metrics():
    """
    Collects disk metrics and returns a list of objects.
    """
    disk_metrics = []
    disk_dict = {}
    disk_metrics.append(psutil.disk_usage('/'))
    disk_metrics.append(psutil.disk_io_counters())

    for metric in disk_metrics:
        disk_dict.update(namedtuple_to_dict(metric))

    metrics_dict["disk"] = disk_dict


def get_metrics():
    """
    Collects various system metrics and returns a list of objects.
    """
    get_memory_metrics()
    get_cpu_metrics()
    get_disk_metrics()
