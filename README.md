# การคำนวณ Jacobian สำหรับหุ่นยนต์ RRR

### คำอธิบาย:
โปรเจคนี้ออกแบบมาเพื่อคำนวณเมทริกซ์ Jacobian ของหุ่นยนต์ RRR (Revolute-Revolute-Revolute) โดยมีสองฟังก์ชันที่สามารถใช้ในการคำนวณ Jacobian:
1. `endEffectorJacobianHW3(q)` - ฟังก์ชันที่เขียนขึ้นเองสำหรับการคำนวณ Jacobian โดยใช้การคำนวณ Forward Kinematics
2. `CheckJacobian(q)` - ฟังก์ชันมาตรฐานจากไลบรารี `roboticstoolbox` ที่ใช้ Denavit-Hartenberg parameters ในการคำนวณ Jacobian

### โครงสร้างของไฟล์:
- **`HW3_utils.py`**: มีฟังก์ชัน `FKHW3` สำหรับการคำนวณ Forward Kinematics
- **`FRA333_HW3_43_52.py`**: มีฟังก์ชันที่เขียนขึ้นเองสำหรับการคำนวณ Jacobian ชื่อว่า `endEffectorJacobianHW3`
- **`testfunction.py`**: มีฟังก์ชันมาตรฐานในการคำนวณ Jacobian ชื่อว่า `CheckJacobian`

### ฟังก์ชันที่ใช้:

#### 1. `endEffectorJacobianHW3(q: list[float]) -> list[float]`
- **Input**: 
  - `q`: ลิสต์ที่เก็บมุมของข้อต่อทั้งสาม [q1, q2, q3] ซึ่งแสดงถึงการกำหนดค่าของหุ่นยนต์
- **Output**: 
  - คืนค่า Jacobian matrix `J_e` ซึ่งเป็นเมทริกซ์ขนาด 6x3 ที่มีส่วนประกอบทั้งความเร็วเชิงเส้นและความเร็วเชิงมุมของหุ่นยนต์
  
- **วิธีการทำงาน**:
  - ฟังก์ชันจะคำนวณการเคลื่อนที่ของหุ่นยนต์ (Forward Kinematics) ตามมุมข้อต่อที่กำหนด
  - จากนั้นจะคำนวณ Jacobian โดยใช้วิธีการ Cross Product เพื่อหาความสัมพันธ์ระหว่างการหมุนของข้อต่อและการเคลื่อนที่ของ end-effector
  - Jacobian สุดท้ายจะรวมกันระหว่างความเร็วเชิงเส้นและความเร็วเชิงมุม

#### 2. `CheckJacobian(q: list[float]) -> np.ndarray`
- **ฟังก์ชัน**: 
  - ฟังก์ชันจากไลบรารี `roboticstoolbox` ใช้ในการคำนวณ Jacobian โดยอิงจาก Denavit-Hartenberg parameters ของหุ่นยนต์

### การติดตั้ง:
เพื่อใช้งานโปรเจคนี้ คุณต้องติดตั้งไลบรารีที่จำเป็น เช่น `numpy`, `roboticstoolbox`, และ `spatialmath`

```bash
pip install numpy roboticstoolbox-python spatialmath-python
