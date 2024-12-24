;; Auto-generated. Do not edit!


(when (boundp 'bigwork::hand_msg)
  (if (not (find-package "BIGWORK"))
    (make-package "BIGWORK"))
  (shadow 'hand_msg (find-package "BIGWORK")))
(unless (find-package "BIGWORK::HAND_MSG")
  (make-package "BIGWORK::HAND_MSG"))

(in-package "ROS")
;;//! \htmlinclude hand_msg.msg.html


(defclass bigwork::hand_msg
  :super ros::object
  :slots (_x _y _fingertips_x _fingertips_y ))

(defmethod bigwork::hand_msg
  (:init
   (&key
    ((:x __x) 0)
    ((:y __y) 0)
    ((:fingertips_x __fingertips_x) (make-array 0 :initial-element 0 :element-type :integer))
    ((:fingertips_y __fingertips_y) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _fingertips_x __fingertips_x)
   (setq _fingertips_y __fingertips_y)
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:fingertips_x
   (&optional __fingertips_x)
   (if __fingertips_x (setq _fingertips_x __fingertips_x)) _fingertips_x)
  (:fingertips_y
   (&optional __fingertips_y)
   (if __fingertips_y (setq _fingertips_y __fingertips_y)) _fingertips_y)
  (:serialization-length
   ()
   (+
    ;; int32 _x
    4
    ;; int32 _y
    4
    ;; int32[] _fingertips_x
    (* 4    (length _fingertips_x)) 4
    ;; int32[] _fingertips_y
    (* 4    (length _fingertips_y)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _x
       (write-long _x s)
     ;; int32 _y
       (write-long _y s)
     ;; int32[] _fingertips_x
     (write-long (length _fingertips_x) s)
     (dotimes (i (length _fingertips_x))
       (write-long (elt _fingertips_x i) s)
       )
     ;; int32[] _fingertips_y
     (write-long (length _fingertips_y) s)
     (dotimes (i (length _fingertips_y))
       (write-long (elt _fingertips_y i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _x
     (setq _x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _y
     (setq _y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32[] _fingertips_x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _fingertips_x (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _fingertips_x i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _fingertips_y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _fingertips_y (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _fingertips_y i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get bigwork::hand_msg :md5sum-) "380b203d8077022bcbc89696459febd1")
(setf (get bigwork::hand_msg :datatype-) "bigwork/hand_msg")
(setf (get bigwork::hand_msg :definition-)
      "int32 x
int32 y
int32[] fingertips_x
int32[] fingertips_y
")



(provide :bigwork/hand_msg "380b203d8077022bcbc89696459febd1")


