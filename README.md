# Deep Learning Summer Overview

## Setting up your python environment

* Download and install the latest version of Anaconda from www.anaconda.com
* Create anaconda environment by launching conda prompt and running "conda env create --file dl-summer.yml"
* Download and extract the flikr-8k dataset from kaggle.  All code expects data to reside in a /data directory.  Data directory should have captions.txt and images directory with the jpg files.

Once you have set up your python environment, you can activate it by running a conda shell and activating the environment by running "conda activate dl-summer".  Then you can launch jupyter notebook by running  "jupyter notebook".

## Overview of Jupyter Notebooks

### 001 - Doc2Vec - Flikr 8k Descriptions
This notebook shows how to train a gensim Doc2Vec model to create paragraph embeddings for the flicker captions.