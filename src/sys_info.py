import platform
import socket
import uuid


def generate_uuid():
    """
    Generates a UUID with the use of mac address
    """
    return {'UUID': str(uuid.uuid1())}


def get_mac_address():
    """
    Gets the mac address of the system
    """
    return {'MAC_ADDRESS': hex(uuid.getnode())}


def get_hostname():
    """
    Gets the hostname of the system
    """
    return {'HOSTNAME': socket.getfqdn()}


def get_os_version():
    """
    Gets the os name and version
    """
    return {'OS_NAME': platform.platform()}


def get_sys_info():
    """
    Gets the unique ID, MAC address, Hstname and the OS version for the system
    """
    sys_info = {}
    sys_info.update(generate_uuid())
    sys_info.update(get_mac_address())
    sys_info.update(get_hostname())
    sys_info.update(get_os_version())

    return sys_info
