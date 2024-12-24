// Auto-generated. Do not edit!

// (in-package bigwork.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class hand_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
      this.fingertips_x = null;
      this.fingertips_y = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0;
      }
      if (initObj.hasOwnProperty('fingertips_x')) {
        this.fingertips_x = initObj.fingertips_x
      }
      else {
        this.fingertips_x = [];
      }
      if (initObj.hasOwnProperty('fingertips_y')) {
        this.fingertips_y = initObj.fingertips_y
      }
      else {
        this.fingertips_y = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type hand_msg
    // Serialize message field [x]
    bufferOffset = _serializer.int32(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.int32(obj.y, buffer, bufferOffset);
    // Serialize message field [fingertips_x]
    bufferOffset = _arraySerializer.int32(obj.fingertips_x, buffer, bufferOffset, null);
    // Serialize message field [fingertips_y]
    bufferOffset = _arraySerializer.int32(obj.fingertips_y, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type hand_msg
    let len;
    let data = new hand_msg(null);
    // Deserialize message field [x]
    data.x = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [fingertips_x]
    data.fingertips_x = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [fingertips_y]
    data.fingertips_y = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.fingertips_x.length;
    length += 4 * object.fingertips_y.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'bigwork/hand_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '380b203d8077022bcbc89696459febd1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 x
    int32 y
    int32[] fingertips_x
    int32[] fingertips_y
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new hand_msg(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0
    }

    if (msg.fingertips_x !== undefined) {
      resolved.fingertips_x = msg.fingertips_x;
    }
    else {
      resolved.fingertips_x = []
    }

    if (msg.fingertips_y !== undefined) {
      resolved.fingertips_y = msg.fingertips_y;
    }
    else {
      resolved.fingertips_y = []
    }

    return resolved;
    }
};

module.exports = hand_msg;
