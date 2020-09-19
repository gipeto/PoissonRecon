
option(BUILD_APPS "Build applications" OFF)
option(BIG_DATA "Supports processing requiring more than 32-bit integers for indexing" OFF)
option(FAST_COMPILE "If enabled, only a single version of the code is compiled" OFF)
option(SHOW_WARNINGS "Display compilation warnings" OFF)
option(ARRAY_DEBUG "If enabled, array access is tested for validity" OFF)
option(USE_SEG_FAULT_HANDLER "Tries to dump a stack trace in the case of a segfault (gcc only)" OFF)

message(STATUS "Active options:")

if(BUILD_APPS)
  message(STATUS "BUILD_APPS")
endif()

if(BIG_DATA)
  message(STATUS "BIG_DATA")
  add_definitions(-DBIG_DATA_SET)
endif()

if(FAST_COMPILE)
  message(STATUS "FAST_COMPILE")
  add_definitions(-DFAST_COMPILE_SET)
endif()

if(SHOW_WARNINGS)
  message(STATUS "SHOW_WARNINGS")
  add_definitions(-DSHOW_WARNINGS_SET)
endif()

if(ARRAY_DEBUG)
   message(STATUS "ARRAY_DEBUG")
  add_definitions(-DARRAY_DEBUG_SET)
endif()

if(USE_SEG_FAULT_HANDLER)
   message(STATUS "USE_SEG_FAULT_HANDLER")
  add_definitions(-DUSE_SEG_FAULT_HANDLER_SET)
endif()