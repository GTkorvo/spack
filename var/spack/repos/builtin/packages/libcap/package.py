##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Libcap(MakefilePackage):
    """Libcap implements the user-space interfaces to the POSIX 1003.1e
    capabilities available in Linux kernels. These capabilities are a
    partitioning of the all powerful root privilege into a set of
    distinct privileges."""

    homepage = "https://sites.google.com/site/fullycapable/"
    url      = "https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.25.tar.gz"

    version('2.25', '4b18f7166a121138cca0cdd8ab64df4c')

    patch('libcap-fix-the-libcap-native-building-failure-on-CentOS-6.7.patch')

    def install(self, spec, prefix):
        make_args = [
            'RAISE_SETFCAP=no',
            'lib=lib',
            'prefix={0}'.format(prefix),
            'install'
        ]
        make(*make_args)

        chmod = which('chmod')
        chmod('+x', join_path(prefix.lib, 'libcap.so'))
