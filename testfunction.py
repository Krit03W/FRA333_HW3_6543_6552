import roboticstoolbox as rtb
import numpy as np
from spatialmath import SE3
from math import pi

d_1 = 0.0892
a_2 = -0.425
a_3 = -0.39243
d_4 = 0.109
d_5 = 0.093
d_6 = 0.082

Eff = (
    SE3.Tx(a_3) @  # Translation along X-axis
    SE3.Tz(d_4) @  # Translation along Z-axis
    SE3.Ty(-d_5) @  # Translation along Y-axis (negative)
    SE3.Ry(-pi/2) @  # Rotation around Y-axis by -π/2
    SE3.Tz(d_6)  # Final translation along Z-axis
)
robot = rtb.DHRobot(
    [
        rtb.RevoluteMDH(d=d_1, offset=pi),
        rtb.RevoluteMDH(alpha=pi/2),
        rtb.RevoluteMDH(a=a_2)
    ],
    tool=Eff,
    name="RRR_Robot"
)

def CheckJacobian(q: list[float]) -> np.ndarray:
    return robot.jacob0(q)

def CheckSingularity(q: list[float]) -> bool:
    epsilon = 0.001
    # คำนวณ Jacobian ของหุ่นยนต์ที่มุม q
    jacobian = CheckJacobian(q)
    
    # หา Determinant ของส่วนตำแหน่ง (3x3) ของ Jacobian
    det = np.linalg.det(jacobian[:3, :3])
    
    # ถ้า determinant ใกล้ 0 มาก (ถือว่าเป็น Singularity)
    if np.abs(det) < epsilon:
        return 1  # เป็น Singularity
    return 0  # ไม่เป็น Singularity


def CheckEffort(q: list[float], w: list[float]) -> list[float]:
    # แปลงค่า w เป็น numpy array
    wrench = np.array(w)

    # คำนวณ Jacobian matrix โดยใช้ฟังก์ชันจาก robot model (robot.jacob0)
    J_e = robot.jacob0(q)

    # คำนวณค่า torque โดยใช้ J^T * wrench
    tau = J_e.T @ wrench

    # ส่งคืนค่า torque ในรูปแบบ list
    return tau.tolist()


