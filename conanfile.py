from conans import ConanFile, tools, CMake
import sys
from distutils import sysconfig
import os.path as p
import platform

PY_MAJOR, PY_MINOR = sys.version_info[ 0 : 2 ]

def GetGlobalPythonPrefix():
  # In a virtualenv, sys.real_prefix points to the parent Python prefix.
  if hasattr( sys, 'real_prefix' ):
    return sys.real_prefix
  # In a pyvenv (only available on Python 3), sys.base_prefix points to the
  # parent Python prefix. Outside a pyvenv, it is equal to sys.prefix.
  if PY_MAJOR >= 3:
    return sys.base_prefix
  return sys.prefix


def GetPossiblePythonLibraryDirectories():
  prefix = GetGlobalPythonPrefix()

  if platform.system() == 'Windows':
    return [ p.join( prefix, 'libs' ) ]
  # On pyenv and some distributions, there is no Python dynamic library in the
  # directory returned by the LIBPL variable. Such library can be found in the
  # "lib" or "lib64" folder of the base Python installation.
  return [
    sysconfig.get_config_var( 'LIBPL' ),
    p.join( prefix, 'lib64' ),
    p.join( prefix, 'lib' )
  ]


class LibtorrentPythonConan(ConanFile):
    name = "LibtorrentPython"
    version = "1.1.4"
    requires = "Libtorrent/1.1.4@lola/stable",
    settings = "os", "compiler", "arch", "build_type"
    options = {"python_version": ["2.7"]}
    default_options = "python_version=2.7"
    exports = "*"
    generators = "cmake"
    build_policy = "missing"

    def conan_info(self):
        self.info.settings.clear()

    def configure(self):
        self.options["Libtorrent"].shared=True
        self.options["Boost"].shared=True
        self.options["Boost"].python=True
        self.options["zlib"].shared=False
        self.options["bzip2"].shared=False
        self.options["OpenSSL"].shared=False

        # with position independent code
        if self.settings.compiler != "Visual Studio":
          self.options["Libtorrent"].fPIC=True
          self.options["Boost"].fPIC=True
          self.options["bzip2"].fPIC=True

    def build(self):
        cmake = CMake(self.settings)
        pythonpaths = "-DPYTHON_INCLUDE_DIR=" + sysconfig.get_python_inc() + " -DPYTHON_LIBRARY=" + str(GetPossiblePythonLibraryDirectories())
        print pythonpaths
        self.run('cmake src %s %s -DEXAMPLE_PYTHON_VERSION=%s' % (cmake.command_line, pythonpaths, self.options.python_version))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy('*.py*')
        self.copy("*.so")

    def package_info(self):
        self.env_info.PYTHONPATH.append(self.package_folder)
