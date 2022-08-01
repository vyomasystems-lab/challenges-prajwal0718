def RippleCarryAdder_4_bits(self, x_array, y_array, s_array ):
    # internal wires
    c0 = self.Wire()
    c1 = self.Wire()
    c2 = self.Wire()
    c3 = self.Wire()

    self.HalfAdder(x_array[0], y_array[0], s_array[0], c0)
    self.FullAdder(x_array[1], y_array[1], c0, s_array[1], c1)
    self.FullAdder(x_array[2], y_array[2], c1, s_array[2], c2)
    self.FullAdder(x_array[3], y_array[3], c2, s_array[3], c3)
   

    return 'ok'

def RippleCarryAdder(self, x_arr, y_arr, s_arr):
    # handle first bit manually
    carry_out = self.Wire()
    self.HalfAdder(x_array[0], y_array[0], s_array[0], carry_out)

    # handle all middle bits with a loop
    for x, y, s in zip(x_arr[1:-1], y_arr[1:-1], s_arr[1:-2]):
        carry_in = carry_out
        carry_out = self.Wire()
        self.FullAdder(x, y, carry_in, s, carry_out)

    # handle last bit manually too
    self.FullAdder(x_array[-1], y_array[-1], carry_out, s_array[-2], s_array[-1])

    return 'ok'
  
