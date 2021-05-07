const Router = require("express").Router();

const {
	sendRequest
} = require("../http-client");

Router.get("/", async (req, res) => {
	console.info(`Forwarding request for get phones`);
	console.info(`http://${process.env.ADMIN_SERVICE_API_ROUTE}`);

	const getPhonesRequest = {
		url: `http://${process.env.ADMIN_SERVICE_API_ROUTE}`,
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
		url: `http://${process.env.ADMIN_SERVICE_API_ROUTE}/${id}`,
		headers: req.headers
	};

	const response = await sendRequest(getPhoneIdRequest);

	res.status(response.status);
	res.json(response.message);
});

Router.put("/:id", async (req, res) => {
	const { 
		name,
		price,
		stock
	} = req.body;

	const { 
		id 
	} = req.params;

	console.info(`Forwarding request for update phone ${id} ...`);

	const putPhoneRequest = {
		url: `http://${process.env.ADMIN_SERVICE_API_ROUTE}/${id}`,
		method: "PUT",
		data: {
			name,
			price,
			stock
		},
		headers: req.headers
	};

	const response = await sendRequest(putPhoneRequest);

	res.status(response.status);
	res.json(response.message);
});

Router.post("/", async (req, res) => {
	const {
		name,
		price,
		stock
	} = req.body;

	console.info(`Forwarding request for add phone ${name}`);

	const postPhoneRequest = {
		url: `http://${process.env.ADMIN_SERVICE_API_ROUTE}`,
		method: "POST",
		data: {
			name,
			price,
			stock
		},
		headers: req.headers
	};

	const response = await sendRequest(postPhoneRequest);

	res.status(response.status);
	res.json(response.message);
});

Router.delete("/:id", async (req, res) => {
	const {
		id
	} = req.params;

	console.info(`Forwarding request for delete phone ${id}`);

	const deletePhoneRequest = {
		url: `http://${process.env.ADMIN_SERVICE_API_ROUTE}/${id}`,
		method: "DELETE",
		headers: req.headers
	};

	const response = await sendRequest(deletePhoneRequest);

	res.status(response.status);
	res.json(response.message);
});

module.exports = Router;
