import os
import pytest
import subprocess


def test_file_contents():
    return "1\nkitty cat\n3\n"


@pytest.fixture
def setup_a_file(tmp_path):
    old_cwd = os.getcwd()
    os.chdir(tmp_path)

    test_file_path = os.path.join(tmp_path, "test_file")

    with open(test_file_path, "w") as test_file:
        test_file.write(test_file_contents())

    yield

    os.remove(test_file_path)
    os.chdir(old_cwd)


def test_verify_test_file_exists(bin_path, setup_a_file):
    with open("test_file") as test_file:
        contents = test_file.read()

        assert contents == test_file_contents()

        with subprocess.Popen(["python3", f"{bin_path}/tac"], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE) as tac:
            tac.stdin.write(test_file_contents().encode())
            out, err = tac.communicate()
            assert err == b''
            assert out == b'3\nkitty cat\n1\n'

