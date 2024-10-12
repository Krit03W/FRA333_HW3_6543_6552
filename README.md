# FRA333 Homework Assignment 3: Static Force

วิธีใช้

Run FRA333_HW3_6543_6552.py (ไฟล์นี้จะเก็บ Function สำหรับแก้ปัญหาข้อ 1 2 3)
```bash
python3 .\FRA333_HW3_6543_6552.py
```
Run testfunction.py (ไฟล์นี้จะเก็บ Function สำหรับตรวจคำตอบข้อ 1 2 3)
```bash
python3 .\testfunction.py
```
Run testScript.py (ไฟล์นี้จะเป็นการทดสอบ Function สำหรับการแก้ปัญหาและ Function สำหรับตรวจคำตอบ และแสดงผลความถูกต้อง)
```bash
python3 .\testScript.py
```

วิธีการทำงาน

![image](https://github.com/user-attachments/assets/e0c4cead-d46d-43dc-baa2-93bc8ba72a08)

1.คำถามข้อที่ 1

เขียนฟังก์ชั่นในการหา Jacobian ของหุ่นยนต์ตัวนี้

Jacobian เมทริกซ์ทั้งหมดประกอบด้วย:

![image](https://github.com/user-attachments/assets/3e547943-04d7-482d-9176-fd8ae1bb783b)

𝐽𝑣 คือ Jacobian เชิงเส้น

𝐽𝑤 คือ Jacobian เชิงมุม

สูตรที่ใช้ในการคำนวณคือ

![image](https://github.com/user-attachments/assets/d1bf1b5c-be44-40f6-b1cf-61905f77eba0)

![image](https://github.com/user-attachments/assets/3476f2f5-f1c7-4026-8ee3-ae65d936f1eb)

การคำนวณสำหรับหุ่นยนต์ RRR

![image](https://github.com/user-attachments/assets/5ccfbd6b-305a-4fd5-af6c-a37545ecc3d2)

```python
def endEffectorJacobianHW3(q: list[float]) -> list[float]:
    # ดึงเมทริกซ์การแปลง (R, R_e) และจุดตำแหน่ง (P, p_e) จากฟังก์ชัน Forward Kinematics
    R, P, R_e, p_e = FKHW3(q)

    # สร้างเมทริกซ์ 3x3 สำหรับ Jacobian ของความเร็วเชิงเส้น (J_v) และความเร็วเชิงมุม (J_w)
    J_v = np.zeros((3, 3))  # J_v จะเก็บความเร็วเชิงเส้น (linear velocity)
    J_w = np.zeros((3, 3))  # J_w จะเก็บความเร็วเชิงมุม (angular velocity)

    # สร้างเวกเตอร์แกน z ในเฟรมฐาน (Base frame) ซึ่งข้อต่อหมุนรอบแกน z ในเฟรมฐานคือ [0, 0, 1]
    z_0 = np.array([0, 0, 1])

    # วนลูปสำหรับข้อต่อแต่ละข้อ (มี 3 ข้อ) เพื่อคำนวณค่า Jacobian
    for i in range(3):
        # คำนวณแกน z_i ของข้อต่อที่ i ในเฟรมฐาน โดยใช้เมทริกซ์การหมุน R ที่ได้จาก FK
        # โดยใช้การคูณเมทริกซ์หมุน R ของข้อต่อ i กับแกน z_0 เพื่อหาทิศทางของแกนหมุนในระบบพิกัดฐาน
        z_i = (R[:, :, i] @ z_0)  

        # คำนวณ Jacobian ของความเร็วเชิงเส้น J_v สำหรับข้อต่อที่ i
        # โดยใช้ cross product ระหว่างแกนหมุน z_i และตำแหน่งของ end-effector ลบด้วยตำแหน่งของข้อต่อที่ i
        J_v[:, i] = np.cross(z_i, p_e - P[:, i])

        # คำนวณ Jacobian ของความเร็วเชิงมุม J_w สำหรับข้อต่อที่ i
        # โดยค่า J_w จะเป็นทิศทางของแกนหมุน z_i เอง (เพราะเป็นข้อต่อหมุน revolute joint)
        J_w[:, i] = z_i

    # นำ Jacobian ของความเร็วเชิงเส้น (J_v) และความเร็วเชิงมุม (J_w) มาต่อกันในแนวตั้ง
    # โดยได้เป็นเมทริกซ์ 6x3 ซึ่งเก็บข้อมูลของทั้งความเร็วเชิงเส้นและเชิงมุม
    J_e = np.vstack((J_v, J_w))

    # ส่งคืนค่า Jacobian J_e ซึ่งเป็นเมทริกซ์ขนาด 6x3 (ในรูปแบบลิสต์ของ float)
    return J_e
```
```
Input q : ค่ามุมของข้อต่อ 1 2 3
Output J_e : ค่า Jacobian ของหุ่นยนต์
```





