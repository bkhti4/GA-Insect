import constants as c
import random
import math

class INSECT:
    
    def send_objects(self,sim,state): 

        if state == True:
            self.O0 = sim.send_box(x=0, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2 * c.R, r=0.5,g=0.5,b=0.5, collision_group='insect')
            self.O1 = sim.send_cylinder(x=c.L-c.R, y=c.L-c.R, z=c.L + c.R, length=c.L, radius=c.R, r=1, g=0, b=0,r1=1,r2=1,r3=0, collision_group='insect')
            self.O2 = sim.send_cylinder(x=-c.L+c.R, y=c.L-c.R, z=c.L+c.R, length=c.L, radius=c.R, r=0,g=1,b=0,r1=-1,r2=1,r3=0, collision_group='insect')
            self.O3 = sim.send_cylinder(x=c.L-c.R,y=-c.L+c.R,z=c.L+c.R, length=c.L, radius=c.R, r=0,g=0,b=1, r1=1,r2=-1,r3=0, collision_group='insect')
            self.O4 = sim.send_cylinder(x=-c.L+c.R,y=-c.L+c.R,z=c.L+c.R, length=c.L, radius=c.R, r=0.8,g=0,b=0.8, r1=-1,r2=-1,r3=0, collision_group='insect')
            self.O5 = sim.send_cylinder(x=c.L/4+c.L, y=c.L/4+c.L, z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.5, g=0.5, b=0,r1=0,r2=0,r3=1, collision_group='insect')
            self.O6 = sim.send_cylinder(x=-c.L/4-c.L, y=c.L/4+c.L, z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.8,g=0.5,b=0,r1=0,r2=0,r3=1, collision_group='insect')
            self.O7 = sim.send_cylinder(x=c.L/4+c.L,y=-c.L/4-c.L,z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.5,g=0.8,b=0, r1=0,r2=0,r3=1, collision_group='insect')
            self.O8 = sim.send_cylinder(x=-c.L/4-c.L,y=-c.L/4-c.L,z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.8,g=0.8,b=0, r1=0,r2=0,r3=1, collision_group='insect')
       
            self.O = {}
            self.O[0] = self.O0
            self.O[1] = self.O1
            self.O[2] = self.O2
            self.O[3] = self.O3
            self.O[4] = self.O4
            self.O[5] = self.O5
            self.O[6] = self.O6
            self.O[7] = self.O7
            self.O[8] = self.O8

        if state == False:

            self.lightsource = sim.send_box(x=2, y=0, z=c.L, length=c.L, width=c.L, height = c.L, r=1,g=1,b=1, collision_group='box1')
            sim.send_light_source(body_id = self.lightsource)

            self.lightcatch = sim.send_box(x=1, y=0,z=2*c.L, length=6*c.L, width=6*c.L, height = 3*c.L, r=1,g=1,b=0, collision_group='box2',mass=20.0)

            self.O0 = sim.send_box(x=0, y=-1.0, z=c.L + c.R, length=c.L, width=c.L, height=2 * c.R, r=0.5,g=0.5,b=0.5, collision_group='insect')
            self.O1 = sim.send_cylinder(x=c.L-c.R, y=-1.0+c.L-c.R, z=c.L + c.R, length=c.L, radius=c.R, r=1, g=0, b=0,r1=1,r2=1,r3=0, collision_group='insect')
            self.O2 = sim.send_cylinder(x=-c.L+c.R, y=-1.0+c.L-c.R, z=c.L+c.R, length=c.L, radius=c.R, r=0,g=1,b=0,r1=-1,r2=1,r3=0, collision_group='insect')
            self.O3 = sim.send_cylinder(x=c.L-c.R,y=-1.0-c.L+c.R,z=c.L+c.R, length=c.L, radius=c.R, r=0,g=0,b=1, r1=1,r2=-1,r3=0, collision_group='insect')
            self.O4 = sim.send_cylinder(x=-c.L+c.R,y=-1.0-c.L+c.R,z=c.L+c.R, length=c.L, radius=c.R, r=0.8,g=0,b=0.8, r1=-1,r2=-1,r3=0, collision_group='insect')
            self.O5 = sim.send_cylinder(x=c.L/4+c.L, y=-1.0+c.L/4+c.L, z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.5, g=0.5, b=0,r1=0,r2=0,r3=1, collision_group='insect')
            self.O7 = sim.send_cylinder(x=c.L/4+c.L,y=-1.0-c.L/4-c.L,z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.5,g=0.8,b=0, r1=0,r2=0,r3=1, collision_group='insect')
            self.O6 = sim.send_cylinder(x=-c.L/4-c.L, y=-1.0+c.L/4+c.L, z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.8,g=0.5,b=0,r1=0,r2=0,r3=1, collision_group='insect')
            self.O8 = sim.send_cylinder(x=-c.L/4-c.L,y=-1.0-c.L/4-c.L,z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.8,g=0.8,b=0, r1=0,r2=0,r3=1, collision_group='insect')
            

            self.O9 = sim.send_box(x=0, y=1.0, z=c.L + c.R, length=c.L, width=c.L, height=2 * c.R, r=0.5,g=0.5,b=0.5, collision_group='insect2')
            self.O10 = sim.send_cylinder(x=c.L-c.R, y=1.0+c.L-c.R, z=c.L + c.R, length=c.L, radius=c.R, r=1, g=0, b=0,r1=1,r2=1,r3=0, collision_group='insect2')
            self.O11 = sim.send_cylinder(x=-c.L+c.R, y=1.0+c.L-c.R, z=c.L+c.R, length=c.L, radius=c.R, r=0,g=1,b=0,r1=-1,r2=1,r3=0, collision_group='insect2')
            self.O12 = sim.send_cylinder(x=c.L-c.R,y=1.0-c.L+c.R,z=c.L+c.R, length=c.L, radius=c.R, r=0,g=0,b=1, r1=1,r2=-1,r3=0, collision_group='insect2')
            self.O13 = sim.send_cylinder(x=-c.L+c.R,y=1.0-c.L+c.R,z=c.L+c.R, length=c.L, radius=c.R, r=0.8,g=0,b=0.8, r1=-1,r2=-1,r3=0, collision_group='insect2')
            self.O14 = sim.send_cylinder(x=c.L/4+c.L, y=1.0+c.L/4+c.L, z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.5, g=0.5, b=0,r1=0,r2=0,r3=1, collision_group='insect2')
            self.O15 = sim.send_cylinder(x=-c.L/4-c.L, y=1.0+c.L/4+c.L, z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.8,g=0.5,b=0,r1=0,r2=0,r3=1, collision_group='insect2')
            self.O16 = sim.send_cylinder(x=c.L/4+c.L,y=1.0-c.L/4-c.L,z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.5,g=0.8,b=0, r1=0,r2=0,r3=1, collision_group='insect2')
            self.O17 = sim.send_cylinder(x=-c.L/4-c.L,y=1.0-c.L/4-c.L,z=(c.L/2)+c.R, length=c.L, radius=c.R, r=0.8,g=0.8,b=0, r1=0,r2=0,r3=1, collision_group='insect2')


            self.O = {}
            self.O[0] = self.O0
            self.O[1] = self.O1
            self.O[2] = self.O2
            self.O[3] = self.O3
            self.O[4] = self.O4
            self.O[5] = self.O5
            self.O[6] = self.O6
            self.O[7] = self.O7
            self.O[8] = self.O8
            self.O[9] = self.O9
            self.O[10] = self.O10
            self.O[11] = self.O11
            self.O[12] = self.O12
            self.O[13] = self.O13
            self.O[14] = self.O14
            self.O[15] = self.O15
            self.O[16] = self.O16
            self.O[17] = self.O17

        #self.whiteObject = sim.send_cylinder(x=0,y=0,z=0.6,length=1.0, radius=0.1)
        #self.redObject = sim.send_cylinder(x=0,y=-0.5,z=1.1,length=1.0,radius=0.1,r=1,g=0,b=0,r1=0,r2=1,r3=0)

    def send_joints(self,sim,state):
        
        if state == True:
            self.J0 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O1, x=c.L/2, y=c.L/2, z=c.L+c.R, n1=1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J1 = sim.send_hinge_joint(first_body_id=self.O1, second_body_id=self.O5, x=c.L/4+c.L, y=c.L/4+c.L, z=c.L+c.R, n1=1,n2=1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J2 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O2, x=-c.L/2, y=c.L/2, z=c.L+c.R, n1=-1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J3 = sim.send_hinge_joint(first_body_id=self.O2, second_body_id=self.O6, x=-c.L/4-c.L, y=c.L/4+c.L, z=c.L+c.R, n1=-1,n2=1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)        
            self.J4 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O3, x=c.L/2, y=-c.L/2, z=c.L+c.R, n1=1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)        
            self.J5 = sim.send_hinge_joint(first_body_id=self.O3, second_body_id=self.O7, x=c.L/4+c.L, y=-c.L/4-c.L, z=c.L+c.R, n1=1,n2=-1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J6 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O4, x=-c.L/2, y=-c.L/2, z=c.L+c.R, n1=-1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J7 = sim.send_hinge_joint(first_body_id=self.O4, second_body_id=self.O8, x=-c.L/4-c.L, y=-c.L/4-c.L, z=c.L+c.R, n1=-1,n2=-1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)        
        
            self.J = {}
            self.J[0] = self.J0
            self.J[1] = self.J1
            self.J[2] = self.J2
            self.J[3] = self.J3
            self.J[4] = self.J4
            self.J[5] = self.J5
            self.J[6] = self.J6
            self.J[7] = self.J7

        if state == False:
            
            self.J0 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O1, x=c.L/2, y=-1.0+c.L/2, z=c.L+c.R, n1=1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J1 = sim.send_hinge_joint(first_body_id=self.O1, second_body_id=self.O5, x=c.L/4+c.L, y=-1.0+c.L/4+c.L, z=c.L+c.R, n1=1,n2=1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J2 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O2, x=-c.L/2, y=-1.0+c.L/2, z=c.L+c.R, n1=-1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J3 = sim.send_hinge_joint(first_body_id=self.O2, second_body_id=self.O6, x=-c.L/4-c.L, y=-1.0+c.L/4+c.L, z=c.L+c.R, n1=-1,n2=1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J4 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O3, x=c.L/2, y=-1.0-c.L/2, z=c.L+c.R, n1=1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J5 = sim.send_hinge_joint(first_body_id=self.O3, second_body_id=self.O7, x=c.L/4+c.L, y=-1.0-c.L/4-c.L, z=c.L+c.R, n1=1,n2=-1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J6 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O4, x=-c.L/2, y=-1.0-c.L/2, z=c.L+c.R, n1=-1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J7 = sim.send_hinge_joint(first_body_id=self.O4, second_body_id=self.O8, x=-c.L/4-c.L, y=-1.0-c.L/4-c.L, z=c.L+c.R, n1=-1,n2=-1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)


            self.J8 = sim.send_hinge_joint(first_body_id=self.O9, second_body_id=self.O10, x=c.L/2, y=1.0+c.L/2, z=c.L+c.R, n1=1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J9 = sim.send_hinge_joint(first_body_id=self.O10, second_body_id=self.O14, x=c.L/4+c.L, y=1.0+c.L/4+c.L, z=c.L+c.R, n1=1,n2=1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J10 = sim.send_hinge_joint(first_body_id=self.O9, second_body_id=self.O11, x=-c.L/2, y=1.0+c.L/2, z=c.L+c.R, n1=-1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J11 = sim.send_hinge_joint(first_body_id=self.O11, second_body_id=self.O15, x=-c.L/4-c.L, y=1.0+c.L/4+c.L, z=c.L+c.R, n1=-1,n2=1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J12 = sim.send_hinge_joint(first_body_id=self.O9, second_body_id=self.O12, x=c.L/2, y=1.0-c.L/2, z=c.L+c.R, n1=1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J13 = sim.send_hinge_joint(first_body_id=self.O12, second_body_id=self.O16, x=c.L/4+c.L, y=1.0-c.L/4-c.L, z=c.L+c.R, n1=1,n2=-1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J14 = sim.send_hinge_joint(first_body_id=self.O9, second_body_id=self.O13, x=-c.L/2, y=1.0-c.L/2, z=c.L+c.R, n1=-1,n2=0,n3=1, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)
            self.J15 = sim.send_hinge_joint(first_body_id=self.O13, second_body_id=self.O17, x=-c.L/4-c.L, y=1.0-c.L/4-c.L, z=c.L+c.R, n1=-1,n2=-1,n3=0, lo=-3.14159/4, hi=3.14159/4,torque=20,speed=2)



            self.J = {}
            self.J_1 = {}
            self.J[0] = self.J0
            self.J[1] = self.J1
            self.J[2] = self.J2
            self.J[3] = self.J3
            self.J[4] = self.J4
            self.J[5] = self.J5
            self.J[6] = self.J6
            self.J[7] = self.J7
            self.J_1[0] = self.J8
            self.J_1[1] = self.J9
            self.J_1[2] = self.J10
            self.J_1[3] = self.J11
            self.J_1[4] = self.J12
            self.J_1[5] = self.J13
            self.J_1[6] = self.J14
            self.J_1[7] = self.J15
        #self.joint = sim.send_hinge_joint(first_body_id=self.whiteObject, second_body_id=self.redObject, x=0, y=0, z=1.1, n1=1, n2=0, n3=0, lo=-3.14159/4, hi=3.14159/4)

    def send_sensors(self,sim,state):

        if state == True:
            self.P1 = sim.send_vestibular_sensor(body_id = self.O0)
            self.P4 = sim.send_position_sensor(body_id = self.O0)
            self.RP_XP = sim.send_ray_sensor(body_id = self.O0, x=c.L/2, y=0, z=c.L + c.R, r1=1, r2=0, r3=0,max_distance=30)
            self.RP_XN = sim.send_ray_sensor(body_id = self.O0, x=-c.L/2, y=0, z=c.L + c.R, r1=-1, r2=0, r3=0, max_distance=30)

            self.RP_YP = sim.send_ray_sensor(body_id = self.O0, x=0, y=c.L/2, z=c.L + c.R, r1=0, r2=1, r3=0,max_distance=30)
            self.RP_YN = sim.send_ray_sensor(body_id = self.O0, x=0, y=-c.L/2, z=c.L + c.R, r1=0, r2=-1, r3=0, max_distance=30)

            self.T0 = sim.send_touch_sensor(body_id = self.O5)
            self.T1 = sim.send_touch_sensor(body_id = self.O6)
            self.T2 = sim.send_touch_sensor(body_id = self.O7) 
            self.T3 = sim.send_touch_sensor(body_id = self.O8)        
            self.T4 = sim.send_proprioceptive_sensor(joint_id = self.J0)
            self.T5 = sim.send_proprioceptive_sensor(joint_id = self.J1)
            self.T6 = sim.send_proprioceptive_sensor(joint_id = self.J2)
            self.T7 = sim.send_proprioceptive_sensor(joint_id = self.J3)
            self.T8 = sim.send_proprioceptive_sensor(joint_id = self.J4)
            self.T9 = sim.send_proprioceptive_sensor(joint_id = self.J5)
            self.T10 = sim.send_proprioceptive_sensor(joint_id = self.J6)
            self.T11 = sim.send_proprioceptive_sensor(joint_id = self.J7)

            self.S = {}
            self.S[0] = self.T0
            self.S[1] = self.T1
            self.S[2] = self.T2
            self.S[3] = self.T3
            self.S[4] = self.T4
            self.S[5] = self.T5
            self.S[6] = self.T6
            self.S[7] = self.T7
            self.S[8] = self.T8
            self.S[9] = self.T9
            self.S[10] = self.T10
            self.S[11] = self.T11

        if state == False:
            self.Obsense = sim.send_light_sensor(body_id = self.lightcatch)
            self.Obsense_Pos = sim.send_position_sensor(body_id = self.lightcatch)
            
            self.P1 = sim.send_vestibular_sensor(body_id = self.O0)
            self.P4 = sim.send_position_sensor(body_id = self.O0)
            self.RP1_XP = sim.send_ray_sensor(body_id = self.O0, x=c.L/2, y=-1.0, z=c.L + c.R, r1=1, r2=0, r3=0,max_distance=30)
            self.RP1_XN = sim.send_ray_sensor(body_id = self.O0, x=-c.L/2, y=-1.0, z=c.L + c.R, r1=-1, r2=0, r3=0, max_distance=30)

            self.RP1_YP = sim.send_ray_sensor(body_id = self.O0, x=0, y=-1.0+c.L/2, z=c.L + c.R, r1=0, r2=1, r3=0,max_distance=30)
            self.RP1_YN = sim.send_ray_sensor(body_id = self.O0, x=0, y=-1.0-c.L/2, z=c.L + c.R, r1=0, r2=-1, r3=0, max_distance=30)
            
            self.RP2_XP = sim.send_ray_sensor(body_id = self.O9, x=c.L/2, y=1.0, z=c.L + c.R, r1=1, r2=0, r3=0,max_distance=30)
            self.RP2_XN = sim.send_ray_sensor(body_id = self.O9, x=-c.L/2, y=1.0, z=c.L + c.R, r1=-1, r2=0, r3=0, max_distance=30)

            self.RP2_YP = sim.send_ray_sensor(body_id = self.O9, x=0, y=1.0+c.L/2, z=c.L + c.R, r1=0, r2=1, r3=0,max_distance=30)
            self.RP2_YN = sim.send_ray_sensor(body_id = self.O9, x=0, y=1.0-c.L/2, z=c.L + c.R, r1=0, r2=-1, r3=0, max_distance=30)


            self.Q1 = sim.send_vestibular_sensor(body_id = self.O9)
            self.Q4 = sim.send_position_sensor(body_id = self.O9)
            
            self.T0 = sim.send_touch_sensor(body_id = self.O5)
            self.T1 = sim.send_touch_sensor(body_id = self.O6)
            self.T2 = sim.send_touch_sensor(body_id = self.O7)
            self.T3 = sim.send_touch_sensor(body_id = self.O8)
            self.T4 = sim.send_proprioceptive_sensor(joint_id = self.J0)
            self.T5 = sim.send_proprioceptive_sensor(joint_id = self.J1)
            self.T6 = sim.send_proprioceptive_sensor(joint_id = self.J2)
            self.T7 = sim.send_proprioceptive_sensor(joint_id = self.J3)
            self.T8 = sim.send_proprioceptive_sensor(joint_id = self.J4)
            self.T9 = sim.send_proprioceptive_sensor(joint_id = self.J5)
            self.T10 = sim.send_proprioceptive_sensor(joint_id = self.J6)
            self.T11 = sim.send_proprioceptive_sensor(joint_id = self.J7)

            self.U = {}
            self.U[0] = sim.send_touch_sensor(body_id = self.O14)
            self.U[1] = sim.send_touch_sensor(body_id = self.O15)
            self.U[2] = sim.send_touch_sensor(body_id = self.O16)
            self.U[3] = sim.send_touch_sensor(body_id = self.O17)
            self.U[4] = sim.send_proprioceptive_sensor(joint_id = self.J8)
            self.U[5] = sim.send_proprioceptive_sensor(joint_id = self.J9)
            self.U[6] = sim.send_proprioceptive_sensor(joint_id = self.J10)
            self.U[7] = sim.send_proprioceptive_sensor(joint_id = self.J11)
            self.U[8] = sim.send_proprioceptive_sensor(joint_id = self.J12)
            self.U[9] = sim.send_proprioceptive_sensor(joint_id = self.J13)
            self.U[10] = sim.send_proprioceptive_sensor(joint_id = self.J14)
            self.U[11] = sim.send_proprioceptive_sensor(joint_id = self.J15)

            self.S = {}
            self.S[0] = self.T0
            self.S[1] = self.T1
            self.S[2] = self.T2
            self.S[3] = self.T3
            self.S[4] = self.T4
            self.S[5] = self.T5
            self.S[6] = self.T6
            self.S[7] = self.T7
            self.S[8] = self.T8
            self.S[9] = self.T9
            self.S[10] = self.T10
            self.S[11] = self.T11

        #self.P2 = sim.send_proprioceptive_sensor(joint_id = self.joint)

        #self.R3 = sim.send_ray_sensor(body_id = self.redObject, x=0, y=-1.1, z=1.0, r1=0, r2=-1, r3=0)
        
    def send_neurons(self,sim,num_of_neurons,state):
        self.SN = {}
        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id = self.S[s])
        
        if state == False:
            self.UN = {}
            for s in self.U:
                self.UN[s] = sim.send_sensor_neuron(sensor_id = self.U[s])

            self.LN = {}
            for j in self.J_1:
                self.LN[j] = sim.send_motor_neuron(joint_id = self.J_1[j], tau=0.5)

        self.MN = {}
        for j in self.J:
            self.MN[j] = sim.send_motor_neuron(joint_id = self.J[j], tau=0.5)
        
        self.HN = {}
        for mk in range(0,num_of_neurons):
            self.HN[mk] = sim.send_hidden_neuron(tau=1,alpha=1)


    def send_synapses(self,sim,wtl1,wtl2,inhib_val):
        for j in self.SN:
            for i in self.HN:
                #if j == 1 or j == 7:
                #    sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id=self.HN[i], weight=inhib_val*wtl1[j,i])
                #else:
                sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id=self.HN[i], weight=wtl1[j,i])

        for i in self.HN:
            for k in self.MN:
                #if k == 0 or k == 4:
                sim.send_synapse(source_neuron_id = self.HN[i], target_neuron_id = self.MN[k], weight=wtl2[i,k])  #math.cos(2*math.pi*wtl2[i,k])
                #if k == 2 or k == 6:
                #sim.send_synapse(source_neuron_id = self.HN[i], target_neuron_id = self.MN[k], weight=wtl2[i,k])  #math.sin(2*math.pi*wtl2[i,k])


        #light_emit = sim.get_group_id('box1')
        #light_catch = sim.get_group_id('box2')
        light_move = sim.get_group_id('insect')
        #light_move2 = sim.get_group_id('insect2')


        #sim.assign_collision('insect','box2')
        #sim.assign_collision('insect2','box2')
        #sim.assign_collision('insect','insect2')

        del self.O
        del self.J
        #del self.J1
        del self.S
        del self.SN
        del self.MN
        del self.HN




    def send_Post_neurons(self,sim,num_of_neurons1,num_of_neurons2):
        self.SN = {}
        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id = self.S[s])

        self.UN = {}
        for s in self.U:
            self.UN[s] = sim.send_sensor_neuron(sensor_id = self.U[s])

        self.LN = {}
        for j in self.J_1:
            self.LN[j] = sim.send_motor_neuron(joint_id = self.J_1[j], tau=0.5)

        self.MN = {}
        for j in self.J:
            self.MN[j] = sim.send_motor_neuron(joint_id = self.J[j], tau=0.5)

        self.HN1 = {}
        for mk in range(0,num_of_neurons1):
            self.HN1[mk] = sim.send_hidden_neuron(tau=1,alpha=1)

        self.HN2 = {}
        for mk in range(0,num_of_neurons2):
            self.HN2[mk] = sim.send_hidden_neuron(tau=1,alpha=1)


    def send_Post_synapses(self,sim,wtl1,wtl2,wtl3,wtl4):

        for j in self.SN:
            for i in self.HN1:
                sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id=self.HN1[i], weight=wtl1[j,i])

        for i in self.HN1:
            for k in self.MN:
                sim.send_synapse(source_neuron_id = self.HN1[i], target_neuron_id = self.MN[k], weight=wtl2[i,k])

        for j in self.UN:
            for i in self.HN2:
                sim.send_synapse(source_neuron_id = self.UN[j], target_neuron_id=self.HN2[i], weight=wtl3[j,i])

        for i in self.HN2:
            for k in self.LN:
                sim.send_synapse(source_neuron_id = self.HN2[i], target_neuron_id = self.LN[k], weight=wtl4[i,k])

        light_emit = sim.get_group_id('box1')
        light_catch = sim.get_group_id('box2')
        light_move = sim.get_group_id('insect')
        light_move2 = sim.get_group_id('insect2')


        sim.assign_collision('insect','box2')
        sim.assign_collision('insect2','box2')
        sim.assign_collision('insect','insect2')

        del self.O
        del self.J
        del self.J_1
        del self.S
        del self.SN
        del self.UN
        del self.MN
        del self.LN
        del self.HN1
        del self.HN2
