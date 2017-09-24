from conans import ConanFile, tools, CMake

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
        pythonpaths = "-DPYTHON_INCLUDE_DIR=/usr/include/python2.7 -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so"
        self.run('cmake src %s %s -DEXAMPLE_PYTHON_VERSION=%s' % (cmake.command_line, pythonpaths, self.options.python_version))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy('*.py*')
        self.copy("*.so")

    def package_info(self):
        self.env_info.PYTHONPATH.append(self.package_folder)
