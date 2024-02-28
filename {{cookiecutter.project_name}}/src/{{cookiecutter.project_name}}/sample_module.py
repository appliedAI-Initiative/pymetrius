"""Top-level module."""


class SampleClass:
    """Sample docstring. Note that init docstrings should be underneath the class and not the init method itself
    (this looks prettier in sphinx). They still will be rendered correctly in pycharm's quick documentation.

    :param param: some parameter
    """

    def __init__(self, param: str | None = None):
        self.hello = "hello "
        self.param = param

    def sample_method(self, name: str) -> str:
        """>>> from {{cookiecutter.project_name}}.sample_module import SampleClass
        >>>
        >>> greeter = SampleClass()
        >>> greeter.sample_method("{{cookiecutter.author}}")
        'hello {{cookiecutter.author}}'.

        :param name:
        :return:
        """
        return self.hello + name
