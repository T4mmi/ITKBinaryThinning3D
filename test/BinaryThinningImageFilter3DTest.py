#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# title           : BinaryThinningImageFilter3DTest.py
# description     : Test file for the ITKBinaryThinning3D module wrapping
# copyright       : Insight Software Consortium
# license         : Apache License, Version 2.0
# author(s)       : Thomas Janvier [thomas.p.janvier@gmail.com]
# creation        : 24 April 2018

import os
import sys
import itk
import warnings


def BinaryThinningImageFilter3DTest(source, destination=None):
    ''' Basic ITK pipeline using BinaryThinningImageFilter3D

    Read input image -> Skeletonize -> Write output image

    Args:
        source {str} -- input filename
        destination {str, optional} -- output filename

    Returns:
        the skeleton image {numpy.array} -- 3D array of unsigned char
    '''
    # check if input exists
    if not os.path.isfile(source):
        raise IOError("Source must be an existing image file")
    ##############
    # IMAGE READER
    ##############
    # Initialize the io buffer
    imageIO = itk.ImageIOFactory.CreateImageIO(source, itk.ImageIOFactory.ReadMode)
    imageIO.SetFileName(source)
    imageIO.ReadImageInformation()
    # Typedef
    Dimension = imageIO.GetNumberOfDimensions()
    if Dimension != 3:
        raise AssertionError("Input image must be tridimensional")
    InputPixelType = itk.ctype(itk.ImageIOBase.GetComponentTypeAsString(
        imageIO.GetComponentType()).replace('_', ' '))  # prevent 'unsigned_char' error
    InputImageType = itk.Image[InputPixelType, Dimension]
    UnsignedCharImageType = itk.Image[itk.UC, Dimension]
    # Read the image
    imageFileReader = itk.ImageFileReader[InputImageType].New()
    imageFileReader.SetFileName(source)
    imageFileReader.ReleaseDataFlagOff()
    ################
    # IMAGE THINNING
    ################
    binaryThinning = itk.BinaryThinningImageFilter3D[UnsignedCharImageType, UnsignedCharImageType].New()
    binaryThinning.SetInput(imageFileReader.GetOutput())
    # ITK pipeline update
    pipelineEndpoint = binaryThinning
    pipelineEndpoint.Update()
    ##############
    # IMAGE WRITER
    ##############
    if destination: #  if destination is set
        # Image file serialization
        imageFileWriter = itk.ImageFileWriter[UnsignedCharImageType].New()
        imageFileWriter.SetFileName(destination)
        imageFileWriter.SetInput(pipelineEndpoint.GetOutput())
        imageFileWriter.Update()
    # finally return the thinning result
    return itk.GetArrayFromImage(pipelineEndpoint.GetOutput())


if __name__ == '__main__':
    '''Entry point for ITKBinaryThinning3D module wrapping testing

    If no arguments are provided, use the module test data.

    First argument is treated as the input image filename.
    Second argument is treated as the output image filename (if none, replace the input).

    Example:
        $ python BinaryThinningImageFilter3DTest.py

    '''
    if len(sys.argv) == 1:
        try:
            CWD = os.path.dirname(os.path.realpath(__file__))
        except Exception as err:
            warnings.warn(
                "Could not access `__file__` attribute, using `os.getcwd()` instead",
                RuntimeWarning)
            CWD = os.getcwd()
        BinaryThinningImageFilter3DTest(
            os.path.join(CWD, 'Data', 'input.tif'),
            os.path.join(CWD, 'Data', 'output.tif')
        )
    elif len(sys.argv) == 2:
        BinaryThinningImageFilter3DTest(sys.argv[1], sys.argv[1])
    else:
        BinaryThinningImageFilter3DTest(sys.argv[1], sys.argv[2])
    sys.exit(0)
