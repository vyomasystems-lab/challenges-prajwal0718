# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
print('Prajwal D Nayak')
@cocotb.test()
async def test_mux(dut):
    dut.sel.value =5'b00000;
    
    dut.sel.value = 5'b00001;

    dut.sel.value = 5'b00010;
    
    dut.sel.value = 5'b10010;
   
     dut.sel.value = 5'b10011;
    
     dut.sel.value = 5'b10110;
   

    assert dut.out.value == 5'b11111 , Mux result takes default value;


    cocotb.log.info( dut.sel.value =5'b00000;
    await Timer(2,units='ns')
    dut.sel.value = 5'b00001;
    await Timer(2,units='ns')
    dut.sel.value = 5'b00010;
    await Timer(2,units='ns')
    dut.sel.value = 5'b10010;
    await Timer(2,units='ns')
     dut.sel.value = 5'b10011;
    await Timer(2,units='ns')
     dut.sel.value = 5'b10110;
    await Timer(2,units='ns'))
