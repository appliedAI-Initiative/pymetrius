"""
This is a top-level module
"""

class SampleClass:
    def __init__(self):
        """
        sample docstring
        """
        self.hello = "hello "

    def sample_method(self, name: str):
        """
        >>> from {{cookiecutter.project_name}}.sample_module import SampleClass
        >>>
        >>> greeter = SampleClass()
        >>> greeter.sample_method("{{cookiecutter.author}}")
        'hello {{cookiecutter.author}}'

        :param name:
        :return:
        """
        return self.hello + name
