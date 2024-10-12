# FRA333 Homework Assignment 3: Static Force

**Library ที่จำเป็นต้องติดตั้ง**
- **roboticstoolbox-python**
- **numpy**
- **spatialmath**
- **math**


**การใช้งาน**

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

**วิธีการทำงาน**
![image](https://github.com/user-attachments/assets/933ca00c-a2ce-4042-8c10-6528eba6bdfd)

DH Parameter :

<p align="center">
  <img src="https://github.com/user-attachments/assets/9e0e980a-5eff-4d25-8fbf-d76c129f18d6" alt="image" />
</p>

 # คำถามข้อที่ 1 : เขียนฟังก์ชั่นในการหา Jacobian ของหุ่นยนต์

Jacobian เมทริกซ์ทั้งหมดประกอบด้วย :

<p align="center">
  <img src="https://github.com/user-attachments/assets/cbcdb180-81dc-40f6-aacc-cf1719167d0e" alt="image" />
</p>

โดยที่ 𝐽𝑣 คือ Jacobian เชิงเส้น และ 𝐽𝑤 คือ Jacobian เชิงมุม

สูตรการคำนวณ :

<p align="center">
  <img src="https://github.com/user-attachments/assets/d1bf1b5c-be44-40f6-b1cf-61905f77eba0" alt="image" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/3476f2f5-f1c7-4026-8ee3-ae65d936f1eb" alt="image" />
</p>

การคำนวณสำหรับหุ่นยนต์ RRR :

<p align="center">
  <img src="https://github.com/user-attachments/assets/5ccfbd6b-305a-4fd5-af6c-a37545ecc3d2" alt="image" />
</p>

ฟังก์ชั่นในการหา Jacobian ของหุ่นยนต์ :
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

**วิธีการเช็คคำตอบ**

หา Jacobian จาก robotics-toolbox จาก DH Parameter ของหุ่นยนต์ จากนั้นนำมาเปรียบเทียบกับค่า Jacobian จากฟังก์ชันที่หาได้

**ผลลัพธ์ของการทดสอบ**

<p align="center">
  <img src="https://github.com/user-attachments/assets/77264948-06fc-4f3b-ae20-2903cfbcfd69" alt="image" />
</p>

   จากผลการทดสอบจะเห็นได้ว่า Jacobian Matrix ที่ได้จากการทำ DH Parameter มีค่าใกล้เคียงกับ Jacobian Matrix ที่หาได้จากฟังก์ชันข้างต้น จึงสามารถสรุปได้ว่า Jacobian Matrix ที่สามารถหาได้เป็นค่าที่ถูกต้อง 

 # คำถามข้อที่ 2 : เขียนฟังก์ชั่นในการหาสภาวะ Singularity 

 ใช้ Determinant: สำหรับระบบที่มี 3DOF แบบข้อต่อหมุน สามารถตรวจสอบ Singularity ได้โดยการตรวจสอบว่า Determinant ของ Jacobian เชิงเส้น 𝐽𝑣 มีค่าเป็น 0 หรือไม่:

<p align="center">
  <img src="https://github.com/user-attachments/assets/82866b94-f5ac-4ee6-8d72-316492efc798" alt="image" />
</p>

หาก det(𝐽𝑣)=0 หมายความว่าหุ่นยนต์ไม่สามารถสร้างความเร็วเชิงเส้นที่ปลายแขนหุ่นยนต์ (end-effector) ได้ครบทุกทิศทาง นั่นคือหุ่นยนต์อยู่ในสภาวะ Singularity

โดยในที่นี้กำหนดให้หุ่นยนต์อยู่ในสภาวะ Sigularity ก็ต่อเมื่อ

<p align="center">
  <img src="https://github.com/user-attachments/assets/1d1badf3-34b3-49bf-ac20-972e3dfa0aa3" alt="image" />
</p>

โดยที่ค่า ε มีค่า 0.001

ฟังก์ชั่นในการหาสภาวะ Singularity ของหุ่นยนต์ :

```python
def checkSingularityHW3(q: list[float]) -> int:
    # กำหนดค่า threshold ที่ใช้บอกว่า determinant ใกล้ศูนย์แค่ไหนถึงจะถือว่ามี Singularity ตามโจทย์กำหนด
    threshold = 0.001

    # เรียกฟังก์ชัน endEffectorJacobianHW3 เพื่อคำนวณ Jacobian matrix ของหุ่นยนต์ที่ตำแหน่ง q
    J_e = endEffectorJacobianHW3(q)

    # ดึงส่วนของเมทริกซ์ Jacobian ที่เกี่ยวกับตำแหน่ง (ส่วนความเร็วเชิงเส้น 3x3)
    J_v = J_e[:3, :3]

    # คำนวณค่า determinant ของเมทริกซ์ J_v ที่ได้ (เพราะถ้า determinant เป็นศูนย์ จะบอกได้ว่ามี Singularity)
    det_J_v = np.linalg.det(J_v)

    # ตรวจสอบว่าค่า determinant น้อยกว่าค่าที่กำหนด(threshold)หรือไม่ ถ้าใช่ แสดงว่ามี Singularity
    if abs(det_J_v) < threshold:
        return 1  # ถ้าใช่, บอกว่าเกิด Singularity
    else:
        return 0  # ถ้าไม่ใช่, ไม่มี Singularity

```

**วิธีการเช็คคำตอบ**

เช็คค่า determinant ด้วยการใช้ robotics-toolbox โดยหากน้อยกว่า threshold แสดงว่าระบบหุ่นยนต์อยู่ในสถานะ Singularity และถ้า determinant มากกว่าหรือเท่ากับ threshold แสดงว่าหุ่นยนต์ไม่อยู่ในสถานะ Singularity

Note: ในโจทย์กำหนด threshold เท่ากับ 0.001

**ผลลัพธ์ของการทดสอบ**

<p align="center">
  <img src="https://github.com/user-attachments/assets/77264948-06fc-4f3b-ae20-2903cfbcfd69](https://github.com/user-attachments/assets/341350b9-7ff7-4383-9c73-550100bb3c29" alt="image" />
</p>

จากผลการทดสอบจะเห็นได้ว่าค่า Singularity จากการทำ DH Parameter และจากฟังก์ชันที่หาได้นั้นมีค่าเท่ากัน จึงสามารถสรุปได้ว่าค่า Singularity ที่หาได้เป็นค่าที่ถูกต้อง

 # คำถามข้อที่ 3 :  เขียนฟังก์ชั่นในการหา effort ของแต่ละข้อต่อเมื่อมี wrench มากระทำ

แรงบิดที่ข้อต่อ (Torque) 𝜏 สามารถคำนวณได้จากสมการ:

<p align="center">
  <img src="https://github.com/user-attachments/assets/244f96de-de5d-4595-b456-3bf940951fd4" alt="image" />
</p>

โดย: 𝜏 คือแรงบิด (Torque) ที่ข้อต่อต่างๆ 𝐽𝑇 คือ Jacobian transpose (เมทริกซ์ Jacobian ที่ทำการ transpose)

𝐹 คือ Wrench ที่ปลายแขนหุ่นยนต์ (Wrench มี 6 องค์ประกอบ: แรงเชิงเส้นในแกน x, y, z และแรงเชิงมุมในแกน x, y, z)

<p align="center">
  <img src="https://github.com/user-attachments/assets/f3b3974e-e4ab-4424-8896-2f0078af9d97" alt="image" />
</p>

ฟังก์ชันในการหาค่า Torque ของหุ่นยนต์ :

```python
def computeEffortHW3(q: list[float], w: list[float]) -> list[float]:
    # แปลงค่า w ที่เป็นลิสต์ให้เป็น numpy array
    wrench = np.array(w)

    # คำนวณ Jacobian matrix โดยใช้ฟังก์ชันที่เราเขียนไว้ก่อนหน้า endEffectorJacobianHW3
    # ฟังก์ชันนี้จะคำนวณเมทริกซ์ J_e ที่แสดงความสัมพันธ์ระหว่างการหมุนของข้อต่อกับการเคลื่อนที่ของ end-effector
    J_e = endEffectorJacobianHW3(q)

    # คำนวณค่าแรงบิด (torque หรือ effort) สำหรับแต่ละข้อต่อโดยใช้สูตร: tau = J^T * wrench
    # J^T คือการ transpose ของ Jacobian (เปลี่ยนแถวเป็นคอลัมน์)
    # wrench คือแรงและโมเมนต์ที่ได้จากเซนเซอร์
    tau = J_e.T @ wrench

    # ส่งคืนค่า torque หรือ effort ที่ได้เป็นลิสต์ของ float
    return tau.tolist()
```

**วิธีการเช็คคำตอบ**

เช็คค่า torque จาก robotics-toolbox และเปรียบเทียบกับฟังก์ชันข้างต้น

**ผลลัพธ์ของการทดสอบ**

<p align="center">
  <img src="https://github.com/user-attachments/assets/cdbbc511-e729-408e-8756-2ea75495b52c" alt="image" />
</p>

จากผลการทดสอบจะเห็นได้ว่าค่า Torque จากการทำ DH Parameter และจากฟังก์ชันที่หาได้นั้นมีค่าเท่ากัน จึงสามารถสรุปได้ว่าค่า Torque ที่หาได้เป็นค่าที่ถูกต้อง



 












