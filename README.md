# roscon-fr-2021

Files and artifacts for my [ROSCon Fr 2021 presentation on 2021-06-22](http://roscon.fr/#jour-1-22-juin): "Tracer ROS 2 avec `ros2_tracing`" ("Tracing ROS 2 with `ros2_tracing`")

## Presentation PDFs

* [French](./2021-06-22%20ROSCon%20Fr%202021%20-%20Tracer%20ROS%202%20avec%20ros2_tracing.pdf)
* [English version](./2021-06-22%20ROSCon%20Fr%202021%20-%20Tracer%20ROS%202%20avec%20ros2_tracing%20-%20English.pdf)

## Artifacts

* [LTTng commands example](./exemple_LTTng.sh)
* [`ros2 trace` command example](./exemple_ros2-trace.sh)
* [`Trace` action example](./exemple_ros2-launch-trace.py)
* [`tracetools_analysis` example code](./exemple_tracetools_analysis.py)
* [`tracetools_analysis` example plot](./exemple_tracetools_analysis_plot.png)
* [demo plot (message publications)](./demo_plot_messages.png)
* [demo plot (controller updates)](./demo_plot_controller_updates.png)
* [demo `ros2_control` controller `init()` instrumentation](./demo_instrumentation_init.png)
* [demo `ros2_control` controller `update()` instrumentation](./demo_instrumentation_update.png)
* [demo launch file](./demo_extrait_launch_file.py)

## Demo

* Jupyter Notebook (instructions and analysis code): https://gitlab.com/ros-tracing/tracetools_analysis/-/blob/add-basic-ros2-control-demo/tracetools_analysis/analysis/ros2_control_demo.ipynb
* `ros2_control` instrumentation: https://github.com/christophebedard/ros2_control/tree/add-basic-ros2-control-instrumentation
* tracing launch file: https://gitlab.com/ros-tracing/tracetools_analysis/-/blob/add-basic-ros2-control-demo/tracetools_analysis/launch/ros2_control.launch.py
