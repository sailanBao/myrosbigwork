# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/fan/桌面/houseworks/bigwork/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/fan/桌面/houseworks/bigwork/build

# Utility rule file for bigwork_gencpp.

# Include the progress variables for this target.
include bigwork/CMakeFiles/bigwork_gencpp.dir/progress.make

bigwork_gencpp: bigwork/CMakeFiles/bigwork_gencpp.dir/build.make

.PHONY : bigwork_gencpp

# Rule to build all files generated by this target.
bigwork/CMakeFiles/bigwork_gencpp.dir/build: bigwork_gencpp

.PHONY : bigwork/CMakeFiles/bigwork_gencpp.dir/build

bigwork/CMakeFiles/bigwork_gencpp.dir/clean:
	cd /home/fan/桌面/houseworks/bigwork/build/bigwork && $(CMAKE_COMMAND) -P CMakeFiles/bigwork_gencpp.dir/cmake_clean.cmake
.PHONY : bigwork/CMakeFiles/bigwork_gencpp.dir/clean

bigwork/CMakeFiles/bigwork_gencpp.dir/depend:
	cd /home/fan/桌面/houseworks/bigwork/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/fan/桌面/houseworks/bigwork/src /home/fan/桌面/houseworks/bigwork/src/bigwork /home/fan/桌面/houseworks/bigwork/build /home/fan/桌面/houseworks/bigwork/build/bigwork /home/fan/桌面/houseworks/bigwork/build/bigwork/CMakeFiles/bigwork_gencpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : bigwork/CMakeFiles/bigwork_gencpp.dir/depend

