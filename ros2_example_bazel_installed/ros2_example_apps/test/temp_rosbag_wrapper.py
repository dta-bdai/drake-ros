import subprocess

command = "mkdir -p ../rosidl_generate_ament_index_entry/lib;"
command += "cp -f ros2_example_apps/*.so ../rosidl_generate_ament_index_entry/lib/ ;"
command += "cp -f ros2_example_common/*.so ../rosidl_generate_ament_index_entry/lib/ ;"
command += "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/ros2_example_common ;"
command += "LD_PRELOAD=../rosidl_generate_ament_index_entry/lib/libros2_example_apps_msgs__rosidl_typesupport_introspection_cpp.so"
command += " ./external/ros2/ros2 bag record --all"

command = "/bin/bash"

subprocess.run(command, shell=True)
