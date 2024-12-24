# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "bigwork: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ibigwork:/home/fan/桌面/houseworks/bigwork/src/bigwork/msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(bigwork_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg" NAME_WE)
add_custom_target(_bigwork_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "bigwork" "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(bigwork
  "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bigwork
)

### Generating Services

### Generating Module File
_generate_module_cpp(bigwork
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bigwork
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(bigwork_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(bigwork_generate_messages bigwork_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg" NAME_WE)
add_dependencies(bigwork_generate_messages_cpp _bigwork_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bigwork_gencpp)
add_dependencies(bigwork_gencpp bigwork_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bigwork_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(bigwork
  "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bigwork
)

### Generating Services

### Generating Module File
_generate_module_eus(bigwork
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bigwork
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(bigwork_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(bigwork_generate_messages bigwork_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg" NAME_WE)
add_dependencies(bigwork_generate_messages_eus _bigwork_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bigwork_geneus)
add_dependencies(bigwork_geneus bigwork_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bigwork_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(bigwork
  "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bigwork
)

### Generating Services

### Generating Module File
_generate_module_lisp(bigwork
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bigwork
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(bigwork_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(bigwork_generate_messages bigwork_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg" NAME_WE)
add_dependencies(bigwork_generate_messages_lisp _bigwork_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bigwork_genlisp)
add_dependencies(bigwork_genlisp bigwork_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bigwork_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(bigwork
  "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bigwork
)

### Generating Services

### Generating Module File
_generate_module_nodejs(bigwork
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bigwork
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(bigwork_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(bigwork_generate_messages bigwork_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg" NAME_WE)
add_dependencies(bigwork_generate_messages_nodejs _bigwork_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bigwork_gennodejs)
add_dependencies(bigwork_gennodejs bigwork_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bigwork_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(bigwork
  "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bigwork
)

### Generating Services

### Generating Module File
_generate_module_py(bigwork
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bigwork
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(bigwork_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(bigwork_generate_messages bigwork_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/fan/桌面/houseworks/bigwork/src/bigwork/msg/hand_msg.msg" NAME_WE)
add_dependencies(bigwork_generate_messages_py _bigwork_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bigwork_genpy)
add_dependencies(bigwork_genpy bigwork_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bigwork_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bigwork)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bigwork
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(bigwork_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(bigwork_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(bigwork_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bigwork)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bigwork
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(bigwork_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(bigwork_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(bigwork_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bigwork)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bigwork
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(bigwork_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(bigwork_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(bigwork_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bigwork)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bigwork
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(bigwork_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(bigwork_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(bigwork_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bigwork)
  install(CODE "execute_process(COMMAND \"/home/fan/anaconda3/envs/rosopencv/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bigwork\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bigwork
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(bigwork_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(bigwork_generate_messages_py sensor_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(bigwork_generate_messages_py std_msgs_generate_messages_py)
endif()
