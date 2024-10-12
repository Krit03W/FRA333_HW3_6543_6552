# FRA333_HW3_6543_6552
Project Title: Jacobian Computation for RRR Robot
Description:
โปรเจคนี้ใช้สำหรับคำนวณ Jacobian ของหุ่นยนต์แบบ RRR (Revolute-Revolute-Revolute) โดยคำนวณจากค่ามุมข้อต่อ 
𝑞
1
,
𝑞
2
,
𝑞
3
q 
1
​
 ,q 
2
​
 ,q 
3
​
  และใช้ฟังก์ชัน endEffectorJacobianHW3(q) ที่ได้รับการเขียนขึ้นมาเอง พร้อมการเทียบผลลัพธ์กับฟังก์ชัน CheckJacobian ซึ่งเป็นฟังก์ชันมาตรฐานสำหรับการคำนวณ Jacobian ของหุ่นยนต์

Structure of Files:
HW3_utils.py: ไฟล์ที่เก็บฟังก์ชัน FKHW3 สำหรับการคำนวณ Forward Kinematics
FRA333_HW3_43_52.py: เก็บฟังก์ชัน endEffectorJacobianHW3 สำหรับการคำนวณ Jacobian แบบกำหนดเอง
testfunction.py: เก็บฟังก์ชัน CheckJacobian สำหรับการทดสอบผลลัพธ์ Jacobian
Functions:
endEffectorJacobianHW3(q: list[float]) -> list[float]

Input:
𝑞
q: ลิสต์ของข้อต่อมุม (มุมการหมุน) ขนาด 3 ค่า ที่ใช้ในการคำนวณ (เช่น [q1, q2, q3])
Output:
คืนค่า Jacobian matrix ขนาด 6x3 โดยที่ 3 แถวแรกเป็น linear velocity และ 3 แถวหลังเป็น angular velocity
การทำงาน:
ฟังก์ชันนี้คำนวณ Jacobian matrix ของหุ่นยนต์แบบ RRR โดยใช้ Forward Kinematics ในการหาตำแหน่งและการหมุนของ end-effector ก่อนจะนำไปคำนวณ Jacobian แต่ละข้อต่อ
ขั้นตอนการทำงาน:
คำนวณเมทริกซ์ 
𝑅
R และตำแหน่ง 
𝑃
P ของ end-effector ด้วยการใช้ Forward Kinematics
ใช้กฎการ cross product ในการหาความเร็วเชิงเส้น (linear velocity) และความเร็วเชิงมุม (angular velocity) ของข้อต่อแต่ละตัว
CheckJacobian(q: list[float]) -> np.ndarray

ฟังก์ชันนี้จะใช้ library ของ roboticstoolbox เพื่อคำนวณ Jacobian โดยใช้ Denavit-Hartenberg parameters สำหรับการทดสอบ
