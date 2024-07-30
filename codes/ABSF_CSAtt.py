# author: Xincheng Yu

import torch
import torch.nn as nn
import numpy as np

class ABSF(nn.Module):
    def __init__(self, hidden):
        super().__init__()
        self.hidden = hidden
        self.conv1 = nn.Conv1d(self.hidden, self.hidden//2, 1, 1, bias=True)
        self.conv2 = nn.Conv1d(self.hidden, self.hidden//2, 1, 1, bias=True)
        self.conv3 = nn.Conv1d(self.hidden//2, self.hidden, 1, 1, bias=True)
        self.sigmoid = nn.Sigmoid()

    def forward(self, E_i, D_j):
        '''
        :param E_i: i-th Encoder feature with shape B*C*L
        :param D_j: (i+1)-th Decoder feature with shape B*C*L
        :return: Mask, final feature Xi
        '''

        B_i = self.sigmoid(self.conv1(E_i) + self.conv2(D_j))
        A_i = self.sigmoid(self.conv3(B_i))  # Mask
        X_i = D_j + A_i * E_i
        return A_i, X_i

class Channel_Processing(nn.Module):
    def __init__(self, hidden, r):
        super().__init__()
        self.hidden = hidden
        self.r = r
        self.squeeze_conv = nn.Conv1d(self.hidden, self.hidden//self.r, 1, 1)
        self.excite_conv = nn.Conv1d(self.hidden//self.r, self.hidden, 1, 1)
        self.relu=nn.PReLU(self.hidden//self.r)
        self.sigmoid=nn.Sigmoid()

    def forward(self, X):
        '''
        :param X: input feature with shape B*C*L
        :return: feature of channel attention X_C
        '''

        b, c, l = X.size()
        GAP = nn.AvgPool1d(l)
        X_c = GAP(X)  # b c 1

        X_B = self.relu(self.squeeze_conv(X_c))  # b c//r 1
        W_C = self.sigmoid(self.excite_conv(X_B)) # b c 1
        X_C = X * W_C   # b c l
        return X_C

class Sequence_Processing(nn.Module):
    def __init__(self, hidden):
        super().__init__()
        self.hidden = hidden
        self.conv = nn.Conv1d(self.hidden, 1, 1, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, X):
        '''
        :param X: input feature with shape B*C*L
        :return: feature of sequence attention X_L
        '''
        W_L = self.sigmoid(self.conv(X))  # b 1 l
        X_L = X * W_L  # b c l
        return X_L

class CSAtt(nn.Module):
    def __init__(self, hidden, r):
        super().__init__()
        self.hidden = hidden
        self.r = r
        self.c_path = Channel_Processing(self.hidden, self.r)
        self.s_path = Sequence_Processing(self.hidden)

    def forward(self, X):
        '''
        :param X: input feature with shape B*C*L
        :return: final feature X_CSAtt
        '''
        X_CSAtt = self.c_path(X) + self.s_path(X)
        return X_CSAtt


if __name__=='__main__':
    # test ABSF
    b, c, l = 64, 768, 500
    E_i = np.random.random((b, c, l))
    E_i = torch.FloatTensor(E_i)
    D_j = np.random.random((b, c, l))
    D_j = torch.FloatTensor(D_j)
    absf = ABSF(c)
    Mask, X_i = absf(E_i, D_j)

    # test CSAtt
    X = np.random.random((b, c, l))
    X = torch.FloatTensor(X)
    csatt = CSAtt(c, 2)
    X_CSAtt = csatt(X)

