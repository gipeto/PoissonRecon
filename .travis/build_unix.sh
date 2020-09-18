 #!/bin/bash

# exit when any command fails
set -e

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT

conan install . -if build --update --build missing -o afes:build_apps=True -pr $CONAN_PROFILE
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=install -DBUILD_APPS=ON -DFAST_COMPILE=ON -G "Ninja" ..
travis-pls ninja -j 1 -k 1