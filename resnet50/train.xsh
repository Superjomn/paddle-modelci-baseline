#!/usr/bin/env xonsh
import os
import sys
# import argparse
# parser = argparse.ArgumentParser('train script')
# parser.add_argument('--train_cost_out', type=str)
# parser.add_argument('--valid_cost_out', type=str)
# parser.add_argument('--gpu', type=int, default=-1)
# args = parser.parse_args($ARGS[1:])

model_file = 'resnet.py'
export MKL_NUM_THREADS=1
export OMP_NUM_THREADS=1
export CUDA_VISIBLE_DEVICES=3
# cifar10 128
FLAGS_benchmark=true FLAGS_fraction_of_gpu_memory_to_use=0.0 python @(model_file) --device=GPU --batch_size=128 --data_set=cifar10 --model=resnet_cifar10 --pass_num=30
python get_gpu_data.py --batch_size=128 --data_set=cifar10
#flowers 64
FLAGS_benchmark=true FLAGS_fraction_of_gpu_memory_to_use=0.0 python @(model_file) --device=GPU --batch_size=64 --data_set=flowers --model=resnet_imagenet --pass_num=3
python get_gpu_data.py --batch_size=64 --data_set=flowers
