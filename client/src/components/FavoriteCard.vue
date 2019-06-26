<template>
  <div class="cards">
    <alert :message="message" v-if="showMessage"></alert>

    <div v-for="(favorite, index) in favorites" :key="index">
      <div class="card mb-3 ">
        <div class="card-header">Header</div>
        <div class="card-body secondary-text">
          <h5 class="card-title">{{favorite.title}}</h5>
          <p
            class="card-text"
          >{{favorite.description}}</p>
          <p
            class="card-text"
          >{{favorite.metaData}}</p>
          <p
            class="card-text"
          >{{formatDate(favorite.createdAt)}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import Alert from "./Alert.vue";
const BASE_URL = "http://127.0.0.1:5000/api/v1";
export default {
  // name: 'Favorite',
  data() {
    return {
      favorites: [],
      token: localStorage.getItem("token"),
      username: localStorage.getItem("user"),
      message: '',
      showMessage: false
    };
  },
  methods: {
    getFavorite() {
      const path = `${BASE_URL}/favorites`;
      var headers = {
        Authorization: `Bearer ${this.token}`
      };
      // console.log('===>', headers)
      axios
        .get(path, {
          headers
        })
        .then(response => {
          console.log('=====?///', response.data.data)
          if(response.data.data.length === 0){
            this.message = 'You don\'t have any favorite things yet'
            this.showMessage = true
          }
          this.favorites = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
     formatDate(date) {
         return moment(String(date)).format('hh:mm a MM/D/YY');
     }
  },
   components: {
    alert: Alert,
  },
  created() {
    this.getFavorite();
  }
};
</script>

<style scoped>
.mb-3 {
  margin: 25px 10px;
  min-width: 20rem;
  min-height: 18rem
}
.cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
}
.card {
  box-shadow: 2px 2px 21px rgba(0, 0, 0, 0.08);
}
</style>
