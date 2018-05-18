import json

from src.metrics import get_metrics
from src.sys_info import get_sys_info


def create_identifier_payload(only_identifier=True):
    """
    Creates a json payload with client information
    """
    if only_identifier:
        return json.dumps(get_sys_info())

    return get_sys_info()


def create_msg_payload():
    """
    Creates the complete message payload
    """
    payload = {}
    payload.update(create_identifier_payload(only_identifier=False))
    payload.update(get_metrics())
    return json.dumps(payload)
