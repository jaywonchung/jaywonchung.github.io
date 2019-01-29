---
title: "Autoencoders"
layout: single
excerpt: "Vanilla autoencoders(AE), denoising autoencoders(DAE), and variational autoencoders(VAE) explained. Referring to the previous post on bayesian statistics may help your understanding."
categories:
  - study
  - machine-learning
---

# Autoencoders(AE)
## Structure
![Autoencoders](/assets/images/posts/2019-01-29-AE.png)
(https://www.slideshare.net/NaverEngineering/ss-96581209)

As seen in the above structure, autoencoders have the same input and output size. Ultimately we want the output to be the same as the input. We penalize the difference of the input $$x$$ and the output $$y$$.

We can formulate the simplest autoencoder (with a single fully connected layer at each side) as follows:

$$x, y \in [0,1]^d$$

$$z = h_\theta(x) = \text{sigmoid}(Wx+b) ~~~ (\theta = \{W, b\})$$

$$y = g_{\theta^\prime}(z) = \text{sigmoid}(W^\prime z+b^\prime) ~~~ (\theta = \{W^\prime, b^\prime\})$$

Since we want $$x=y$$, we obtain the following optimization problem:

$$\theta^*, \theta^{\prime *} = \underset{\theta, \theta^\prime}{\text{argmin}} \frac{1}{N} \sum_{i=1}^N l(x^{(i)}, y^{(i)})$$

The $$l(x,y)$$ is the loss function, which calculates the difference between $$x$$ and $$y$$. We can use square error or cross-entropy, which are written as follows:

$$l(x, y) = \Vert x-y \Vert^2$$

$$l(x, y) = - \sum_{k=1}^d [x_k \log(y_k) + (1-x_k)\log(1-y_k)]$$

We will use cross-entropy error, which we will specially denote as $$l(x, y) = L_H(x, y)$$.

## Statistical viewpoint

We can view this loss function in terms of expectation:

$$\theta^*, \theta^{\prime *} = \underset{\theta, \theta^\prime}{\text{argmin}} \mathbb{E}_{q^0(X)}[L_H(X, g_{\theta^\prime}(h_\theta(X)))]$$

where $$q^0(X)$$ denotes the empirical distribution associated with our $$N$$ training examples.

# Denoising Autoencoders(DAE)
## Structure
![Denoising Autoencoders](/assets/images/posts/2019-01-29-DAE.png)
(https://www.slideshare.net/NaverEngineering/ss-96581209)

With the encoder and decoder formula the same, denoising autoencoders intentionally drop a specific portion of the pixels of the input $$ x $$ to zero, creating $$ \tilde{x} $$. Formally, we are sampling $$ \tilde{x} $$ from a stochastic mapping $$ q_D(\tilde{x}\vert x) $$. The loss is computed between the original $$ x $$ and the output $$ y $$.

In formulating our objective function, we cannot use that of the vanilla autoencoder since now $$ g_{\theta^\prime}(f_\theta(\tilde{x})) $$ is a deterministic function of $$ \tilde{x}  $$, not $$ x $$. Thus we need to take into account the connection between $$ \tilde{x} $$ and $$ x $$, which is $$ q_D(\tilde{x}\vert x) $$. Then our optimization problem can be written and expanded as follows:

$$ \begin{aligned}
  \theta^*,\theta^{\prime *} 
  &= \underset{\theta, \theta^\prime}{\text{argmin}} \mathbb{E}_{q^0(X, \tilde{X})}[L_H(X, g_{\theta^\prime}(f_\theta(\tilde{X})))]\\
  &= \underset{\theta, \theta^\prime}{\text{argmin}} \frac{1}{N} \sum_{x\in D} \mathbb{E}_{q_D(\tilde{x}\vert x)}[L_H(x, g_{\theta^\prime}(f_\theta(\tilde{x})))]\\
  &\approx \underset{\theta, \theta^\prime}{\text{argmin}}\frac{1}{N} \sum_{x\in D} \frac{1}{L} \sum_{i=1}^L L_H(x, g_{\theta^\prime}(f_\theta(\tilde{x}_i)))
\end{aligned} $$

where $$ q^0(X, \tilde{X}) = q^0(X)q_D(\tilde{X}\vert X) $$. Since we cannot compute the expectation in the second line, we approximate it by drawing $$ L $$ samples and computing their mean loss.