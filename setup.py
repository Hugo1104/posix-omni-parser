"""Install posix omni parser
"""

from distutils.core import setup

setup(name='posix_omni_parser',
      version='1.0',
      description='posix-omni-parser',
      author='Savvas Savvides',
      author_email='',
      url='https://github.com/pkmoore/posix-omni-parser',
      # sysDef must be an upper level package rather than under posix_omni_parser
      # because the pickle file generated by parse-syscall-definitions assumes that it
      # will exist at this point in the namespace.
      packages=['posix_omni_parser',
                'posix_omni_parser.parsers',
                'sysDef'])
