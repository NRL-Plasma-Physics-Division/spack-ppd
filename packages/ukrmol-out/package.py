# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class UkrmolOut(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://zenodo.org/record/4120626"
    url      = "https://zenodo.org/record/4120626/files/ukrmol-out-3.1.tar.gz"

    maintainers = ['padamson']

    version('3.1', sha256='4d5970ae06bcc114ff97d0d4ad58cbf01ef14d18f688a4946064933efeb3dcaf')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
