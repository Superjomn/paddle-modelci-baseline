import os
import sys
sys.path.append(os.environ['modelci_root'])
from core import CostFactor, DurationFactor, AccFactor

train_acc_factor = AccFactor('train_acc', 0.15)
test_acc_factor = AccFactor('test_acc', 0.15)
train_duration_factor = DurationFactor('train_duration', 0.1)

tracking_factors = [
    train_acc_factor,
    test_acc_factor,
    train_duration_factor,
]
