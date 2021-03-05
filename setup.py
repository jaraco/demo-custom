import setuptools
import distutils.command.build

distutils.command.build.build.sub_commands.append(('custom-build', None))

setuptools.setup()
