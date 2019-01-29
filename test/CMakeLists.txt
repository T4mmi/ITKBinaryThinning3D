itk_module_test()

#${itk-module} will be the name of this module and will not need to be
#changed when this module is renamed.

set(${itk-module}Tests
  itkBinaryThinningImageFilterTest.cxx
)

CreateTestDriver(${itk-module}  "${${itk-module}-Test_LIBRARIES}" "${ITK${itk-module}Tests}")

itk_add_test(NAME itkBinaryThinningImageFilterTest
  COMMAND ${itk-module}TestDriver  itkBinaryThinningImageFilterTest
  DATA{Input/input.tif} ${ITK_TEST_OUTPUT_DIR}/medial_axis.tif
)
