import sys
import pytest

if __name__ == "__main__":
    print("Running tests...")
    sys.exit(pytest.main(["-v", "-s", "tests"]))
