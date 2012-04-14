#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is part of box-linux-sync.
#
# Copyright (C) 2012 Vítor Brandão <noisebleed@noiselabs.org>
#
# box-linux-sync is free software; you can redistribute it  and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# box-linux-sync is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with box-linux-sync; if not, see
# <http://www.gnu.org/licenses/>.

from noiselabs.box.config import BoxConfig

class BoxSetup(object):
    """
    Box setup helper.
    """
    def __init__(self, box_console):
        self.config = BoxConfig(box_console)
        self.out = box_console
    
    def check(self):
        self.check_config()
        self.check_deps()

    def check_config(self):
        self.config.check_file()
        self.config.check_config()

    def check_deps(self):
        self.check_dep_davfs()

    def check_dep_davfs(self):
        self.out.debug("Checking davfs installation...")

    def wizard(self):
        pass
    