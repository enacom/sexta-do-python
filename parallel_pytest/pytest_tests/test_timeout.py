import pytest


@pytest.mark.timeout(2)
def test_simple_loop():
    for i in range(int(1e9)):
        print(str(i).zfill(9), end='\r')
    return


if __name__ == '__main__':
    pytest.main()
