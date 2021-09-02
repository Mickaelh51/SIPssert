#!/usr/bin/env python
##
## TODO: update project's name
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.
##

from time import sleep
import docker
from framework import parser
from framework import scenario
from datetime import datetime
from framework import tests_set

class Controller:

    def __init__(self, sets_dirs):
        self.sets_dirs = sets_dirs
        self.docker = docker.from_env()

    def __del__(self):
        pass

    def run(self):
        for set in self.sets_dirs:
            s = tests_set.TestSet(set, self)
            s.run()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
