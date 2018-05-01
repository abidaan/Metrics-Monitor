import json

from src.metrics import get_metrics
from src.sys_info import get_sys_info

payload = {}


def create_identifier_payload(onlyIdentifier=True):
    """
    Creates a json payload with client information
    """
    if onlyIdentifier:
        return json.dumps(payload.update(get_sys_info()))

    payload.update(get_sys_info())


def create_msg_payload():
    """
    Creates the complete message payload
    """
    create_identifier_payload(onlyIdentifier=False)
    return json.dumps(payload.update(get_metrics))
