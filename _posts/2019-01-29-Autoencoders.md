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

As seen in the above structure, autoencoders have the same input and output size. Ultimately we want the output to be the same as the input. We penalize the difference of the input $$x$$ and the output $$y$$.

We can formulate the simplist autoencoder (with a single fully connected layer at each side) as follows:

$$x, y \in [0,1]^d$$

$$z = f_\theta(x) = \text{sigmoid}(Wx+b) ~~~ (\theta = \{W, b\})$$

$$y = g_{\theta^\prime}(z) = \text{sigmoid}(W^\prime z+b^\prime) ~~~ (\theta = \{W^\prime, b^\prime\})$$

Since we want $$x=y$$, we obtain the following optimization problem:

$$\theta^*, \theta^{\prime *} = \underset{\theta, \theta^\prime}{\text{argmin}} \frac{1}{N} \sum_{i=1}^N l(x^{(i)}, y^{(i)})$$

The $$l(x,y)$$ is the loss function, which calculates the difference between $$x$$ and $$y$$. We can use square error or cross-entropy, which are written as follows:

$$l(x, y) = \Vert x-y \Vert^2$$

$$l(x, y) = - \sum_{k=1}^d [x_k \log(y_k) + (1-x_k)\log(1-y_k)]$$

We will use cross-entropy error, which we will specially denote as $$l(x, y) = L_H(x, y)$$.

## Statistical viewpoint

We can view this loss function in terms of expectation:

$$\theta^*, \theta^{\prime *} = \underset{\theta, \theta^\prime}{\text{argmin}} \mathbb{E}_{q^o(X)}[L_H(X, g_{\theta^\prime}(f_\theta(X)))]$$

where $$q^o(X)$$ denotes the empirical distribution associated with our $$N$$ training examples.

# Denoising Autoencoders(DAE)
## Structure
