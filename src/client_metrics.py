import json

from src.metric import metrics
from src.metric import util

metrics_dict = {}
metrics = metrics.get_metrics()

for metric in metrics:
    metrics_dict.update(util.namedtuple_to_dict(metric))

json_metrics = json.dumps(metrics_dict)

