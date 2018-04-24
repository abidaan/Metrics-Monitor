import json

import metrics
import util


metrics_dict = {}

metrics = metrics.get_metrics()

for metric in metrics:
    metrics_dict.update(util.namedtuple_to_dict(metric))


json_metrics = json.dumps(metrics_dict)

print(json_metrics)
