import os
import sys
sys.path.append(os.environ['modelci_root'])
from core import CostFactor, DurationFactor, AccFactor

cifar10_128_train_acc_factor = AccFactor('cifar10_128_train_acc', 0.15)
cifar10_128_train_speed_factor = AccFactor('cifar10_128_train_speed', 0.15)
cifar10_128_gpu_memory_factor = DurationFactor('cifar10_128_gpu_memory', 0.01)

flowers_64_train_speed_factor = AccFactor('flowers_64_train_speed', 0.15)
flowers_64_gpu_memory_factor = DurationFactor('flowers_64_gpu_memory', 0.01)

tracking_factors = [
    cifar10_128_train_acc_factor,
    cifar10_128_train_speed_factor,
    cifar10_128_gpu_memory_factor,
    flowers_64_train_speed_factor,
    flowers_64_gpu_memory_factor,
]
