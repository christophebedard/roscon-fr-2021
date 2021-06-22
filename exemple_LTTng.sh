NOTE: ros2 run tracetools_test test_ping
--

$ lttng create ros2-session
$ lttng enable-event --kernel sched_switch
$ lttng enable-event --userspace ros2:rclcpp_publish
$ lttng enable-event --userspace ros2:*
$ lttng start
$ ros2 run pkg exe
$ lttng stop && lttng destroy

$ babeltrace2 ros2-session
sched_switch: { cpu_id = 1 }, { prev_comm = "swapper/1", prev_tid = 0, prev_prio = 20, prev_state = ( "TASK_RUNNING" : container = 0 ), next_comm = "test_ping", next_tid = 416160, next_prio = 20 }
ros2:callback_start: { cpu_id = 1 }, { callback = 0x55FBF3541190, is_intra_process = 0 }
ros2:rclcpp_publish: { cpu_id = 1 }, { publisher_handle = 0x55FBF3541A40, message = 0x55FBF35464F0 }
ros2:rcl_publish: { cpu_id = 1 }, { publisher_handle = 0x55FBF3541A40, message = 0x55FBF35464F0 }
ros2:rmw_publish: { cpu_id = 1 }, { rmw_publisher_handle = 0x55FBF3541AE0, message = 0x55FBF35464F0 }
ros2:callback_end: { cpu_id = 1 }, { callback = 0x55FBF3541190 }