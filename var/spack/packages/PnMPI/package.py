from spack import *
import os

class Pnmpi(Package):
    """Virtualization Layer for the MPI Profiling Interface."""

    homepage = "https://computation.llnl.gov/project/pnmpi/"

    version('1.0.0', '62ab6baae55412aeff5f2593d16b483f', url='http://tu-dresden.de/die_tu_dresden/zentrale_einrichtungen/zih/forschung/projekte/must/files/pnmpi.tar.gz')
    version('1.1.0', '50f449ba5fdef2f8736fc135c851aebd', url='http://tu-dresden.de/die_tu_dresden/zentrale_einrichtungen/zih/forschung/projekte/must/files/pnmpi-for-gti-1.1.0.tar.gz')
    version('1.2.0', 'd81ec8d463fd0881ce3fcad0515eb69d', url='http://tu-dresden.de/die_tu_dresden/zentrale_einrichtungen/zih/forschung/projekte/must/files/pnmpi-for-gti-1.2.0.tar.gz')
    version('1.3.0', 'a3a947470308a58ce70ab0b5e1f701e4', url='https://doc.itc.rwth-aachen.de/download/attachments/7373495/pnmpi-for-gti-1.3.0.tgz?version=1&modificationDate=1394454458000&api=v2')
    version('1.4.0', 'c6ffec1cf980605b942b01078dcd832f', url='https://doc.itc.rwth-aachen.de/download/attachments/7373495/pnmpi-release-for-gti-1.4.0-rc1.tar.gz?version=1&modificationDate=1417292856000&api=v2')

    def install(self, spec, prefix):
        cmake(".", *std_cmake_args)

        # FIXME: Add logic to build and install here
        make()
        make("install")

    def setup_dependent_environment(self, module, spec, dep_spec):
        """Dependencies of PnMPI find pnmpi-patch in PATH environment variable."""
        os.environ['PATH'] = ':'.join((os.path.join(self.prefix, "bin"), os.environ['PATH']))
