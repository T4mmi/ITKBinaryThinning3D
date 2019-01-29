itk_module_test()

#${itk-module} will be the name of this module and will not need to be
#changed when this module is renamed.

set(${itk-module}Tests
  itkBinaryThinningImageFilter3DTest.cxx
)

CreateTestDriver(${itk-module}  "${${itk-module}-Test_LIBRARIES}" "${${itk-module}Tests}")

itk_add_test(NAME itkBinaryThinningImageFilter3DTest
  COMMAND ${itk-module}TestDriver
  itkBinaryThinningImageFilter3DTest
  DATA{Input/input.tif} ${ITK_TEST_OUTPUT_DIR}/skeleton.tif
)