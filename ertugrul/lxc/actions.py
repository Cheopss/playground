#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize("--force --install")
    autotools.autoreconf("-vif")

    autotools.configure("--prefix=/usr \
                         --sbindir=/usr/bin \
                         --localstatedir=/var \
                         --libexecdir=/usr/libexec \
                         --sysconfdir=/etc \
                         --enable-api-doc \
                         --disable-apparmor \
                         --enable-seccomp \
                         --enable-cgmanager \
                         --enable-capabilities \
                         --enable-lua")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.doman("doc/*.[1-8]")
    pisitools.dodir("/var/lib/lxc")

    # Install management tools
    for script in shelltools.ls("lxc-management-tools/lxc*"):
        pisitools.dobin(script)

    #shelltools.move("%s/usr/lib/lxc/templates" % get.installDIR(), "%s/%s/lxc/" % (get.installDIR(), get.docDIR()))
