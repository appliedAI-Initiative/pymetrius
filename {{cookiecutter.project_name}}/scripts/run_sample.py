from utils import prepare_imports
prepare_imports()

from {{cookiecutter.project_name}}.sample_module import SampleClass
from config import get_config

if __name__ == "__main__":

    c = get_config()
    assert c.sample_key == "sample_value"
    print(SampleClass().sample_method("{{cookiecutter.author}}"))
    print("Your new library project {{cookiecutter.project_name}} is waiting for you!")
    print("Try running your first build with tox")