

import cocotb
from cocotb.triggers import ReadOnly, ReadWrite, RisingEdge, Timer
from cocotb.clock import Clock

def print_vals(dut, msg=""):
    print(f"{msg} i={dut.i.value}, o={dut.o.value}, o_reg={dut.o_reg.value}")

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 10, units="us") 
    cocotb.fork(clock.start())
    await Timer(1)

    dut.i.setimmediatevalue(0)
    print_vals(dut, "A:")
    await ReadWrite()
    print_vals(dut, "B:")
    dut.i.value = 1
    await ReadWrite()
    print_vals(dut, "C:")
    await ReadOnly()
    print_vals(dut, "D:")
    await Timer(1)
    print_vals(dut, "E:")
    await RisingEdge(dut.clk)
    print_vals(dut, "F:")
    await ReadOnly()
    print_vals(dut, "G:")

