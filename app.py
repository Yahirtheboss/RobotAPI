from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import rclpy
from geometry_msgs.msg import Twist

# If you're trying to send a request from one origin (e.g., Postman) to a different origin (localhost),
# make sure the server's CORS policy allows this.
# Cross-Origin Resource Sharing (CORS)
app = Flask(__name__)
CORS(app)   # Enable CORS for all routes
rclpy.init()

# Creates a node and makes it a publisher
node = rclpy.create_node('flask_ros2_cmd_vel_publisher')
pub = node.create_publisher(Twist, '/cmd_vel', 10)

# Route for homepage
@app.route('/')
def home():
    return render_template('app_index.html')

@app.route('/move_robot', methods = ['POST'])
def send_command():
    if request.method == 'POST':
        data = request.get_json() 
        linear_x = data.get('linear_x')
        angular_z = data.get('angular_z')

        # Create and publish the Twist message
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        pub.publish(msg)
        
        
        # Returns a json file contaning the contents sent
        return jsonify({'status': 'Command sent', 'linear': linear_x, 'angular': angular_z}), 200
    
if __name__ == '__main__':
    try:
        app.run(debug=True)
    finally:
        node.destroy_node()
        rclpy.shutdown()

# TODO: Test by running the ROS2 node first then running the Flask API and sending the data to the ROS2 node.













                    # #!/usr/bin/env python3
                    # import rclpy
                    # from rclpy.node import Node
                    # from geometry_msgs.msg import Twist

                    # class Robot_Controller(Node):

                    #     def __init__(self):
                    #         super().__init__("robot_controller_listener_node")
                    #         # Creating the Node as a publisher, params (MessageType, Topic Name, callback, QuequeSize)
                    #         self.command_subscriber = self.create_subscription(
                    #             Twist, "/cmd_vel", self.command_callback, 10)
                            
                    #     # This is just to confirm that the subscriber got the proper message data.
                    #     def command_callback(self, msg:Twist):
                    #         self.get_logger().info(f"Linear Velocity Received: {msg.linear.x}\n"
                    #                                f"Angular Velocity Received: {msg.angular.z}")

                    # # Initializes the ROS 2 system.
                    # # Creates a node instance (Robot_Controller).
                    # # Keeps the node alive and spinning (processing data/events).
                    # # Catches user interruptions (e.g., pressing Ctrl+C).
                    # # Cleans up the node and shuts down the ROS 2 system when the program ends.
                    # def main(args=None):
                    #     rclpy.init(args=args)
                    #     node = Robot_Controller()
                    #     try:
                    #         rclpy.spin(node)
                    #     except KeyboardInterrupt:
                    #         pass
                    #     finally:
                    #         node.destroy_node()
                    #         rclpy.shutdown()

                    # if __name__ == "__main__":
                    #     main()
