def generate_launch_description():
    launchfile_path = os.path.join(
        get_package_share_directory('ros2_control_demo_bringup'),
        'launch',
        'rrbot_system_position_only.launch.py',
    )
    base_ros2_control_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([launchfile_path]),
        launch_arguments={ 'start_rviz': 'True' }.items(),
    )
    return LaunchDescription([
        Trace(
            session_name='ros2-control-demo',
            events_ust=[
                'ros2:*',
                'ros2:control_controller_init',
                'ros2:control_controller_update',
            ],
        ),
        base_ros2_control_launch,
    ])
