const axios = require('axios').default;

const sendRequest = async (options) => {
    try {
        const { data } = await axios(options);
        return { message: data,
                 status: 200};
    } catch (error) {
        return {
            message: JSON.parse(error.response.data.split('\'').join('\"')),
            status: error.response.status
        };
    }
}

module.exports = {
    sendRequest
}