from spack import *
import os

class Gti(Package):
    """GTI infrastructure for MUST."""

    homepage = "https://doc.itc.rwth-aachen.de/display/CCP/Project+MUST"
    url      = "https://doc.itc.rwth-aachen.de/download/attachments/7373495/gti-release-1.4.0.tgz?version=1&modificationDate=1427730709000&api=v2"

    version('1.4.0', 'da6cf5969f8f4c2ecf4c1ff3473d5bda', url='https://doc.itc.rwth-aachen.de/download/attachments/7373495/gti-release-1.4.0.tgz?version=1&modificationDate=1427730709000&api=v2')
    version('experimental', git='git@github.com:RWTH-ELP/GTI_svn.git')

    depends_on("PnMPI")
    depends_on("PnMPI@experimental+experimental")

    def install(self, spec, prefix):
        cmake(".", *std_cmake_args)

        # FIXME: Add logic to build and install here
        make()
        make("install")

    def setup_dependent_environment(self, module, spec, dep_spec):
        """Dependencies of PnMPI find pnmpi-patch in PATH environment variable."""
        os.environ['PATH'] = ':'.join((os.path.join(self.prefix, "bin"), os.environ['PATH']))
