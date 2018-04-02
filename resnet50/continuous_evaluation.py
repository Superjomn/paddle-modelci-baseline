import os
import sys
sys.path.append(os.environ['modelci_root'])
from core import CostFactor, DurationFactor, AccFactor

train_acc_factor = AccFactor('train_acc', 0.15)
train_speed_factor = AccFactor('train_speed', 0.15)
gpu_memory_factor = DurationFactor('gpu_memory', 0.01)

tracking_factors = [
    train_acc_factor,
    train_speed_factor,
    gpu_memory_factor,
]
