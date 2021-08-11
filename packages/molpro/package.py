# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Molpro(CMakePackage):
    """Molpro is a comprehensive system of ab initio programs for advanced 
    molecular electronic structure calculations
    spack install molpro %intel@2021.1
    spack install molpro %gcc@10.3.0
    """

    homepage = "https://www.molpro.net"
    url      = "/p/home/padamson/opt/molpro/molpro_20210528.tar.gz"

    maintainers = ['padamson']

    version('20210528', sha256='c24937ae7119431c1efe972effc712530a3b948b8f2fe7191c9458191b1a4a65')

    depends_on('eigen')
    depends_on('lapack')
    depends_on('openblas')
    depends_on('mpi')
    depends_on('globalarrays')
    depends_on('python')
    depends_on('icu4c')
    depends_on('libxml2')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
