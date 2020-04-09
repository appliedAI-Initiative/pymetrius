import logging
import os
import sys

log = logging.getLogger(__name__)


def prepare_imports():
    sys.path.insert(0, os.path.abspath(os.path.join(__file__, "../..")))  # insert top level modules
    # use either the installed library or the modules in src (this way scripts can be executed in both scenarios)
    try:
        import {{cookiecutter.project_name}}
    except ModuleNotFoundError:
        src_path = os.path.abspath(os.path.join(__file__, "../../src"))
        log.warning(f"{{cookiecutter.project_name}} library was not installed, "
                    f"will try to import modules from {src_path}")
        sys.path.insert(0, src_path)
        import {{cookiecutter.project_name}}
