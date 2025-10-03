module.exports = function (req, res, next) {
    // sus
    // make session userId param to develop?
    // && req.ip == '127.0.0.1' ?
    if (req.session.userId === 'develop' && req.ip == '127.0.0.1') {
      return next();
    }
    res.status(403).send('Forbidden: Development access only');
  };