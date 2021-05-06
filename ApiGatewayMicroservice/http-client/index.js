const axios = require('axios').default;

const sendRequest = async (config) => {
    var axios = require('axios');
    var data = JSON.stringify({"username":"admin","password":"123321123","email":"admin@gmail.com"});

    var config = {
    method: 'post',
    url: 'authentication/api',
    headers: { 
            "content-type": "application/json",
            "Accept": "application/json"
    },
    data : data
    };

    const ret = axios(config)
    .then(function (response) {
    console.log(JSON.stringify(response.data));
    })
    .catch(function (error) {
    console.log(error);
    });

    return ret;
    // try {
    //     const { data } = await axios(options);
    //     return data;
    // } catch (error) {
    //     throw error;
    // }
}

module.exports = {
    sendRequest
}

const axios = require('axios');

async function makeGetRequest() {

    let payload = { name: 'John Doe', occupation: 'gardener' };

    let res = await axios.post('http://httpbin.org/post', payload);

    let data = res.data;
    console.log(data);
}

makeGetRequest();


const axios = require('axios');

async function makeGetRequest() {

    let payload = {
        "username": "admin",
        "id": "5c19a5a2fcd64e2a9401225b61596b3d",
        "password": "123321123",
        "email": "teia_vava@yahoo.com",
        "firstName": "Teiaaaa"
    };

    let res = await axios.post('http://52.29.155.35/api/users', payload);

    let data = res.data;
    console.log(data);
}

makeGetRequest();