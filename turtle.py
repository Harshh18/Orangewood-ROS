#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def move_rectangle():
    # Initialize the node
    rospy.init_node('turtle_rectangle', anonymous=True)
    
    # Create a publisher
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Set the rate
    rate = rospy.Rate(1) # 1 Hz
    
    # Create Twist message
    vel_msg = Twist()
    
    # Set the distance and speed
    speed = 2
    distance = 4
    
    for i in range(4):
        # Move forward
        vel_msg.linear.x = speed
        vel_msg.angular.z = 0
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        
        # Move forward for 'distance' units
        while current_distance < distance:
            pub.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = speed * (t1 - t0)
        
        # Stop moving forward
        vel_msg.linear.x = 0
        pub.publish(vel_msg)
        
        # Rotate 90 degrees
        vel_msg.angular.z = math.pi/2  # 90 degrees in radians
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        
        while current_angle < math.pi/2:
            pub.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = math.pi/2 * (t1 - t0)
        
        # Stop rotating
        vel_msg.angular.z = 0
        pub.publish(vel_msg)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        move_rectangle()
    except rospy.ROSInterruptException:
        pass
