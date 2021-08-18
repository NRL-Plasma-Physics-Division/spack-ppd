# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Molpro(AutotoolsPackage):
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
    depends_on('blas')
    depends_on('netlib-lapack')
    depends_on('globalarrays')
    depends_on('libxml2')

    #def configure_args(self):
#
        ## Make sure we use Spack's blas/lapack:
        #lapack_libs = spec['blas'].libs.joined(';')
#
        #args = [
            #self.define('--with-lapack-path', lapack_libs),
            #]
#
        #return args

    def setup_run_environment(self, env):
        env.prepend_path('PATH', '{0}/molpro_2021.1/bin'.format(self.prefix))
        env.set('ARMCI_DEFAULT_SHMMAX', '8192')
