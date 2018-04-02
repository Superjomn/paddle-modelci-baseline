import os
import sys
sys.path.append(os.environ['modelci_root'])
from core import CostFactor, DurationFactor

train_cost_factor = CostFactor('train_cost', 0.15)
train_duration_factor = DurationFactor('train_duration', 0.15)

tracking_factors = [
    train_cost_factor,
    train_duration_factor,
]
