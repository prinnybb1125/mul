class MulLayer:
  def__init__self:
    self.x = Nono
    self.y = None

  def forward(self, x, y):
    self.x = x
    self.y = y

    return out

  def backward(self, dout):
    dx = dout * self.y
    dy = dout * self.x

    return dx, dy