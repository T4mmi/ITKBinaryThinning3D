[CircleCI]: https://img.shields.io/circleci/project/github/T4mmi/ITKBinaryThinning3D/master.svg?label=Linux
[TravisCI]: https://img.shields.io/travis/T4mmi/ITKBinaryThinning3D/master.svg?label=macOS
[Appveyor]: https://img.shields.io/appveyor/ci/T4mmi/itkbinarythinning3d.svg?label=Windows
[Python version]: https://img.shields.io/pypi/pyversions/itk-binarythinning3d.svg
[PyPI version]: https://img.shields.io/pypi/v/itk-binarythinning3d.svg?label=PyPI


ITKBinaryThinning3D
==============================

**An ITK module to compute 3D image skeleton**

![CircleCI][CircleCI] ![TravisCI][TravisCI] ![Appveyor][Appveyor] ![Python version][Python version] ![PyPI version][PyPI version] 

ITK currently comes with a 2D binary thinning (skeletonisation) method, but does not support 3D or higher.  
This contribution implements a new itk::BinaryThinningImageFilter3D that can find all deletable surface points at every iteration and is thus very fast.


Overview
--------

This is a module for the [Insight Toolkit (ITK)](http://itk.org) that provides filters that compute the skeleton of 3D images.  
For more information, see the [Insight Journal article](http://hdl.handle.net/1926/1292):  
```  
  Homann H.  
  Implementation of a 3D thinning algorithm  
  The Insight Journal - 2007 July - December.  
  http://hdl.handle.net/1926/1292  
  http://insight-journal.org/browse/publication/181  
```

### Filters

- **[`itk::BinaryThinningImageFilter3D<TInputImage, TOutputImage>`](include/itkBinaryThinningImageFilter3D.h)**: Compute the 3D skeleton of the input image.

### Warnings
The *filtered/output/skeleton* image is a **pseudo binary image coded with `0` and `1`**, be sure to visualize it with the correct lookup table. *Blank output image might just be the effect of the viewer*, you might have to check manually the actual values (see [issue #4](https://github.com/T4mmi/ITKBinaryThinning3D/issues/4#issuecomment-455090984)).


Installation
------------

Binary [python packages](https://pypi.python.org/pypi/itk-binarythinning3d) are available for Linux, macOS, and Windows. They can be installed with:
```
  python -m pip install --upgrade pip
  python -m pip install itk-binarythinning3d
```


Usage
-----

Once ITK imported, you can use the `itk.BinaryThinningImageFilter3D` just as any other [ITK methods](https://itkpythonpackage.readthedocs.io/en/latest/Quick_start_guide.html):
```
skeleton = itk.BinaryThinningImageFilter3D.New(image)
```  

Here is a simple python script that reads an image, applies the skeletonization and writes the resulting image in a file:
```
import itk

input_filename = sys.argv[1]
output_filename = sys.argv[2]

image = itk.imread(input_filename)
skeleton = itk.BinaryThinningImageFilter3D.New(image)

itk.imwrite(skeleton, output_filename)
```


License
-------

This software is distributed under the Apache 2.0 license.

Please see the *LICENSE* file for details.


Acknowledgements
----------------

**This contribution is only a python wrapping of the original Insight Journal post**  
*No significant changes have been made to the source code*:
- Wrapping was done using this [documention](https://itkpythonpackage.readthedocs.io/en/latest/Build_ITK_Module_Python_packages.html).
- The original test image was converted from `uint16` DICOM to `uint8` TIFF format to avoid GDCM errors.
- Source files were slightly changed to be wrapped and pass KWStyle tests.