
conan install . -if build --update --build missing -o amgs:build_apps=True -pr %CONAN_PROFILE%
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=install -DBUILD_APPS=ON -DFAST_COMPILE=ON -G "Visual Studio 16 2019" -A x64 ..
cmake --build . --config Release -j %BUILD_THREADS%
