<template>
  <div class="cards">
    <alert :message="message" v-if="showMessage"></alert>

    <div v-for="(favorite, index) in favorites" :key="index">
      <div class="card mb-3 ">
        <div class="card-header">{{favorite.title}}</div>
        <div class="card-body secondary-text">
          <div> <span class="card-title">Category : </span> <span>{{favorite.category.type}}</span> </div>

        <div> <span class="card-title">Rank : </span> <span >{{favorite.rank}}</span> </div>
         <div><span class="card-title">Description : </span><span
          >{{favorite.description}}</span> </div>
          <div><span class="card-title">Other Info : </span><span
          >{{favorite.metaData}}</span> </div>
          <div><span class="card-title">Date Created : </span><span
          >{{formatDate(favorite.createdAt)}}</span> </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import Alert from "./Alert.vue";
const BASE_URL = process.env.VUE_APP_URL;
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
      let headers = {
        Authorization: `Bearer ${this.token}`
      };
      axios
        .get(path, {
          headers
        })
        .then(response => {
          if(response.data.data.length === 0){
            this.message = 'You don\'t have any favorite things yet';
            this.showMessage = true
          }
          this.favorites = response.data.data;
        })
        .catch(error => {
           this.message = error.response.data.message;
          this.showMessage = true;
            this.variant = 'warning'
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
  .card-header{
    color: #42b983;
  }
  .card-title{
    text-shadow: 1px 1px yellow;
    font-weight: bold;
  }


</style>
