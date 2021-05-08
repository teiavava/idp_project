const Router = require("express").Router();

const {
	sendRequest
} = require("../http-client");

Router.get("/", async (req, res) => {
	console.info(`Forwarding request for get phones`);

	const getPhonesRequest = {
		url: `http://${process.env.PHONES_SERVICE_API_ROUTE}`,
		headers: req.headers
	};

	const response = await sendRequest(getPhonesRequest);

	res.status(response.status);
	res.json(response.message);
});

Router.get("/:id", async (req, res) => {
	const {
		id
	} = req.params;

	console.info(`Forwarding request for get phone ${id}`);

	const getPhoneIdRequest = {
		url: `http://${process.env.PHONES_SERVICE_API_ROUTE}/${id}`,
		headers: req.headers
	};

	const response = await sendRequest(getPhoneIdRequest);

	res.status(response.status);
	res.json(response.message);
});

Router.put("/:id", async (req, res) => {
	const {
		username
	} = req.body;

	console.info(`Forwarding request for buy phone`);

	const { 
		id 
	} = req.params;

	const postPhoneRequest = {
		url: `http://${process.env.PHONES_SERVICE_API_ROUTE}/buy/${id}`,
		method: "PUT",
		data: {
			username
		},
		headers: req.headers
	};

	const response = await sendRequest(postPhoneRequest);

	res.status(response.status);
	res.json(response.message);
});

module.exports = Router;
