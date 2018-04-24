import psutil

import src.util

metrics_dict = {"cpu": {}, "memory": {}, "disk": {}}


def get_memory_metrics():
    """
    Collects memory metrics and returns a list of objects.
    """
    memory_metrics = []
    memory_dict = {}
    metrics.append(psutil.virtual_memory())
    metrics.append(psutil.swap_memory())

    for metric in memory_metrics:
        memory_dict.update(util.namedtuple_to_dict(metric))

    metrics_dict["memory"] = memory_dict


def get_cpu_metrics():
    """
    Collects CPU metrics and returns a list of objects.
    """
    cpu_metrics = []
    cpu_dict = {}
    metrics.append(psutil.cpu_stats())
    metrics.append(psutil.cpu_freq())
    metrics.append(psutil.cpu_times())

    for metric in cpu_metrics:
        cpu_dict.update(util.namedtuple_to_dict(metric))

    metrics_dict["cpu"] = cpu_dict


def get_disk_metrics():
    """
    Collects disk metrics and returns a list of objects.
    """
    disk_metrics = []
    disk_dict = {}
    metrics.append(psutil.disk_usage('/'))
    metrics.append(psutil.disk_io_counters())

    for metric in disk_metrics:
        disk_dict.update(util.namedtuple_to_dict(metric))

    metrics_dict["disk"] = disk_dict


def get_metrics():
    """
    Collects various system metrics and returns a list of objects.
    """
    get_memory_metrics()
    get_cpu_metrics()
    get_disk_metrics()

