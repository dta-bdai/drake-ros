from typing import Tuple


"""
Contains classes which describe how to use Python and C++ libraries.
"""


def _init_helper(instance, kwargs):
    for name in instance.__slots__:
        setattr(instance, name, tuple())
    for key, value in kwargs.items():
        if key not in instance.__slots__:
            raise TypeError(f'Unexpected keyword argument {key}')
        if not value:
            value = tuple()
        else:
            value = tuple(value)
        setattr(instance, key, value)


class CcProperties:

    __slots__ = (
        'link_libraries',
        'include_directories',
        'compile_flags',
        'defines',
        'link_flags',
        'link_directories'
    )

    link_libraries: Tuple[str]
    include_directories: Tuple[str]
    compile_flags: Tuple[str]
    defines: Tuple[str]
    link_flags: Tuple[str]
    link_directories: Tuple[str]

    def __init__(self, **kwargs):
        _init_helper(self, kwargs)


class PyProperties:

    __slots__ = (
        'cc_extensions',
        'cc_libraries',
        'python_eggs',
        'python_packages',
        'python_modules',
    )

    cc_extensions: Tuple[str]
    cc_libraries: Tuple[str]
    python_eggs: Tuple[str]
    python_packages: Tuple[str]
    python_modules: Tuple[str]

    def __init__(self, **kwargs):
        _init_helper(self, kwargs)
