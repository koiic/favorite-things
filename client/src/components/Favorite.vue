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
          <router-link :to="{ name: 'Category' }">Categories</router-link>
        </div>


        <br><br>
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
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm"  v-b-modal.favorite-update-modal
        @click="editFavorite(favorite)">Update</button>
                  <button type="button" class="btn btn-danger btn-sm" @click="onDeleteFavorite(favorite)">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addFavoriteModal"
         id="favorite-modal"
         title="Add New favorite thing"
         hide-footer>
    <b-form  @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-title-group"
                  label="Title:"
                  label-for="form-title-input">
        <b-form-input id="form-title-input"
                      type="text"
                      v-model="addFavoriteForm.title"
                      required
                      placeholder="Enter title">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-description-group"
                    label="Description:"
                    label-for="form-description-input">
          <b-form-input id="form-description-input"
                        type="text"
                        v-model="addFavoriteForm.description"
                        placeholder="Enter Description">
          </b-form-input>
      </b-form-group>
      <b-form-group id="form-metadata-group"
                    label="MetaData:"
                    label-for="form-metadata-input">
          <b-form-input id="form-metadata-input"
                        type="text"
                        v-model="addFavoriteForm.metaData"
                        placeholder="meta-data should be in key:value pair">
          </b-form-input>
      </b-form-group>
      <b-form-group id="form-category-group"
                    label="Category:"
                    label-for="form-category-input">
          <b-select v-model="addFavoriteForm.categoryId">
          <option :value="null" selected="selected">select category</option>
          <option v-for="category in categories" v-bind:value="category.id">
            {{ category.type }}
          </option>
        </b-select>
        <span class="category" v-b-modal.category-modal>Add Category</span>
      </b-form-group>
      <b-form-group id="form-rank-group"
                    label="Rank:"
                    label-for="form-rank-input">
          <b-form-input id="form-rank-input"
                       type="number" min="1" max="100"
                        v-model="addFavoriteForm.rank"
                        required
                        placeholder="Rank">
          </b-form-input>
      </b-form-group>
      <b-button-group>
          <b-button type="submit" variant="success">Save Favorite</b-button>
          <b-button type="reset" variant="warning">Reset</b-button>
      </b-button-group>
    </b-form>
  </b-modal>
   <b-modal ref="editFavoriteModal"
         id="favorite-update-modal"
         title="Update favorite things"
         hide-footer>
    <b-form  @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    <b-form-group id="form-title-edit-group"
                  label="Title:"
                  label-for="form-title-edit-input">
        <b-form-input id="form-title-eidt-input"
                      type="text"
                      v-model="editFavoriteForm.title"
                      required
                      placeholder="Enter title">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-description-edit-group"
                    label="Description:"
                    label-for="form-description-eidt-input">
          <b-form-input id="form-description-edit-input"
                        type="text"
                        v-model="editFavoriteForm.description"
                        required
                        placeholder="Enter Description">
          </b-form-input>
      </b-form-group>
      <b-form-group id="form-metadata-edit-group"
                  label="MetaData:"
                  label-for="form-metadata-edit-input">
        <b-form-input id="form-metadata-edit-input"
                      type="text"
                      v-model="editFavoriteForm.metaData"
                      required
                      placeholder="Enter Metadata">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-category-edit-group"
            label="Category:"
            label-for="form-category-edit-input">
        <b-select v-model="editFavoriteForm.categoryId">
          <option v-for="category in categories" v-bind:value="category.id">
            {{ category.type }}
          </option>
        </b-select>
      </b-form-group>
       <b-form-group id="form-rank-edit-group"
                  label="Rank:"
                  label-for="form-rank-edit-input">
        <b-form-input id="form-rank-edit-input"
                      type="number"
                      v-model="editFavoriteForm.rank"
                      required
                      placeholder="">
        </b-form-input>
      </b-form-group>
      <b-button-group>
          <b-button type="submit" variant="success">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
      </b-button-group>
    </b-form>
  </b-modal>
     <b-modal ref="addCategoryModal" id="category-modal" title="New Category" hide-footer>
      <b-form @submit="onSubmitCategory" @reset="onReset" class="w-100">
        <b-form-group id="form-type-group" label="Name:" label-for="form-type-input">
          <b-form-input id="form-type-input" type="text" v-model="addCategoryForm.type" required placeholder="Enter category">
          </b-form-input>
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="success">Create</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>


