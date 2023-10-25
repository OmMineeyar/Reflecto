import numpy as np
import math as mh
def angle_bisector(P1, P2, P3):
    P1 = np.array(P1)
    P2 = np.array(P2)
    P3 = np.array(P3)
    
    V1 = P1 - P2
    V2 = P3 - P2

    V1_normalized = V1 / np.linalg.norm(V1)
    V2_normalized = V2 / np.linalg.norm(V2)

    angle_bisector = V1_normalized + V2_normalized

    angle_bisector_normalized = angle_bisector / np.linalg.norm(angle_bisector)

    return angle_bisector_normalized
P3=[0,10,2]
P1=[0,10,0]
P2=[0,12,0]
if(mh.asin(np.dot(angle_bisector(P1,P2,P3),[0,1,0]))*360/(2*mh.pi)==0):
    print(mh.asin(np.dot(angle_bisector(P1,P2,P3),[1,0,0]))*360/(2*mh.pi))
else:
    print(mh.asin(np.dot(angle_bisector(P1,P2,P3),[0,1,0]))*360/(2*mh.pi))