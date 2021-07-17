add_library(apps_utils INTERFACE)
target_include_directories(apps_utils INTERFACE $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include> "${CMAKE_CURRENT_BINARY_DIR}")
target_sources(apps_utils INTERFACE
                include/apps_utils/CmdLineParser.h
                include/apps_utils/CmdLineParser.inl
                include/apps_utils/io/Image.h
                include/apps_utils/io/JPEG.h
                include/apps_utils/io/JPEG.inl
                include/apps_utils/io/PNG.h
                include/apps_utils/io/PNG.inl
)

target_link_libraries(apps_utils INTERFACE
                      amgs::amgs
                      ZLIB::ZLIB
                      JPEG::JPEG
                      PNG::PNG)
install(TARGETS apps_utils
        DESTINATION ${CMAKE_INSTALL_BINDIRs})

add_library(apps_utils::apps_utils ALIAS apps_utils)

