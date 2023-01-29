import re

from dewey import __version__ as version


def test_version():
    """Sanity check that there is a version in the right place"""
    assert re.match(r"^\d+\.\d+\.\d+$", version)
