itk_module_test()

set(BinaryThinningImageFilter3DTests
  BinaryThinningImageFilter3DTest.cxx
  )

CreateTestDriver(BinaryThinningImageFilter3D "${BinaryThinningImageFilter3D-Test_LIBRARIES}" "${BinaryThinningImageFilter3DTests}")

itk_add_test(NAME BinaryThinningImageFilter3DTest
  COMMAND BinaryThinningImageFilter3DTestDriver
  BinaryThinningImageFilter3DTest
  DATA{Data/input.tif} DATA{Data/output.tif}
  )
