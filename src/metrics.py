import psutil

from src.util import namedtuple_to_dict


def get_memory_metrics():
    """
    Collects memory metrics and returns a list of objects.
    """
    memory_metrics = {}
    memory_metrics.update(namedtuple_to_dict(psutil.virtual_memory()))
    memory_metrics.update(namedtuple_to_dict(psutil.swap_memory()))

    return {'memory': memory_metrics}


def get_cpu_metrics():
    """
    Collects CPU metrics and returns a list of objects.
    """
    cpu_metrics = {}
    cpu_metrics.update(namedtuple_to_dict(psutil.cpu_stats()))
    cpu_metrics.update(namedtuple_to_dict(psutil.cpu_freq()))
    cpu_metrics.update(namedtuple_to_dict(psutil.cpu_times()))

    return {'cpu': cpu_metrics}


def get_disk_metrics():
    """
    Collects disk metrics and returns a list of objects.
    """
    disk_metrics = {}
    disk_metrics.update(namedtuple_to_dict(psutil.disk_usage('/')))
    disk_metrics.update(namedtuple_to_dict(psutil.disk_io_counters()))

    return {'disk': disk_metrics}


def get_metrics():
    """
    Collects various system metrics and returns a list of objects.
    """
    metrics = {}
    metrics.update(get_memory_metrics())
    metrics.update(get_cpu_metrics())
    metrics.update(get_disk_metrics())

    return metrics
