---
title: 离散傅里叶变换(DFT)
date: 2017-05-25 17:46:15
tags:
  - MIR
categories:
  - Audio Signal Processing
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

对于音频信号处理而言，`离散傅里叶变化(DFT)`是最最常用的函数工具。它将信号的时域采样变换为其`离散时间傅里叶变化(DTFT)`的频域采样（在\\([0,2\pi]\\)之间进行均匀采样）,最后得到数字信号在区间\\([0,(k-1)f_s/N]\\)内的离散频谱值。

在形式上，变换两端（时域和频域上）的序列是有限长的，而实际上这两组序列都应当被认为是离散周期信号的主值序列。即使对有限长的离散信号作DFT，也应当将其看作其周期延拓的变换。

DFT的变化等式为：  
$$X[k]=  \sum_{n=0}^{N-1}{x[n]e^{−j2{\pi}kn/N}}   (k=0,...,N−1)$$
<!--More-->

```python
# DFT的Python实现
import numpy as np

def DFT(x):
    """
    Input:
        x (numpy array) = input time sequence of N samples
    Output:
        X (numpy array) = The N point DFT of the input sequence x
    """

    N = len(x)
    n = np.arange(N)
    X = np.array([])

    for k in range(N):
        Xk = sum(x*np.conjugate(np.exp(1j*2*np.pi*k/N * n)))
        X = np.append(X, Xk)

    return X
```

DFT的逆变化：
   
$$x[n]=  \frac{1}{N}\sum_{k=0}^{N-1}{X[k]e^{j2{\pi}nk/N}}   (n=0,...,N−1)$$

```python
# IDFT的Python实现
import numpy as np

def IDFT(x):
     """
    Input:
        X (numpy array) = frequency spectrum (length N)
    Output:
        The function should return a numpy array of length N 
        x (numpy array) = The N point IDFT of the frequency spectrum X
    """
    
    x = np.array([])
    N = len(X)

    for n in range(N):
        xn = 1.0/N * sum(X*np.exp(1j*2*np.pi*n/N * np.arange(N)))
        x = np.append(x,xn)
        
    return x
```

## DFT的几条重要性质
备注：\\(x[n]\\)是时域信号，\\(X[k]\\)是相应的频域信号；\\(mX=20\log_{10}(|X|)\\)是幅度谱(dB)，\\(pX=\angle{X} \\)是相位谱。

P1. 线性性质(Linearity)  
$$ax_1[n]+bx_2[n] \Leftrightarrow aX_1[k]+bX_2[k] $$

P2. 时移性和频移性(Shift) ：移动之后幅度谱不变相位谱改变。  
$$x[n-n_0] \Leftrightarrow e^{-j2{\pi}kn_0/N}X[k] $$

P3. 对称性(Symmetry)：  
$$\begin{align} x[n]real \Leftrightarrow \mathfrak{R}(X[k])even{\quad}and{\quad}\mathfrak{I}(X[k])odd \newline \Leftrightarrow |X[k]|even \quad and \quad \angle{X[k]}odd \quad \end{align}$$

$$\begin{align} x[n]real\&even \Leftrightarrow \mathfrak{R}(X[k])even{\quad}and{\quad}\mathfrak{I}(X[k])=0 \newline \Leftrightarrow |X[k]|even \quad and \quad \angle{X[k]}=n\pi \quad \end{align}$$

P4. 卷积定理(Convolution)  
$$x_1[n]\otimes x_2[n] \Leftrightarrow X_1[K]X_2[K]$$

## DFT中的处理方法
* Energy conservation  
* Phase unwrapping* Zero padding* Fast Fourier Transform (FFT) 
* FFT and zero-phase windowing 
* Analysis/synthesis
