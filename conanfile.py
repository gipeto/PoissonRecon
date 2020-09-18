
from conans import ConanFile, CMake, tools

class AdaptiveFiniteElementSolver(ConanFile):
    name = "afes"
    lib_version = '13.61.0'
    pkg_version = '0'
    version = '{}-{}'.format(lib_version, pkg_version)
    license = "MIT (https://github.com/mkazhdan/PoissonRecon/blob/master/LICENSE)"
    url = "https://github.com/mkazhdan/PoissonRecon/"
    description = """This recipe expose the Adaptive Finite Element Solver of the PoissonRecon
                      repository as a library.
                      The source is a fork of the linked repository, reorganized for allowing
                      cmake integration and refactored to remove external dependencies on the
                      solver.
                   """

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"
    options = {"shared": [True, False], "build_apps": [True, False], "precompiled_headers": [True, False]}
    default_options = {"shared": False, "build_apps": False, "precompiled_headers": False}
    short_paths = True

    scm = {
        "type" : "git",
        "url"  : "auto",
        "revision" : "auto",
    }

    def requirements(self):
        if self.options.build_apps:
            self.requires('zlib/[>=1.2.11]@conan/stable')
            self.requires('libpng/[>=1.6.37]@bincrafters/stable')
            self.requires('libjpeg/9c@bincrafters/stable')
        
    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="lib", src="lib")
        self.copy('*.so*', dst='lib', src='lib')

    def _configure(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_APPS'] = "ON" if self.options.build_apps else "OFF"
        cmake.definitions['PRECOMPILED_HEADERS'] = "ON" if self.options.precompiled_headers else "OFF"
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
