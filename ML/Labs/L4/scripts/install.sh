#!/bin/bash

curl -L -o ~/Study/S6/ML/Labs/L5/fresh-and-stale-classification.zip \
    https://www.kaggle.com/api/v1/datasets/download/swoyam2609/fresh-and-stale-classification

unzip fresh-and-stale-classification.zip -d  ~/Study/S6/ML/Labs/L5/dataset/
rm fresh-and-stale-classification.zip`