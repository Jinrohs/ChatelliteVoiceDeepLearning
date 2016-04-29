# ChatelliteVoiceDeepLearning

Recurrent neural network model for Chatellite Voice.
The network is trained to predict the word given the preceding word sequence.

This code is based on the following RNNLM example implementation.
https://github.com/pfnet/chainer/tree/master/examples/ptb

## How to ues
```
python train_ptb.py -g 0
python genetxt.py -m rnnlm.model -v vocab.bin --length 30 -o 100 > data/foo.result
python convert_to_text.py data/foo.result
```

