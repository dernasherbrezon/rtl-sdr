from conans import ConanFile, CMake


class LibrtlsdrConan(ConanFile):
    name = "librtlsdr"
    version = "0.6.4"
    license = "GPLv2"
    author = "Steve Markgraf <steve@steve-m.de>"
    url = "https://github.com/dernasherbrezon/rtl-sdr"
    description = "turns your Realtek RTL2832 based DVB dongle into a SDR receiver"
    topics = ("rtl-sdr")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.definitions["VERSION"] = self.version
        cmake.definitions["MAJOR_VERSION"] = "0"
        cmake.definitions["LIBVER"] = self.version
        cmake.configure(source_folder=".")
        cmake.build()
        cmake.install()
        
        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package_info(self):
        self.cpp_info.libs = ["librtlsdr"]
