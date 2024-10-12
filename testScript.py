# file สำหรับตรวจคำตอบ
# ในกรณีที่มีการสร้าง function อื่0น ๆ ให้ระบุว่า input-output คืออะไรด้วย
"""
ชื่อ_รหัส
1.พสุรัตน์ พิบูลย์จิรชาติ 65340500043
2.วิจักขณ์ มะโนปราง  65340500052
"""
# ===========================================<ตรวจคำตอบข้อ 1>====================================================#
print('Test_No.1')
from testfunction import CheckJacobian
from FRA333_HW3_43_52 import endEffectorJacobianHW3
import numpy as np

# ตั้งจำนวนการทดสอบเป็น 5 รอบ
num_tests = 5  # สามารถเปลี่ยนตัวเลขได้ถ้าอยากทดสอบมากกว่านี้

# ลูปเพื่อทดสอบ num_tests รอบ
for i in range(num_tests):
    # สุ่มค่ามุมข้อต่อ q ในช่วง -π ถึง π สำหรับข้อต่อ 3 ตัว
    q1_test = np.random.uniform(low=-np.pi, high=np.pi, size=3)  # สุ่มมุม q แบบ random

    # คำนวณ Jacobian ของแต่ละฟังก์ชัน (ทั้ง endEffectorJacobianHW3 และ CheckJacobian)
    jacobian_hw3 = endEffectorJacobianHW3(q1_test)
    jacobian_check = CheckJacobian(q1_test)

    # พิมพ์ผลลัพธ์
    print(f"Test case {i+1}: q = {q1_test}")  # พิมพ์ค่ามุม q ที่สุ่มได้
    print(f"Jacobian จาก endEffectorJacobianHW3:\n{jacobian_hw3}")  # พิมพ์ Jacobian จากฟังก์ชันแรก
    print(f"Jacobian จาก CheckJacobian:\n{jacobian_check}")  # พิมพ์ Jacobian จากฟังก์ชันที่สอง

    # เปรียบเทียบผลลัพธ์ว่าใกล้เคียงกันมากพอมั้ย (ใช้ np.allclose)
    if np.allclose(jacobian_hw3, jacobian_check, atol=1e-6):
        print("Jacobian ใกล้เคียงกันมาก!")  # ถ้าค่าใกล้เคียงพอ
    else:
        print("Jacobian ไม่ตรงกัน!")  # ถ้าค่าไม่ใกล้เคียงกัน

    print("\n")  # แสดงเส้นแบ่งระหว่างแต่ละรอบการทดสอบ
# ตั้งจำนวนการทดสอบเป็น 1,000 รอบ
num_tests = 1000
count_close = 0  # ตัวแปรเก็บจำนวนครั้งที่ค่า Jacobian ใกล้เคียงกัน

# ลูปเพื่อทดสอบ num_tests รอบ
for i in range(num_tests):
    # สุ่มค่ามุมข้อต่อ q ในช่วง -π ถึง π สำหรับข้อต่อ 3 ตัว
    q1_test = np.random.uniform(low=-np.pi, high=np.pi, size=3)  # สุ่มมุม q แบบ random

    # คำนวณ Jacobian ของแต่ละฟังก์ชัน (ทั้ง endEffectorJacobianHW3 และ CheckJacobian)
    jacobian_hw3 = endEffectorJacobianHW3(q1_test)
    jacobian_check = CheckJacobian(q1_test)

    # เปรียบเทียบผลลัพธ์ว่าใกล้เคียงกันมากพอมั้ย (ใช้ np.allclose)
    if np.allclose(jacobian_hw3, jacobian_check, atol=1e-6):
        count_close += 1  # นับจำนวนครั้งที่ Jacobian ใกล้เคียงกัน

# แสดงผลลัพธ์ว่ามีค่าใกล้เคียงกันกี่เคส
print('----------------------------------------')
print(f"ทดสอบทั้งหมด {num_tests} เคส")
print(f"ผลลัพธ์ตรงกันทั้งหมด {count_close} เคส")
print(f"ผลลัพธ์ไม่ตรงกันทั้งหมด {num_tests-count_close} เคส")
print('----------------------------------------')
print('\n')
# ===========================================<ตรวจคำตอบข้อ 2>====================================================#
print('Test_No.2')
import numpy as np
from testfunction import CheckSingularity
from FRA333_HW3_43_52 import checkSingularityHW3

# สุ่มค่า q แบบสุ่มในช่วง [-pi, pi] สำหรับแต่ละข้อต่อ
def random_test_case():
    return np.random.uniform(-np.pi, np.pi, 3).tolist()

# ทดสอบด้วยการสุ่มค่า q และตรวจสอบว่าให้ผลลัพธ์ Singularity ตรงกันหรือไม่
for i in range(5):  # ทำการทดสอบ 5 ครั้ง
    q2_test = random_test_case()  # สุ่มค่า q

    # เรียกใช้ฟังก์ชัน checkSingularityHW3 และ CheckSingularity
    result_hw3 = checkSingularityHW3(q2_test)
    result_dh = CheckSingularity(q2_test)

    # พิมพ์ผลลัพธ์ออกมาเพื่อเปรียบเทียบ
    print(f"Test case {i+1}: q = {q2_test}")
    print(f"HW3 Singularity: {result_hw3}")
    print(f"DH Singularity: {result_dh}")

    # ตรวจสอบว่าผลลัพธ์ตรงกันหรือไม่
    if result_hw3 == result_dh:
        print(f"Test {i+1}: Results match!\n")
    else:
        print(f"Test {i+1}: Results do NOT match!\n")
    
