import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Get package directories
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    
    # Paths
    nav2_params_file = PathJoinSubstitution([
        FindPackageShare('airavat_nav2'),
        'config',
        'nav2_params.yaml'
    ])
    
    map_file = os.path.join(
        get_package_share_directory('airavat_nav2'),
        'maps',
        'my_map.yaml'
    )
    
    rviz_config_file = PathJoinSubstitution([
        FindPackageShare('airavat_nav2'),
        'rviz2',
        'nav2_view.rviz'
    ])
    
    # Launch configuration variables
    use_sim_time = LaunchConfiguration('use_sim_time')
    autostart = LaunchConfiguration('autostart')
    params_file = LaunchConfiguration('params_file')
    map_yaml_file = LaunchConfiguration('map')
    
    # Declare launch arguments
    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='True',
        description='Use simulation (Gazebo) clock if true'
    )
    
    declare_autostart_cmd = DeclareLaunchArgument(
        'autostart',
        default_value='True',
        description='Automatically startup the nav2 stack'
    )
    
    declare_params_file_cmd = DeclareLaunchArgument(
        'params_file',
        default_value=nav2_params_file,
        description='Full path to the ROS2 parameters file to use'
    )
    
    declare_map_yaml_cmd = DeclareLaunchArgument(
        'map',
        default_value=map_file,
        description='Full path to map yaml file to load'
    )
    
    # Nav2 full bringup (includes map_server + AMCL + navigation)
    bringup_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': map_yaml_file,
            'use_sim_time': use_sim_time,
            'params_file': params_file,
            'autostart': autostart
        }.items()
    )
    
    # RViz
    rviz_cmd = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )
    
    # Create the launch description and populate
    ld = LaunchDescription()
    
    # Declare the launch options
    ld.add_action(declare_use_sim_time_cmd)
    ld.add_action(declare_autostart_cmd)
    ld.add_action(declare_params_file_cmd)
    ld.add_action(declare_map_yaml_cmd)
    
    # Add the actions
    ld.add_action(bringup_cmd)
    ld.add_action(rviz_cmd)
    
    return ld