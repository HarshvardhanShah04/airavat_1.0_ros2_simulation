from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, TextSubstitution
from launch_ros.actions import SetParameter



def generate_launch_description():
    use_sim_time = SetParameter(name='use_sim_time', value=True)

    robot_description_path = PathJoinSubstitution([FindPackageShare('airavat_description'), 'urdf', 'my_airavat_1.0_compiled.urdf.xacro'])

    robot_description_value = ParameterValue(Command([
            FindExecutable(name='xacro'),
            ' ',
            robot_description_path
        ]),
        value_type=str
    )

    rviz_config_path = PathJoinSubstitution([FindPackageShare('airavat_description'), 'rviz', 'rviz_config.rviz'])

    gz_sim_path = PathJoinSubstitution([FindPackageShare('ros_gz_sim'), 'launch', 'gz_sim.launch.py'])

    world_file_path = PathJoinSubstitution([FindPackageShare('airavat_bringup'), 'world', 'test_world.sdf'])

    gzbridge_config_file_path = PathJoinSubstitution([FindPackageShare('airavat_bringup'), 'config', 'gazebo_bridge.yaml'])


    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description_value
        }]
    )

    # # Add this to see if robot_description is being generated
    # print("Robot description path:", robot_description_path)

    # # Add output to your RSP node
    # rsp_node = Node(
    #     package='robot_state_publisher',
    #     executable='robot_state_publisher',
    #     name='robot_state_publisher',
    #     parameters=[{
    #         'robot_description': robot_description_value,
    #         'use_sim_time': True
    #     }],
    #     output='screen'  # This will show any errors
    # )

    launch_1 = IncludeLaunchDescription(PythonLaunchDescriptionSource(gz_sim_path),
        launch_arguments={
            # "gz_args": [world_file_path, "-r, -v, 4"]
            'gz_args': [world_file_path, TextSubstitution(text=' -r -v 4')]
            # "gz_args": "empty.sdf -r -v 4"
        }.items(),
    )

    ros_gz_node = Node(
        package = 'ros_gz_sim',
        executable = 'create',
        name= 'gz',
        arguments=['-topic', 'robot_description']
    )

    rviz2_node = Node(
        package = 'rviz2',
        executable = 'rviz2',
        name = 'rviz2',
        output='screen',
        arguments=['-d', rviz_config_path]
    )

    ros_gz_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters = [{
            'config_file': gzbridge_config_file_path
        }]
    )

    static_tf_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_transform_publisher_lidar',
        output='screen',
        arguments=['0','0','0','0','0','0','1','lidar_link','airavat_1.0/base_footprint/gpu_lidar']
    )

    return LaunchDescription([
        use_sim_time,
        rsp_node,
        launch_1,
        ros_gz_node,
        rviz2_node,
        static_tf_node,
        ros_gz_bridge 
    ])