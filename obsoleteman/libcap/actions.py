#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    if get.buildTYPE() == "emul32": pisitools.dosed("Make.Rules", "^(PAM_CAP\s:=).*", r"\1 no")

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("prefix=/emul32 lib=../usr/lib32 DESTDIR=%s" % get.installDIR())
        pisitools.remove("/usr/lib32/*.a")
        shelltools.chmod("%s/usr/lib32/%s.so.%s" % (get.installDIR(), get.srcNAME(), get.srcVERSION()))
        return

    autotools.rawInstall("prefix=/usr DESTDIR=%s SBINDIR=%s/sbin RAISE_SETFCAP=no" % ((get.installDIR(),)*2))

    pisitools.insinto("/etc/security", "pam_cap/capability.conf")

    pisitools.remove("/usr/lib/libcap.a")
    shelltools.chmod("%s/usr/lib/%s.so.%s" % (get.installDIR(), get.srcNAME(), get.srcVERSION()))

    pisitools.dodoc("CHANGELOG", "README", "doc/capability.notes")
