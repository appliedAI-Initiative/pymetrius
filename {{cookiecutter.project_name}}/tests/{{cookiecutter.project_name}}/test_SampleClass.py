from {{cookiecutter.project_name}}.sample_module import SampleClass


def test_SampleClass():
    greeter = SampleClass()
    assert greeter.hello == "hello "