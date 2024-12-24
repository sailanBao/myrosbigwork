
(cl:in-package :asdf)

(defsystem "bigwork-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "hand_msg" :depends-on ("_package_hand_msg"))
    (:file "_package_hand_msg" :depends-on ("_package"))
  ))