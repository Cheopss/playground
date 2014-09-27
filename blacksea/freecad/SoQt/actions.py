#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --enable-optimization \
                         --enable-man \
                         --enable-exceptions \
                         --disable-debug \
                         --disable-maintainer-mode \
                         --disable-dependency-tracking \
                         --enable-shared \
                         --disable-static \
                         --with-qt=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS", "README*")
