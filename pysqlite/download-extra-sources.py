"""
download-extra-sources.py

This script can be used to download extra source repositories listed in a recipe meta.yaml file.
They must be listed in the 'extra' section, as shown in the example below.

##
## meta.yaml:
##

package:
  name: multisrc-example
  version: "0.1"

source:
  fn: llvm-3.8.0.src.tar.xz
  url: http://llvm.org/releases/3.8.0/llvm-3.8.0.src.tar.xz
  md5: 07a7a74f3c6bd65de4702bf941b511a0  
  
extra:
  sources:
    cfe:
      fn: cfe-3.8.0.src.tar.xz
      url: http://llvm.org/releases/3.8.0/cfe-3.8.0.src.tar.xz
      md5: cc99e7019bb74e6459e80863606250c5



Run this script from build.sh, using conda's *root* interpreter, as shown here.

##
## build.sh
##
CONDA_PYTHON=$(conda info --root)/bin/python
${CONDA_PYTHON} ${RECIPE_DIR}/download-extra-sources.py

# ... build commands go here ...
"""
import os
from conda_build import source
from conda_build.metadata import MetaData


def main():
    recipe_dir = os.environ["RECIPE_DIR"]
    src_dir = os.environ["SRC_DIR"]
    
    metadata = MetaData(recipe_dir)
    #main_work_dir = metadata.config.work_dir
    extra_sources_sections = metadata.get_section('extra')['sources']
    

    for recipe in extra_sources_sections:
        # Override the location to clone into
        #work_dir = os.path.join(main_work_dir, name)
        #os.makedirs(work_dir)
        sub_metadata = MetaData(
          os.path.join(recipe_dir,recipe))
        #sub_metadata.config.work_dir = work_dir
        # Download source
        source.provide(sub_metadata, config=sub_metadata.config)
    
if __name__ == "__main__":
    main()