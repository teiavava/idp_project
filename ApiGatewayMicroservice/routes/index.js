const Router = require('express').Router();

const UsersRoute = require('./users.js');

Router.use('/users', UsersRoute);

module.exports = Router;
