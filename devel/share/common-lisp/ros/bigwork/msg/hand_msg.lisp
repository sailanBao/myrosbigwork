; Auto-generated. Do not edit!


(cl:in-package bigwork-msg)


;//! \htmlinclude hand_msg.msg.html

(cl:defclass <hand_msg> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:integer
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:integer
    :initform 0)
   (fingertips_x
    :reader fingertips_x
    :initarg :fingertips_x
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (fingertips_y
    :reader fingertips_y
    :initarg :fingertips_y
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass hand_msg (<hand_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <hand_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'hand_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name bigwork-msg:<hand_msg> is deprecated: use bigwork-msg:hand_msg instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <hand_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bigwork-msg:x-val is deprecated.  Use bigwork-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <hand_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bigwork-msg:y-val is deprecated.  Use bigwork-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'fingertips_x-val :lambda-list '(m))
(cl:defmethod fingertips_x-val ((m <hand_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bigwork-msg:fingertips_x-val is deprecated.  Use bigwork-msg:fingertips_x instead.")
  (fingertips_x m))

(cl:ensure-generic-function 'fingertips_y-val :lambda-list '(m))
(cl:defmethod fingertips_y-val ((m <hand_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bigwork-msg:fingertips_y-val is deprecated.  Use bigwork-msg:fingertips_y instead.")
  (fingertips_y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <hand_msg>) ostream)
  "Serializes a message object of type '<hand_msg>"
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'fingertips_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'fingertips_x))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'fingertips_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'fingertips_y))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <hand_msg>) istream)
  "Deserializes a message object of type '<hand_msg>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'fingertips_x) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'fingertips_x)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'fingertips_y) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'fingertips_y)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<hand_msg>)))
  "Returns string type for a message object of type '<hand_msg>"
  "bigwork/hand_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'hand_msg)))
  "Returns string type for a message object of type 'hand_msg"
  "bigwork/hand_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<hand_msg>)))
  "Returns md5sum for a message object of type '<hand_msg>"
  "380b203d8077022bcbc89696459febd1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'hand_msg)))
  "Returns md5sum for a message object of type 'hand_msg"
  "380b203d8077022bcbc89696459febd1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<hand_msg>)))
  "Returns full string definition for message of type '<hand_msg>"
  (cl:format cl:nil "int32 x~%int32 y~%int32[] fingertips_x~%int32[] fingertips_y~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'hand_msg)))
  "Returns full string definition for message of type 'hand_msg"
  (cl:format cl:nil "int32 x~%int32 y~%int32[] fingertips_x~%int32[] fingertips_y~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <hand_msg>))
  (cl:+ 0
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'fingertips_x) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'fingertips_y) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <hand_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'hand_msg
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':fingertips_x (fingertips_x msg))
    (cl:cons ':fingertips_y (fingertips_y msg))
))
