# -*- coding: utf-8 -*-
from __future__ import print_function
from os import sys

try:
    from skbuild import setup
except ImportError:
    print('scikit-build is required to build from source.', file=sys.stderr)
    print('Please run:', file=sys.stderr)
    print('', file=sys.stderr)
    print('  python -m pip install scikit-build')
    sys.exit(1)

setup(
    name='itk-binarythinning3d',
    version='5.0b1',
    author='Insight Software Consortium',
    author_email='itk+community@discourse.itk.org',
    packages=['itk'],
    package_dir={'itk': 'itk'},
    download_url=r'https://github.com/InsightSoftwareConsortium/ITKBinaryThinningImageFilter3D',
    description=r'An ITK module to compute 3D image skeleton',
    long_description='ITK currently comes with a 2D binary thinning (skeletonisation) method, but does not support 3D or higher. This contribution implements a new itkBinaryThinningImageFilter3D that can find all deletable surface points at every iteration and is thus very fast.',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: C++",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
    license='Apache',
    keywords='ITK InsightToolkit',
    url=r'https://itk.org/',
    install_requires=[
        r'itk>=5.0b1'
    ]
    )
