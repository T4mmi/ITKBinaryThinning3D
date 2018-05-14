ITKBinaryThinning3D
==============================

**An ITK module to compute 3D image skeleton**

.. |CircleCI| image:: https://circleci.com/gh/T4mmi/ITKBinaryThinning3D.svg?style=shield
    :target: https://circleci.com/gh/T4mmi/ITKBinaryThinning3D
.. |TravisCI| image:: https://travis-ci.org/T4mmi/ITKBinaryThinning3D.svg?branch=ITKv4
    :target: https://travis-ci.org/T4mmi/ITKBinaryThinning3D
.. |AppVeyor| image:: https://img.shields.io/appveyor/ci/T4mmi/ITKBinaryThinning3D.svg
    :target: https://ci.appveyor.com/project/T4mmi/ITKBinaryThinning3D
    
=========== =========== ===========
   Linux      macOS       Windows
=========== =========== ===========
|CircleCI|  |TravisCI|  |AppVeyor|
=========== =========== ===========

ITK currently comes with a 2D binary thinning (skeletonisation) method, but does not support 3D or higher.

This contribution implements a new itk::BinaryThinningImageFilter3D that can find all deletable surface points at every iteration and is thus very fast.

Overview
--------

This is a module for the `Insight Toolkit (ITK) <http://itk.org>`_ that provides filters that compute the skeleton of 3D images.

For more information, see the `Insight Journal article <http://hdl.handle.net/1926/1292>`_::


  Homann H.
  Implementation of a 3D thinning algorithm
  The Insight Journal - 2007 July - December.
  http://hdl.handle.net/1926/1292
  http://insight-journal.org/browse/publication/181

Installation
------------

Python
^^^^^^

Binary `Python packages <https://pypi.python.org/pypi/itk-binarythinning3d>`_
are available for Linux, macOS, and Windows. They can be installed with::

  python -m pip install --upgrade pip
  python -m pip install itk-binarythinning3d


License
-------

This software is distributed under the Apache 2.0 license.

Please see
the *LICENSE* file for details.

Acknowledgements
----------------

**This module only supports ITKv4 at the moment, working on ITKv5...**

This contribution is only a python wrapping of the original Insight Journal, no changes have been made to the code.  

The test image was converted from `uint16` DICOM to `uint8` TIFF format to avoid GDCM type errors.