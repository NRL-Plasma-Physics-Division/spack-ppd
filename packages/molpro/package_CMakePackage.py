# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Molpro(CMakePackage):
    """Molpro is a comprehensive system of ab initio programs for advanced 
    molecular electronic structure calculations.
    """

    homepage = "https://www.molpro.net"
    url      = "/p/home/padamson/opt/molpro/molpro_20210528.tar.gz"

    maintainers = ['padamson']

    version('20210528', sha256='c24937ae7119431c1efe972effc712530a3b948b8f2fe7191c9458191b1a4a65')

    depends_on('python')
    depends_on('icu4c')
    depends_on('eigen')
    depends_on('mpi')
    depends_on('cray-libsci')
    depends_on('globalarrays')
    depends_on('libxml2')

    def cmake_args(self):
        args = [
                '-DBUILD_TESTING:BOOL=ON',
                #'-DGCI_TEST:BOOL=ON',
                #'-DSYMMETRY_MATRIX_COMPLEXDOUBLE:BOOL=ON',
                #'-DSYMMETRY_MATRIX_DOUBLE:BOOL=ON',
                #'-DSYMMETRY_MATRIX_FLOAT:BOOL=ON',
                #'-DXCGRID_BUILD_TESTS:BOOL=ON',
                #'-DWHATEVER:STRING=somevalue',
                #self.define('ENABLE_BROKEN_FEATURE', False),
                #self.define_from_variant('DETECT_HDF5', 'hdf5'),
                #self.define_from_variant('THREADS'), # True if +threads
                ]

        return args
