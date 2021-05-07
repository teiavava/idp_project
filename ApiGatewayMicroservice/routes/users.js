const Router = require("express").Router();

const {
	sendRequest
} = require("../http-client");

Router.get("/", async (req, res) => {
	console.info(`Forwarding request for get users`);
	console.info(`http://${process.env.USERS_SERVICE_API_ROUTE}`);

	const getUsersRequest = {
		url: `http://${process.env.USERS_SERVICE_API_ROUTE}`,
		headers: req.headers
	};

	const response = await sendRequest(getUsersRequest);

	res.status(response.status);
	res.json(response.message);
});

Router.get("/:id", async (req, res) => {
	const {
		id
	} = req.params;

	console.info(`Forwarding request for get user ${id}`);

	const getUserIdRequest = {
		url: `http://${process.env.USERS_SERVICE_API_ROUTE}/${id}`,
		headers: req.headers
	};

	const response = await sendRequest(getUserIdRequest);

	res.status(response.status);
	res.json(response.message);
});

Router.put("/:id", async (req, res) => {
	const { 
		username,
		password,
		email
	} = req.body;

	const { 
		id 
	} = req.params;

	console.info(`Forwarding request for update user ${id} ...`);

	const putUserRequest = {
		url: `http://${process.env.USERS_SERVICE_API_ROUTE}/${id}`,
		method: "PUT",
		data: {
			username,
			password,
			email
		},
		headers: req.headers
	};

	const response = await sendRequest(putUserRequest);

	res.status(response.status);
	res.json(response.message);
});

Router.post("/login", async (req, res) => {
	const {
		username,
		password
	} = req.body;

	console.info(`Forwarding request for login user ${username} ...`);

	const loginUserRequest = {
		url: `http://${process.env.USERS_SERVICE_API_ROUTE}/login`,
		method: "POST",
		data: {
			username,
			password
		}
	};

	const response = await sendRequest(loginUserRequest);

	res.status(response.status);
	res.json(response.message);
});

Router.post("/", async (req, res) => {
	const {
		username,
		password,
		email,
		role,
		cash
	} = req.body;

	console.info(`Forwarding request for add user ${username}`);

	const postUserRequest = {
		url: `http://${process.env.USERS_SERVICE_API_ROUTE}`,
		method: "POST",
		data: {
			username,
			password,
			email,
			role,
			cash
		},
		headers: {'Content-Type': 'application/json'}
	};

	const response = await sendRequest(postUserRequest);

	res.status(response.status);
	res.json(response.message);
});

Router.delete("/:id", async (req, res) => {
	const {
		id
	} = req.params;

	console.info(`Forwarding request for delete user ${id}`);

	const deleteUserRequest = {
		url: `http://${process.env.USERS_SERVICE_API_ROUTE}/${id}`,
		method: "DELETE",
		headers: req.headers
	};

	const response = await sendRequest(deleteUserRequest);

	res.status(response.status);
	res.json(response.message);
});

module.exports = Router;
