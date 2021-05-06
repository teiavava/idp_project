const Router = require("express").Router();

const {
	sendRequest
} = require("../http-client");

Router.get("/", async (req, res) => {
	console.info(`Forwarding request for get users`);

	const getUsersRequest = {
		url: `http://${process.env.USERS_SERVICE_API_ROUTE}`,
	};

	const users = await sendRequest(getUsersRequest);

	res.json(users);
});

Router.get("/:id", async (req, res) => {
	const {
		id
	} = req.params;

	console.info(`Forwarding request for get user ${id}`);

	const getUserIdRequest = {
		url: `http://${process.env.USERS_SERVICE_API_ROUTE}/${id}`,
	};

	const user = await sendRequest(getUserIdRequest);

	res.json(user);
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
	};

	const user = await sendRequest(putUserRequest);

	res.json(user);
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

	const user = await sendRequest(loginUserRequest);

	res.json(user);
});

Router.post("/", async (req, res) => {
	const { 
		username,
		password,
		email
	} = req.body;

	console.info(`Forwarding request for add user ${username}`);

	const postUserRequest = {
		url: `http://${process.env.USERS_SERVICE_API_ROUTE}`,
		method: "POST",
		data: {
			username,
			password,
			email
		},
		'headers': {'Content-Type': 'application/json'}
	};

	const user = await sendRequest(postUserRequest);

	res.json(user);
});

Router.delete("/:id", async (req, res) => {
	const {
		id
	} = req.params;

	console.info(`Forwarding request for delete user ${id}`);

	const deleteUserRequest = {
		url: `http://${process.env.USERS_SERVICE_API_ROUTE}/${id}`,
		method: "DELETE"
	};

	const resId = await sendRequest(deleteUserRequest);

	res.json({ 
		resId
	});
});

module.exports = Router;
