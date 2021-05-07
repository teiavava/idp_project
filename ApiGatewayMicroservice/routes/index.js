const Router = require('express').Router();

const UsersRoute = require('./users.js');
const AdminRoute = require('./admin.js');
const PhonesRoute = require('./phones.js');

Router.use('/users', UsersRoute);
Router.use('/admin', AdminRoute);
Router.use('/phones', PhonesRoute);

module.exports = Router;
