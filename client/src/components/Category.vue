<template>
   <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <br><br>
          <button type="button" class="btn btn-success btn-sm" v-b-modal.favorite-modal>Add Favorite Thing</button>

        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <div class="linkcontainer">
           <router-link :to="{ name: 'Favorite' }">Favorites</router-link>
          <router-link :to="{ name: 'Dashboard' }">Categories</router-link>
        </div>


        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">s/n</th>
              <th scope="col">Name</th>
              <th scope="col">Favorite</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(category, index) in categories" :key="index">
              <td>{{category.category_id}}</td>
              <td>{{category.type}}</td>
              <!-- <td>{{formatDate(category)}}</td> -->
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm"  v-b-modal.favorite-view-modal
        @click="viewFavorites(category.favorite_things)">View Favorites</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
     <b-modal ref="viewFavoriteModal" id="favorite-view-modal" size="lg" title="Favorites" class="modal-lg" hide-footer>
          <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Category</th>
              <th scope="col">Description</th>
              <th scope="col">created date</th>
              <th scope="col">more info</th>
              <th scope="col">rank</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(favorite, index) in favorites" :key="index">
              <td>{{favorite.title}}</td>
              <td>{{favorite.category.type}}</td>
              <td>{{favorite.description}}</td>
              <td>{{formatDate(favorite.createdAt)}}</td>
              <td>{{favorite.metaData}}</td>
               <td>{{favorite.rank}}</td>
              <td>
              </td>
            </tr>
          </tbody>
        </table>
    </b-modal>
   </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment'
import FavoriteCard from './FavoriteCard';
import Alert from './Alert'
import Swal from 'sweetalert2';
const BASE_URL = 'http://127.0.0.1:5000/api/v1'
export default {
  data() {
    return {
      message: '',
      showMessage: false,
      categories: [],
      favorites: [],
      token: localStorage.getItem('token'),
      username: localStorage.getItem('user')

    }
  },
  methods : {
     getCategoryFavorite(){
      const path = `${BASE_URL}/category/favorites`;
       var headers = {
        'Authorization': `Bearer ${this.token}`
      }
      axios.get(path, {headers}).then((response) => {
        this.categories = response.data.data;
      })
        .catch((error) => {
          console.log(' i got error', error)
          this.message = error
          this.showMessage = true
        });
    },
    viewFavorites(favorites){
      this.favorites = favorites
    },
    formatDate(date) {
         return moment(String(date)).format('hh:mm a MM/D/YY');
     }
  },
   components: {
    alert: Alert,
  },
  created(){
    this.getCategoryFavorite()
  }


}
</script>
<style scoped>
  .category {
    float: right;

  }
  .linkcontainer {
    display: flex;
    width: 200px;
  }
  .linkcontainer a {
      flex: 1;
    }
  .bmodal {
  width: 750px;
  margin: auto;
}
</style>


