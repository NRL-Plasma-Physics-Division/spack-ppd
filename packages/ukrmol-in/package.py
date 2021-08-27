# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class UkrmolIn(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://zenodo.org/record/5025567"
    url      = "https://zenodo.org/record/5025567/files/ukrmol-in-3.1.2.tar.gz"

    maintainers = ['padamson']

    version('3.1.2', sha256='ec5b9d1d55d541424efdb07a2858b83a808b4b24efef701a3770f5e1b7b889f2')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
