# Example script for Copilot/agent usage metrics
import json

def collect_copilot_metrics():
    metrics = {
        "suggestion_acceptance_rate": 0.75,
        "usage_count": 120
    }
    with open("copilot_metrics.json", "w") as f:
        json.dump(metrics, f)

if __name__ == "__main__":
    collect_copilot_metrics()
