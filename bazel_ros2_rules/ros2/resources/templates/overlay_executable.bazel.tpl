ros_import_binary(
    name = @name@,
    executable = @executable@,
    py_binary_rule = py_binary,
    data = @data@,
    deps = @deps@ + [
        "@pypi//catkin_pkg",
        "@pypi//empy",
        "@pypi//lark",
        "@pypi//netifaces",
        "@pypi//packaging",
        "@pypi//pyyaml",
    ],
)
