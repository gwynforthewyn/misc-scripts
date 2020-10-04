import os
import pytest

@pytest.fixture(autouse = True)
def setup_PATH():
    bin_path = os.path.abspath("../bin")
    os.putenv("PATH", f"{bin_path}:{os.environ['PATH']}")
