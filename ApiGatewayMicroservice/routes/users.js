const Router = require("express").Router();

const { 
	sendRequest 
} = require("../http-client");


Router.post("/", async (req, res) => {
	const { 
		username,
		password,
		email
	} = req.body;

	console.info(`Forwarding request for add user ${username} on route ${process.env.USERS_SERVICE_API_ROUTE}`);


	const postUserRequest = {
		url: `authentication/api/users`,
		method: "POST",
		data: {
			username,
			password,
			email
		},
		'headers': {'Content-Type': 'application/json'}
	};

	const resId = await sendRequest(postUserRequest);

	res.json({ 
		resId 
	});
});

module.exports = Router;
