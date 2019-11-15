# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "xf86-video-vesa-%s" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("COPYING", "ChangeLog", "README")