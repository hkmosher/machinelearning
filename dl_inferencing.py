#dl_inferencing.py contains functions for Doc2Vec inferencing.

from gensim.models.doc2vec import Doc2Vec
from hashlib import sha256

MODEL = Doc2Vec.load('Models/Flickr-8k-Doc2Vec.h5', mmap='r')

def infer_vector(document):
    vector = MODEL.infer_vector(document.split(' '), epochs=500, alpha=MODEL.alpha)
    documenthash = sha256(document.encode('utf-8')).hexdigest()
    return documenthash, vector
