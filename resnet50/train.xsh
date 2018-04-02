#!/usr/bin/env xonsh
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
FLAGS_benchmark=true python @(model_file) --device=GPU --batch_size=128 --data_set=cifar10 --model=resnet_cifar10 --pass_num=30
