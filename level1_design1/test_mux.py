# See LICENSE.vyoma for details
import random
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux_0(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp0.value = random.randint(0,3)
    dut.sel.value = 0
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp0.value, f"The Result of Mux is not correct: {dut.inp0.value}!={dut.out.value}"

@cocotb.test()
async def test_mux_1(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp1.value = random.randint(0,3)
    dut.sel.value = 1
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp1.value, f"The Result of Mux is not correct: {dut.inp1.value}!={dut.out.value}"

@cocotb.test()
async def test_mux_2(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp2.value = random.randint(0,3)
    dut.sel.value = 2
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp2.value, f"The Result of Mux is not correct: {dut.inp2.value}!={dut.out.value}"

@cocotb.test()
async def test_mux_3(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp3.value = random.randint(0,3)
    dut.sel.value = 3
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp3.value, f"The Result of Mux is not correct: {dut.inp3.value}!={dut.out.value}"

@cocotb.test()
async def test_mux_4(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp0.value = random.randint(0,3)
    dut.sel.value = 4
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp4.value, f"The Result of Mux is not correct: {dut.inp4.value}!={dut.out.value}"

@cocotb.test()
async def test_mux_5(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp0.value = random.randint(0,3)
    dut.sel.value = 5
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp5.value, f"The Result of Mux is not correct: {dut.inp5.value}!={dut.out.value}"

@cocotb.test()
async def test_mux_6(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp6.value = random.randint(0,3)
    dut.sel.value = 6
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp6.value, f"The Result of Mux is not correct: {dut.inp6.value}!={dut.out.value}"

@cocotb.test()
async def test_mux_7(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp7.value = random.randint(0,3)
    dut.sel.value = 7
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp7.value, f"The Result of Mux is not correct: {dut.inp7.value}!={dut.out.value}"

@cocotb.test()
async def test_mux_8(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp8.value = random.randint(0,3)
    dut.sel.value = 8
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp8.value, f"The Result of Mux is not correct: {dut.inp8.value}!={dut.out.value}"

@cocotb.test()
async def test_mux_9(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp0.value = random.randint(0,3)
    dut.sel.value = 9
    await Timer(2,units='ns')
    assert dut.out.value==dut.inp9.value, f"The Result of Mux is not correct: {dut.inp9.value}!={dut.out.value}"