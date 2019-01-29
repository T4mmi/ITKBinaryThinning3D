itk_module_test()

set(BinaryThinningImageFilter3DTests
  itkBinaryThinningImageFilter3DTest.cxx
  )

CreateTestDriver(BinaryThinningImageFilter3D "${BinaryThinningImageFilter3D-Test_LIBRARIES}" "${BinaryThinningImageFilter3DTests}")

itk_add_test(NAME BinaryThinningImageFilter3DTest
  COMMAND BinaryThinningImageFilter3DTestDriver
  itkBinaryThinningImageFilter3DTest
  DATA{Input/input.tif} ${ITK_TEST_OUTPUT_DIR}/skeleton.tif
  )
