#!/bin/bash

curl -L -o ~/Study/S6/ML/Labs/L2/bitcoin-historical-data.zip https://www.kaggle.com/api/v1/datasets/download/mczielinski/bitcoin-historical-data
unzip ~/Study/S6/ML/Labs/L2/bitcoin-historical-data.zip -d ~/Study/S6/ML/Labs/L2/dataset/
rm ~/Study/S6/ML/Labs/L2/bitcoin-historical-data.zip