q2_Singularity = [-2.2827749666024557, 1.6631974330270758, 2.9483149284442174]
# เรียกใช้ฟังก์ชัน checkSingularityHW3 และ CheckSingularity
result_hw3 = checkSingularityHW3(q2_Singularity)
result_dh = CheckSingularity(q2_Singularity)

# พิมพ์ผลลัพธ์ออกมาเพื่อเปรียบเทียบ
print(f"Test case Singularity: q = {q2_Singularity}")
print(f"HW3 Singularity: {result_hw3}")
print(f"DH Singularity: {result_dh}")

# ตรวจสอบว่าผลลัพธ์ตรงกันหรือไม่
if result_hw3 == result_dh:
    print(f"Test Singularity: Results match!\n")
else:
    print(f"Test Singularity: Results do NOT match!\n")
print('\n')
# สุ่มค่า q แบบสุ่มในช่วง [-pi, pi] สำหรับแต่ละข้อต่อ
def random_test_case():
    return np.random.uniform(-np.pi, np.pi, 3).tolist()

# ตั้งจำนวนการทดสอบ
num_tests = 1000  # จำนวนการทดสอบ 1,000 ครั้ง

# ตัวนับสำหรับติดตามจำนวนครั้งที่ผลลัพธ์ตรงกันและไม่ตรงกัน
count_match = 0
count_mismatch = 0

# วนลูปเพื่อทดสอบ
for i in range(num_tests):
    q2_test = random_test_case()  # สุ่มค่า q

    # เรียกใช้ฟังก์ชัน checkSingularityHW3 และ CheckSingularity
    result_hw3 = checkSingularityHW3(q2_test)
    result_dh = CheckSingularity(q2_test)

    # ตรวจสอบว่าผลลัพธ์ตรงกันหรือไม่
    if result_hw3 == result_dh:
        count_match += 1  # ถ้าผลลัพธ์ตรงกันให้เพิ่มตัวนับ
    else:
        count_mismatch += 1  # ถ้าผลลัพธ์ไม่ตรงกันให้เพิ่มตัวนับ

# แสดงผลลัพธ์สรุป
print('----------------------------------------')
print(f"ทดสอบทั้งหมด {num_tests} เคส")
print(f"ผลลัพธ์ตรงกันทั้งหมด {count_match} เคส")
print(f"ผลลัพธ์ไม่ตรงกันทั้งหมด {count_mismatch} เคส")
print('----------------------------------------')
# ==============================================================================================================#

# ===========================================<ตรวจคำตอบข้อ 3>====================================================#
print('\nTest_No.3')
import numpy as np
from FRA333_HW3_43_52 import computeEffortHW3
from testfunction import CheckEffort

# วนลูป 10 รอบ
for i in range(10):
    # กำหนดค่าของ q3_test และ w_example แบบสุ่มภายในช่วง [-pi, pi] สำหรับ q และ [-10, 10] สำหรับ w
    q3_test = np.random.uniform(-np.pi, np.pi, 3).tolist()  # สุ่ม q3_test สามค่าในช่วง [-pi, pi]
    w_example = np.random.uniform(-10, 10, 6).tolist()  # สุ่ม w_example หกค่าในช่วง [-10, 10]

    # คำนวณค่า torque จากทั้งสองฟังก์ชัน
    effort_hw3 = computeEffortHW3(q3_test, w_example)
    effort_check = CheckEffort(q3_test, w_example)

    # พิมพ์ผลลัพธ์ของแต่ละรอบ
    print(f"รอบที่ {i+1}")
    print("computeEffortHW3:", effort_hw3)
    print("CheckEffort:", effort_check)

    # ตรวจสอบว่าค่าทั้งสองใกล้เคียงกันหรือไม่ ด้วย atol = 1e-6
    if np.allclose(effort_hw3, effort_check, atol=1e-6):
        print("ผลลัพธ์ใกล้เคียงกัน\n")
    else:
        print("ผลลัพธ์ไม่ใกล้เคียงกัน\n")
    
# ตั้งจำนวนการทดสอบ
num_tests = 1000  # จำนวนการทดสอบ 1,000 ครั้ง

# ตัวนับสำหรับติดตามจำนวนครั้งที่ผลลัพธ์ใกล้เคียงกันและไม่ใกล้เคียงกัน
count_close = 0
count_not_close = 0

# วนลูปเพื่อทดสอบ num_tests รอบ
for i in range(num_tests):
    # กำหนดค่าของ q3_test และ w_example แบบสุ่มภายในช่วง [-pi, pi] สำหรับ q และ [-10, 10] สำหรับ w
    q3_test = np.random.uniform(-np.pi, np.pi, 3).tolist()  # สุ่ม q3_test สามค่าในช่วง [-pi, pi]
    w_example = np.random.uniform(-10, 10, 6).tolist()  # สุ่ม w_example หกค่าในช่วง [-10, 10]

    # คำนวณค่า torque จากทั้งสองฟังก์ชัน
    effort_hw3 = computeEffortHW3(q3_test, w_example)
    effort_check = CheckEffort(q3_test, w_example)

    # ตรวจสอบว่าค่าทั้งสองใกล้เคียงกันหรือไม่ ด้วย atol = 1e-6
    if np.allclose(effort_hw3, effort_check, atol=1e-6):
        count_close += 1  # ถ้าค่าใกล้เคียงกันเพิ่มตัวนับ
    else:
        count_not_close += 1  # ถ้าค่าไม่ใกล้เคียงกันเพิ่มตัวนับ

# แสดงผลลัพธ์สรุป
print('----------------------------------------')
print(f"ทดสอบทั้งหมด {num_tests} เคส")
print(f"ผลลัพธ์ตรงกันทั้งหมด {count_close} เคส")
print(f"ผลลัพธ์ไม่ตรงกันทั้งหมด {count_not_close} เคส")
print('----------------------------------------')
# ==============================================================================================================#
