# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-fno-strict-aliasing")
    pisitools.dosed("configure", '(wx_cv_std_libpath="lib)64"', r'\1"')

    autotools.configure("--enable-gtk2 \
                         --enable-shared \
                         --disable-optimise \
                         --disable-debug \
                         --enable-no_deps \
                         --disable-rpath \
                         --enable-intl \
                         --enable-geometry \
                         --enable-timer \
                         --enable-unicode \
                         --enable-sound \
                         --enable-mediactrl \
                         --enable-xrc \
                         --enable-graphics_ctx \
                         --enable-display \
                         --enable-joystick \
                         --disable-gtktest \
                         --disable-sdltest \
                         --disable-precomp-headers \
                         --with-gtk=3 \
                         --with-libpng=sys \
                         --with-libjpeg=sys \
                         --with-libtiff=sys \
                         --with-libxpm=sys \
                         --with-sdl \
                         --without-gnomeprint \
                         --without-gnomevfs \
                         --without-odbc \
                         --with-opengl \
                         --with-regex=sys \
                         --with-zlib=sys \
                         --with-expat=sys")

def build():
    autotools.make()
    autotools.make("-C locale allmo")

def install():
    autotools.install()

    pisitools.remove("/usr/bin/wx-config")
    pisitools.dosym("/usr/lib/wx/config/gtk2-unicode-release-2.8", "/usr/bin/wx-config")

    pisitools.remove("/usr/share/locale/it/LC_MESSAGES/wxmsw.mo")

    pisitools.dodoc("docs/*.txt", "docs/*.htm")
