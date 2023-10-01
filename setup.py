from distutils.version import LooseVersion
import os
import sys

from setuptools import __version__ as setuptools_version
from setuptools import find_packages
from setuptools import setup
from setuptools.command.test import test as TestCommand

version = "1.7.1.b0"

# Remember to update local-oldest-requirements.txt when changing the minimum
# acme/certbot version.
install_requires = [
    "requests",
    "setuptools",
    "zope.interface",
]

if not os.environ.get("SNAP_BUILD"):
    install_requires.extend(
        [
            # We specify the minimum acme and certbot version as the current plugin
            # version for simplicity. See
            # https://github.com/certbot/certbot/issues/8761 for more info.
            f"acme>={version}",
            f"certbot>={version}",
        ]
    )
elif "bdist_wheel" in sys.argv[1:]:
    raise RuntimeError(
        "Unset SNAP_BUILD when building wheels " "to include certbot dependencies."
    )

setuptools_known_environment_markers = LooseVersion(setuptools_version) >= LooseVersion(
    "36.2"
)
if setuptools_known_environment_markers:
    install_requires.append('mock ; python_version < "3.3"')
elif "bdist_wheel" in sys.argv[1:]:
    raise RuntimeError(
        "Error, you are trying to build certbot wheels using an old version "
        "of setuptools. Version 36.2+ of setuptools is required."
    )
if os.environ.get("SNAP_BUILD"):
    install_requires.append("packaging")

docs_extras = [
    "Sphinx>=1.0",  # autodoc_member_order = 'bysource', autodoc_default_flags
    "sphinx_rtd_theme",
]

# Load readme to use on PyPI
with open("README.rst", encoding="utf8") as f:
    readme = f.read()


class PyTest(TestCommand):
    user_options = []

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def run_tests(self):
        import shlex

        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name="certbot-dns-beget",
    version=version,
    description="Beget DNS Authenticator plugin for Certbot",
    url="https://github.com/skrashevich/certbot-dns-beget",
    author="Certbot Project",
    author_email="s.krashevich@gmail.com",
    license="Apache License 2.0",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        "docs": docs_extras,
    },
    entry_points={
        "certbot.plugins": [
            "dns-beget = certbot_dns_beget._internal.dns_beget:Authenticator",
        ],
    },
    tests_require=["pytest"],
    test_suite="certbot_dns_beget",
    cmdclass={"test": PyTest},
)
