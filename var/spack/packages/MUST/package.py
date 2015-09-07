from spack import *

class Must(Package):
    """Marmot Umpire Scalable Tool."""

    homepage = "https://doc.itc.rwth-aachen.de/display/CCP/Project+MUST"
    url      = "https://doc.itc.rwth-aachen.de/download/attachments/7373495/must-release-1.4.0.tgz?version=2&modificationDate=1427732652000&api=v2"

    version('experimental', git='git@github.com:RWTH-ELP/must_new.git')

    depends_on("GTI@experimental+experimental")

    def install(self, spec, prefix):
        cmake(".", *std_cmake_args)

        # FIXME: Add logic to build and install here
        make()
        make("install")
