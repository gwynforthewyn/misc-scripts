import os
import pytest

@pytest.fixture()
def bin_path():
    this_file_path = os.path.realpath(__file__)
    this_file_dir = os.path.dirname(this_file_path)

    return os.path.abspath(os.path.join(this_file_dir, "bin"))
