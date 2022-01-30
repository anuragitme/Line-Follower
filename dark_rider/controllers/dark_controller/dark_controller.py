from controller import Robot
import time

def run_robot(robot):
    
    time_step = 6
    max_speed = 25
    
    #Motors
    right_motor = robot.getDevice('R_motor')
    left_motor = robot.getDevice('L_motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    #enable ir sensors
    right_ir = robot.getDevice('ir_right')
    right_ir.enable(time_step)
    left_ir = robot.getDevice('ir_left')
    left_ir.enable(time_step)
    mid_ir = robot.getDevice('ir_mid')
    mid_ir.enable(time_step)
    str_ir = robot.getDevice('ir_str')
    str_ir.enable(time_step)

    while robot.step(time_step) != -1:
    
        # read ir sensors
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        mid_ir_value = mid_ir.getValue()
        str_ir_value = str_ir.getValue()
        
        print("left: {} --- mid: {} --- right: {} --- straight: {} ".format(left_ir_value,mid_ir_value,right_ir_value,str_ir_value))


        current_time = robot.getTime()
        print(current_time)
        
        if (  left_ir_value < 500 and  mid_ir_value > 500 and right_ir_value > 500 ):
     
            print("Go Right")
            right_speed = -0.25 * max_speed
            left_speed = -0.40 * max_speed
        if (  left_ir_value < 500 and  mid_ir_value < 500 and right_ir_value > 500 ):
     
            print("--- Right----")
            right_speed = -0 * max_speed
            left_speed = -0.40 * max_speed     
        #left_speed = -0.25 * max_speed
        #right_speed = -0.25 * max_speed
        if (  left_ir_value > 500 and  mid_ir_value > 500 and right_ir_value > 500 ):
     
            print("go left")
            right_speed = -0.40 * max_speed
            left_speed = -0.0 * max_speed
        if (  left_ir_value > 500 and  mid_ir_value < 500 and right_ir_value < 500 ):
     
            print("--- left----")
            right_speed = -0.40 * max_speed
            left_speed = -0 * max_speed 
        if (  left_ir_value > 500 and  mid_ir_value > 500 and right_ir_value < 500 ):
     
            print("888 left----")
            right_speed = -0.40 * max_speed
            left_speed = -0.0 * max_speed   
        if ( left_ir_value < 500 and  mid_ir_value > 500 and right_ir_value < 500):
             print("straight---")
             right_speed = -0.40 * max_speed
             left_speed = -0.40 * max_speed
        if(current_time > 23.37):
             print("reached our destination")
             right_speed = -0 * max_speed
             left_speed = -0 * max_speed
            
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        
    
    
        
           
                
    
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)