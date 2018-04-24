import psutil

def get_metrics():
    """
    Collects various system metrics and returns a list of objects.
    """
    # Memory statistics

    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()

    # CPU statistics

    interrupts = psutil.cpu_stats()
    cpu_frequency = psutil.cpu_freq()
    cpu_time = psutil.cpu_times()

    # Disk statistics

    disk_usage = psutil.disk_usage('/')
    disk_counters = psutil.disk_io_counters()

    return [virtual_memory, swap_memory, interrupts, cpu_frequency, cpu_time,
            disk_usage, disk_counters]