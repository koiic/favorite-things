<template>
<div class="container">
    <div class="row">
      <div class="col-sm-10">
        <br><br>
          <button type="button" class="btn btn-success btn-sm" v-b-modal.favorite-modal>Logs</button>

        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>


        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">s/n</th>
              <th scope="col">Action</th>
              <th scope="col">Description</th>
              <th scope="col">date</th>
              <!-- <th scope="col">meta data</th>
              <th scope="col">rank</th> -->
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(audit, index) in audits" :key="index">
              <td>{{audit.id}}</td>
              <td>{{audit.action}}</td>
              <td>{{audit.description}}</td>
              <td>{{formatDate(audit.createdAt)}}</td>
              <td>
                <!-- <div class="btn-group" role="group"> -->
                  <!-- <button type="button" class="btn btn-warning btn-sm"  v-b-modal.favorite-update-modal
        @click="editFavorite(favorite)">Update</button>
                  <button type="button" class="btn btn-danger btn-sm" @click="onDeleteFavorite(favorite)">Delete</button> -->
                <!-- </div> -->
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import moment from 'moment'
import { Script } from 'vm';
const BASE_URL = 'http://127.0.0.1:5000/api/v1'
export default {
  // name: 'Favorite',
  data() {
    return {
      audits: [],
      message: '',
      showMessage: false,
      token: localStorage.getItem('token'),
      username: localStorage.getItem('user')
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getAudits(){
      const path = `${BASE_URL}/audits`;
       var headers = {
        'Authorization': `Bearer ${this.token}`
      }
      // console.log('===>', headers)
      axios.get(path, {headers}).then((response) => {
        console.log('===>>>>', response.data.data[0])
        this.audits = response.data.data;
        this.message = response.data.message
        this.showMessage = True
      })
        .catch((error) => {
          console.log(error);
        });
    },
     formatDate(date) {
         return moment(String(date)).format('hh:mm a DD/MM/YY');
     }
  },
  created(){
    this.getAudits()
  }
}

</script>
