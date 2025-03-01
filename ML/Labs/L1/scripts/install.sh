#!/bin/bash

curl -L -o ~/Study/S6/ML/L1/fer2013.zip https://www.kaggle.com/api/v1/datasets/download/msambare/fer2013
unzip fer2013.zip -d ../dataset/
rm fer2013.zip