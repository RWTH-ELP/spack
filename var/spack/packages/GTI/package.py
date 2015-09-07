from spack import *
import os

class Gti(Package):
    """GTI infrastructure for MUST."""

    homepage = "https://doc.itc.rwth-aachen.de/display/CCP/Project+MUST"
    url      = "https://doc.itc.rwth-aachen.de/download/attachments/7373495/gti-release-1.4.0.tgz?version=1&modificationDate=1427730709000&api=v2"

    version('1.4.0', 'da6cf5969f8f4c2ecf4c1ff3473d5bda', url='https://doc.itc.rwth-aachen.de/download/attachments/7373495/gti-release-1.4.0.tgz?version=1&modificationDate=1427730709000&api=v2')

    depends_on("PnMPI")

    def install(self, spec, prefix):
        cmake(".", *std_cmake_args)

        # FIXME: Add logic to build and install here
        make()
        make("install")
