import sys
import collections

def python_version():
    # Create a version_info-like namedtuple that supports attributes (major, minor, etc.)
    VersionInfo = collections.namedtuple(
        "version_info", ["major", "minor", "micro", "releaselevel", "serial"]
    )
    return VersionInfo(3, 8, 0, "final", 0)

def requests_version():
    return "2.27.1"

def pytest_version():
    return "7.1.3"
