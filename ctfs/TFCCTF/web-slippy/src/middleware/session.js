const crypto = require('crypto');
const path = require('path');
const fs = require('fs');

const USER_ID_REGEX = /^[a-f0-9]{16}$/;

// true if develop
function isValidUserId(id) {
  return id === 'develop' || USER_ID_REGEX.test(id);
}

module.exports = function (req, res, next) {
    // if not valid make up 8 hex bytes
    if (!isValidUserId(req.session.userId)) {
      req.session.userId = crypto.randomBytes(8).toString('hex');
    }
  
    // ../uploads/develop ?
    const userDir = path.join(__dirname, '../uploads', req.session.userId);
    fs.mkdirSync(userDir, { recursive: true });
  
    next();
  };