ros_import_binary(
    name = @name@,
    executable = @executable@,
    py_binary_rule = py_binary,
    data = @data@,
    deps = @deps@ + [
        requirement("pyyaml"),
        requirement("empy"),
        requirement("lark"),
        requirement("catkin_pkg"),
    ],
)