<script>
import axios from 'axios';
import moment from 'moment'
import Alert from './Alert.vue';
import Swal from 'sweetalert2';
const BASE_URL = 'http://127.0.0.1:5000/api/v1'
export default {
  // name: 'Favorite',
  data() {
    return {
      favorites: [],
      addFavoriteForm : {
        title: '',
        description: '',
        metaData: '',
        categoryId: '',
        rank: ''
      },
      editFavoriteForm : {
        id: '',
        title: '',
        description: '',
        metaData: '',
        categoryId: '',
        rank:''
      },
      addCategoryForm: {
        type: ''
      },
      message: '',
      showMessage: false,
      categories: [],
      token: localStorage.getItem('token'),
      username: localStorage.getItem('user')
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getFavorite(){
      const path = `${BASE_URL}/favorites`;
       var headers = {
        'Authorization': `Bearer ${this.token}`
      }
      axios.get(path, {headers}).then((response) => {
         if(response.data.data.length === 0){
            this.message = 'You don\'t have any favorite things yet'
            this.showMessage = true
          }
        this.favorites = response.data.data;
      })
        .catch((error) => {
          console.log(' i got error', error)

          this.message = error
          this.showMessage = true
        });
    },

     getCategories(){
      const path = `${BASE_URL}/categories`;
      axios.get(path).then((response) => {
        this.categories = response.data.data;
      })
        .catch((error) => {
          this.message = error
        });
    },

    addCategory(payload){
      const path = `${BASE_URL}/categories`;
       var headers = {
        'Authorization': `Bearer ${this.token}`
      }
      axios.post(path, payload, {headers}).then((response) => {
        console.log('====>>',response)
        this.showMessage = true
        this.message = response.data.message
        this.$refs.addCategoryModal.hide()
        this.getCategories()

      })
      .catch((error) => {
        this.message = response.data.message
        this.$refs.addCategoryModal.hide()

      })

    },

    addFavorite(payload){
      const path = `${BASE_URL}/favorites`;
      var headers = {
        'Authorization': `Bearer ${this.token}`
      }
      axios.post(path, payload,  {'headers':headers},).then((response) => {
        console.log('====>>',response)
        this.getFavorite()
        this.showMessage = true
        this.message = response.data.message

      })
      .catch((error) => {
        this.message = response.data.message
        this.getFavorite();
      })

    },

    editFavorite(favorite) {
      this.editFavoriteForm = favorite;
    },
    updateFavorite(payload, favorite_id){
      var headers = {
        'Authorization': `Bearer ${this.token}`
      }
    const path = `${BASE_URL}/favorites/${favorite_id}`;
    axios.patch(path, payload, {headers})
      .then((response) => {
        Swal.fire({
          position: 'top-end',
          type: 'success',
          title: response.data.message,
          showConfirmButton: false,
          timer: 1500
        })
        this.getFavorite();
        this.showMessage = true
        this.message = response.data.message
      })
      .catch((error) => {
        // eslint-disable-next-line
        this.getFavorite();
      });
    },

    initForm() {
        this.addFavoriteForm.title = '',
        this.addFavoriteForm.description = '',
        this.addFavoriteForm.category = '',
        this.addFavoriteForm.metaData = '',
         this.editFavoriteForm.title = '',
        this.editFavoriteForm.description = '',
        this.editFavoriteForm.category = '',
        this.editFavoriteForm.metaData = '',
        this.addCategoryForm.type = ''
    },

    onSubmit(evt){
      evt.preventDefault();
      this.$refs.addFavoriteModal.hide()
      const payload = {
        title: this.addFavoriteForm.title,
        description: this.addFavoriteForm.description,
        categoryId: this.addFavoriteForm.categoryId,
        metaData: this.addFavoriteForm.metaData,
        rank: this.addFavoriteForm.rank
      }
      this.addFavorite(payload);
      this.initForm();
    },

    onReset(evt){
      evt.preventDefault();
      this.$refs.addFavoriteModal.hide();
      this.initForm();
    },

    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editFavoriteModal.hide();
      const payload = {
        title: this.editFavoriteForm.title,
        description: this.editFavoriteForm.description,
        categoryId: this.editFavoriteForm.categoryId,
        metaData: this.editFavoriteForm.metaData,
        rank: this.editFavoriteForm.rank
      }
      this.updateFavorite(payload, this.editFavoriteForm.id);
      this.initForm();
    },

    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editFavoriteModal.hide();
      this.initForm();
      this.getFavorite();
    },

    deleteFavorite(favorite_id) {
      const path = `${BASE_URL}/favorites/${favorite_id}`;
      var headers = {
        'Authorization': `Bearer ${this.token}`
      }
      axios.delete(path, {headers})
        .then((response) => {
          if(response.data.status == 'success'){
            Swal.fire(
            'Deleted!',
            'Favorite has been deleted.',
            'success'
            )
            this.getFavorite();
            this.message = response.data.message;
            this.showMessage = true;
          }

        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getFavorite();
        });
    },
    onDeleteFavorite(favorite) {
      Swal.fire({
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      type: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
      if (result.value) {
        this.deleteFavorite(favorite.id)
      }
    })
    },

    onSubmitCategory(evt) {
      evt.preventDefault();
      this.$refs.addCategoryModal.hide()
      const payload = {
        type: this.addCategoryForm.type,
      }
      this.addCategory(payload);
      this.initForm();

    },
    formatDate(date) {
         return moment(String(date)).format('hh:mm a MM/D/YY');
     }
  },
   created() {
    this.getFavorite();
    this.getCategories();
  },
   updated() {
  },
};
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
</style>
