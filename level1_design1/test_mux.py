# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux_0(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp0.value = random.randint(0,3)
    dut.sel.value = 0
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp0.value, f'The Result of Mux is not correct: {dut.inp0.value}!={dut.out.value}'