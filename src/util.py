def namedtuple_to_dict(data):
    """
    Converts a namedtuple to a dictionary with the top-level key being the class name.
    """
    return {type(data).__name__.lower(): dict(data._asdict())}
