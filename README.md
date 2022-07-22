# challenges-Tarak79
challenges-Tarak79 created by GitHub Classroom

MUX DESIGN VERIFICATION

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.
The Screenshot:
![image](https://user-images.githubusercontent.com/65438040/180433889-84662841-638d-45c6-9490-9fc2a4f6b2e4.png)

Verification Environment

The CoCoTb based Python test is developed as below. The test drives inputs to the Design Under Test ,Since the input is of 2 bits i have taken a random integer to be generated in range(00,01,10,11) and select line value varies for different test cases. The format i used is shown below.

 
    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp0.value = random.randint(0,3)
    dut.sel.value = 0

The assert statement is used for comparing the mux output to the expected value.
The error is as follows:
![image](https://user-images.githubusercontent.com/65438040/180445783-2409c60e-a5d6-49a6-8432-26c99966a2a3.png)


TEST SCENARIOS:

The output has been passed for all the cases except cases 12 and 13. 

for these cases there is a assertion that has been shown above in the screenshot and in remaining all the cases the output satisfies the expected output of the design,so
Output mismatches for the above inputs proving that there is a design bug.

Design Bug:

So in the dsign if we see the mux verilog code , in the case statement there is same case has been written for case 12 and 13, so that might the reason for the bug and this has been shown as in the screenshot below:

![image](https://user-images.githubusercontent.com/65438040/180446493-09e6add2-0742-4812-8562-6bed44086b78.png)

so for this design , same assignment for 12,13 cases has been written so that's the bug!

Design Fix

After fixing the design the outputs are found to be in order and therefore the design got fixed!

![image](https://user-images.githubusercontent.com/65438040/180448572-917bb659-0a4b-48cf-9365-bb92d37f1eb6.png)

The updated design is provided by mux_fixed.v

Verification Strategy

For the verification of this design , i have created 30 test cases in which each case will check for all the possible two inputs and check the design so by this all the bugs are found and have been fixed!

Is Verification Complete?

Yes! verification is completed.
