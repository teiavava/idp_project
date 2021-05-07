const Router = require('express').Router();

const UsersRoute = require('./users.js');
const AdminRoute = require('./admin.js');

Router.use('/users', UsersRoute);
Router.use('/admin', AdminRoute);

module.exports = Router;
