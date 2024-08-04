import pytest





def test_simple_attribute(driver, request: pytest.FixtureRequest):
    print()
    print("----------------------------------------------------------")
    # print(request.node.__dict__)
    print(request.node.attr1)

    print("----------------------------------------------------------")

