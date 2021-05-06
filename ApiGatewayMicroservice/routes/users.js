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
		url: `authentication/api`,
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

// curl --location --request POST 'authentication/api/users' \
// --header 'Content-Type: application/json' \
// --data-raw '{
//     "username": "adaaamin",
//     "password": "123321123",
//     "email": "aaaa@gmail.com"
// }'


// curl --location --request POST 'http://io/api/users' --header 'Content-Type: application/json' --data-raw '{"username": "admin","password": "123321123","email": "admin@gmail.com"}'

// import requests

// url = "http://io/api/users"

// payload="{\r\n    \"username\": \"admin\",\r\n    \"password\": \"123321123\",\r\n    \"email\": \"admin@gmail.com\"\r\n}"
// headers = {
//   'Content-Type': 'application/json'
// }

// response = requests.request("POST", url, headers=headers, data=payload)

// print(response.text)
