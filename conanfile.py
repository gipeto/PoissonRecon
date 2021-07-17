
from conans import ConanFile, CMake, tools

class AdaptiveMultiGridSolver(ConanFile):
    name = "amgs"
    version = '13.72.0'
    license = "MIT (https://github.com/mkazhdan/PoissonRecon/blob/master/LICENSE)"
    url = "https://github.com/mkazhdan/PoissonRecon/"
    description = """This recipe expose the Adaptive Multigrid Solver of the PoissonRecon
                      repository as a library.
                      The source is a fork of the linked repository, reorganized for allowing
                      cmake integration and refactored to remove external dependencies on the
                      solver.
                   """

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"
    options = {"shared": [True, False], "build_apps": [True, False], "with_io": [True, False]}
    default_options = {"shared": False, "build_apps": False, "with_io": False}
    short_paths = True

    scm = {
        "type" : "git",
        "url"  : "auto",
        "revision" : "auto",
    }

    def requirements(self):
        if self.options.build_apps:
            self.requires('zlib/[>=1.2.11]')
            self.requires('libpng/[>=1.6.37]')
            self.requires('libjpeg/9c')
        
    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="lib", src="lib")
        self.copy('*.so*', dst='lib', src='lib')

    def _configure(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_APPS'] = "ON" if self.options.build_apps else "OFF"
        cmake.definitions['WITH_IO'] = "ON" if self.options.with_io else "OFF"
        if self.settings.os == 'Macos':
            cmake.definitions['CMAKE_MACOSX_RPATH'] = "TRUE"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure()
        cmake.build()

    def package(self):
        cmake = self._configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
