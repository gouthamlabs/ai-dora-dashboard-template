# Example Python script to collect DORA metrics from CI/CD logs
# (You will need to adapt this for your environment)

import json

def collect_metrics():
    # Placeholder for actual data collection logic
    metrics = {
        "deployment_frequency": 5,
        "lead_time_for_changes": 2,
        "change_failure_rate": 8,
        "mean_time_to_recovery": 1
    }
    with open("metrics.json", "w") as f:
        json.dump(metrics, f)

if __name__ == "__main__":
    collect_metrics()
