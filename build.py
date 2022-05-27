#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author
import os
import inspect

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.sphinx")


name = "Alien_Invasion"
version = "1.0"
summary = "Alien_invasion_game"
url = "https://github.com/Darya1488/ProjectOnPython"
description = """2D-game cosmic shooter"""
authors = [Author("Pozhidaeva Alyona", "a.pozhidaeva@g.nsu.ru"),
           Author("Baturova Dari", "d.baturova@g.nsu.ru"),
           Author("Nadezhdina Darya", "d.nadezhdina@g.nsu.ru")]
licence = "None"
default_task = ["analyze", "publish", "sphinx_generate_documentation"]


@init
def set_properties(project):
    project.set_property("dir_source_main_python", "src/")
    project.set_property("dir_source_unittest_python", "unittest/")
    project.set_property("dir_source_main_scripts", "scripts/")
    project.set_property("coverage_break_build", False)

    project.set_property("sphinx_builder", "html")
    project.set_property("sphinx_config_path", "source")
    project.set_property("sphinx_source_dir", "source")
    project.set_property("sphinx_output_dir", "docs/_build")
