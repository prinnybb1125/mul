class Sigmoid:
  def __init__(self):
    self.out = None
  def forward(self, x):
    self.out = 1 / (1 + np.exp(-x))
    return self.out

    return np.outer
  def backward(self, dout):
    dx = dout * (1.0 - self.out) * self.out
    return dx