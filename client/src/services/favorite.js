import axios from 'axios';

// eslint-disable-next-line import/prefer-default-export
const getFavorite = () => {
  const path = 'http://127.0.0.1:5000/api/v1/favorite';
  console.log('====>>', path);
  axios.get(path).then((response) => {
    return response.data.data;
  })
    .catch((error) => {
      console.log(error);
    });
};

export default getFavorite;
