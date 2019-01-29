/*=========================================================================
 *
 *  Copyright Insight Software Consortium
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *         http://www.apache.org/licenses/LICENSE-2.0.txt
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *=========================================================================*/

#include "itkImage.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkBinaryThinningImageFilter3D.h"

#include "itkCommand.h"
#include "itkTestingMacros.h"

namespace
{
class ShowProgress : public itk::Command
{
public:
  itkNewMacro(ShowProgress);

  void
  Execute(itk::Object *caller, const itk::EventObject &event) override
  {
    Execute((const itk::Object *)caller, event);
  }

  void
  Execute(const itk::Object *caller, const itk::EventObject &event) override
  {
    if (!itk::ProgressEvent().CheckEvent(&event))
    {
      return;
    }
    const auto *processObject = dynamic_cast<const itk::ProcessObject *>(caller);
    if (!processObject)
    {
      return;
    }
    std::cout << " " << processObject->GetProgress();
  }
};
} // namespace

int itkMedialThicknessImageFilterTest(int argc, char *argv[])
{
  if (argc <= 2)
  {
    std::cerr << "Usage: " << argv[0];
    std::cerr << "inputImageFile outputImageFile";
    std::cerr << std::endl;
    return EXIT_FAILURE;
  }
  const char *inputImageFileName = argv[1];
  const char *outputImageFileName = argv[2];

  const unsigned int Dimension = 3;
  using InputPixelType = unsigned char;
  using OutputPixelType = unsigned char;
  using InputImageType = itk::Image<InputPixelType, Dimension>;
  using OutputImageType = itk::Image<OutputPixelType, Dimension>;

  using FilterType = itk::BinaryThinningImageFilter3D<InputImageType, OutputImageType>;
  FilterType::Pointer filter = FilterType::New();

  EXERCISE_BASIC_OBJECT_METHODS(filter, BinaryThinningImageFilter3D, ImageToImageFilter);

  // Read image
  using ReaderType = itk::ImageFileReader<InputImageType>;
  ReaderType::Pointer reader = ReaderType::New();
  reader->SetFileName(inputImageFileName);
  try
  {
    reader->Update();
  }
  catch (itk::ExceptionObject &ex)
  {
    std::cout << ex << std::endl;
    return EXIT_FAILURE;
  }
  std::cout << inputImageFileName << " sucessfully read." << std::endl;

  ShowProgress::Pointer showProgress = ShowProgress::New();
  filter->AddObserver(itk::ProgressEvent(), showProgress);
  filter->SetInput(reader->GetOutput());

  typedef itk::ImageFileWriter<OutputImageType> WriterType;
  WriterType::Pointer writer = WriterType::New();
  writer->SetFileName(outputImageFileName);
  writer->SetInput(filter->GetOutput());

  TRY_EXPECT_NO_EXCEPTION(writer->Update());

  return EXIT_SUCCESS;
}
