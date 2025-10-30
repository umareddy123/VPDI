from conan import ConanFile
from conan.tools.scm import Git
from conan.tools.files import copy
import os
from conan.tools.env import VirtualBuildEnv


class MyModelConan(ConanFile):
    name = "rns_mymodel0_u2a"
    version = "1.0.0"
    tlmc = 'RNS_MyModel0_U2A'
    
    # Optional metadata
    description = "A short description of the package"
    topics = ("c++", "library")
    homepage = "https://github.com/snps-ssw/RNS_MyModel0_U2A.git"
    url = "https://github.com/snps-ssw/RNS_MyModel0_U2A.git"
    license = "MIT"
    
    # Package settings
    settings = "os", "compiler", "build_type", "arch"
    #options = {"shared": [True, False], "fPIC": [True, False]}
    #default_options = {"shared": True, "fPIC": True}
    
    # def layout(self):
    #     self.folders.build = "../b/IP/RNS/U2A/MyModel0"
    #     self.folders.generators = "../b"
    #     self.folders.package = "package"
    #     self.folders.bin = "../IP/RNS/U2A/MyModel0"
    #     self.folders.source = "."

    # def config_options(self):
    #     """Configure options based on settings"""
    #     pass

    # def configure(self):
    #     """Configure package based on options and settings"""
    #     pass

    # def requirements(self):
    #     """Define package dependencies"""
    #     pass

    # def build_requirements(self):
    #     """Define build dependencies"""
    #     pass


    def source(self):
        """Get the source code"""
        git = Git(self)
        git.clone(url="https://github.com/snps-ssw/RNS_MyModel0_U2A.git")

    def generate(self):
        """Generate build system files"""
        ms = VirtualBuildEnv(self)
        my_env_var = ms.vars().get("MY_ENV_VAR")
        pass

    def build(self):
        """Build the package"""
        source_abs_path = os.path.normpath(os.path.join(self.source_folder, self.tlmc))
        build_abs_path = os.path.normpath(self.build_folder)
        bin_abs_path = os.path.normpath(os.path.join(self.recipe_folder, self.folders.bin))  

        # Convert if needed using standard methods
        source_path = self.cygwin_to_windows_path(source_abs_path)
        build_path = self.cygwin_to_windows_path(build_abs_path)
        bin_path = self.cygwin_to_windows_path(bin_abs_path)

        self.run(f"vsmake --package {source_path} --workdir {build_path} --package-LIBRARY-dir {bin_path}")

    def package(self):
        """Package the built files"""
        # Calculate bin_path the same way as in build method
        bin_abs_path = os.path.normpath(os.path.join(self.recipe_folder, self.folders.bin))
        bin_path = self.cygwin_to_windows_path(bin_abs_path)
        
        # Copy all artifacts from bin_path to package folder
        copy(self, "*", src=bin_path, dst=self.package_folder)
        
        # Copy recipe files
        copy(self, "conanfile.py", src=self.recipe_folder, dst=self.package_folder)
        #copy(self, "*.tlmc", src=self.recipe_folder, dst=self.package_folder)

    def package_info(self):
        """Define package information for consumers"""
        pass

    def cygwin_to_windows_path(self, path):
        """Convert Cygwin path to Windows path using standard methods and normalize with forward slashes"""
        if not path or not isinstance(path, str):
            return path
        
        converted_path = path
        
        # Method 1: Use cygpath utility if available (most reliable)
        try:
            import subprocess
            result = subprocess.run(['cygpath', '-w', path], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                converted_path = result.stdout.strip()
        except (subprocess.SubprocessError, FileNotFoundError, subprocess.TimeoutExpired):
            # Method 2: Use pathlib for cross-platform path handling
            try:
                from pathlib import Path, PureWindowsPath
                if path.startswith('/cygdrive/'):
                    # Convert /cygdrive/c/path to C:\path
                    parts = Path(path).parts
                    if len(parts) >= 3 and parts[1] == 'cygdrive':
                        drive = parts[2].upper() + ':'
                        remaining = parts[3:] if len(parts) > 3 else ()
                        converted_path = str(PureWindowsPath(drive, *remaining))
                else:
                    # Let pathlib handle other cases
                    converted_path = str(Path(path).resolve())
            except (OSError, ValueError, ImportError):
                # Method 3: Fallback to manual conversion
                if path.startswith('/cygdrive/'):
                    parts = path.split('/')
                    if len(parts) >= 4:
                        drive_letter = parts[2].upper()
                        remaining_path = '/'.join(parts[3:])
                        converted_path = f"{drive_letter}:/{remaining_path}"
                else:
                    converted_path = path
        
        # Convert backslashes to forward slashes for final output
        return converted_path.replace('\\', '/')
