<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <br />
        <br />
        <button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.favorite-modal
        >Add Favorite Thing</button>

        <hr />
        <br />
        <br />
        <div class="linkcontainer">
          <router-link :to="{ name: 'Favorite' }">Favorites</router-link>
          <router-link :to="{ name: 'Category' }">Categories</router-link>
        </div>

        <br />
        <br />
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
                  <button
                    type="button"
                    class="btn btn-warning btn-sm"
                    v-b-modal.favorite-update-modal
                    @click="editFavorite(favorite)"
                  >Update</button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteFavorite(favorite)"
                  >Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      v-model="addFavoriteModal"
      id="favorite-modal"
      title="Add New favorite thing"
      hide-footer
    >
      <b-alert v-model="addFavoriteModalMessage" :variant="variant" show dismissible>{{ message }}</b-alert>
      <b-form @submit="onSubmit" class="w-100">
        <b-form-group
          id="form-title-group"
          label="What is your favorite thing title:"
          label-for="form-title-input"
        >
          <b-form-input id="form-title-input" type="text" v-model="addFavoriteForm.title" required></b-form-input>
        </b-form-group>
        <b-form-group
          id="form-description-group"
          label="Description(optional):"
          label-for="form-description-input"
        >
          <b-form-textarea
            id="form-description-input"
            type="text"
            v-model="addFavoriteForm.description"
          ></b-form-textarea>
        </b-form-group>
        <div></div>
            <b-form-group id="form-metadata-group"
                      label="Any other Info(Optional):"
                      label-for="form-metadata-input">
            <b-form-input id="form-metadata-input"
                          type="text"
                          v-model="addFavoriteForm.metaData"
                          placeholder="">
            </b-form-input>
      </b-form-group>
        <b-form-group
          id="form-category-group"
          label="Select a category"
          label-for="form-category-input"
        >
          <b-select v-model="addFavoriteForm.categoryId">
            <option :value="null" selected="selected">select category</option>
            <option v-for="category in categories" v-bind:value="category.id">{{ category.type }}</option>
          </b-select>
          <b-button variant="link" class="category" v-b-modal.category-modal>add category</b-button>
        </b-form-group>
        <b-form-group
          id="form-rank-group"
          label="What rank do you want to place it"
          label-for="form-rank-input"
        >
          <b-form-input
            id="form-rank-input"
            type="number"
            min="1"
            max="100"
            v-model="addFavoriteForm.rank"
            required
          ></b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="success">Add</b-button>
          <b-button type="reset" variant="warning">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal
      v-model="editFavoriteModal"
      id="favorite-update-modal"
      title="Update favorite things"
      hide-footer
    >
      <b-alert v-model="showMessage" :variant="variant" show dismissible>{{ message }}</b-alert>

      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group" label="Favorite Title:" label-for="form-title-edit-input">
          <b-form-input
            id="form-title-edit-input"
            type="text"
            v-model="editFavoriteForm.title"
            required
            placeholder="Enter title"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="form-description-edit-group"
          label="Description:"
          label-for="form-description-edit-input"
        >
          <b-form-textarea
            id="form-description-edit-input"
            type="text"
            v-model="editFavoriteForm.description"
            placeholder="Enter Description"
          ></b-form-textarea>
        </b-form-group>
          <b-form-group id="form-metadata-edit-group"
                      label="Other Info:"
                      label-for="form-metadata-edit-input">
            <b-form-input id="form-metadata-edit-input"
                          type="text"
                          v-model="editFavoriteForm.metaData"
                          placeholder="">
            </b-form-input>
      </b-form-group>
        <b-form-group id="form-rank-edit-group" label="Rank:" label-for="form-rank-edit-input">
          <b-form-input
            id="form-rank-edit-input"
            type="number"
            v-model="editFavoriteForm.rank"
            required
            placeholder
          ></b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="success">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="addCategoryModal" id="category-modal" title="New Category" hide-footer>
    <b-alert v-model="addFavoriteModalMessage" :variant="variant" show dismissible>{{ message }}</b-alert>

      <b-form @submit="onSubmitCategory" class="w-100">
        <b-form-group id="form-type-group" label="Name:" label-for="form-type-input">
          <b-form-input
            id="form-type-input"
            type="text"
            v-model="addCategoryForm.type"
            required
            placeholder="Enter category"
          ></b-form-input>
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="success">add</b-button>
          <b-button type="reset" variant="danger">reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>


<script>
import axios from "axios";
import moment from "moment";
import Alert from "./Alert.vue";
import Swal from "sweetalert2";
const BASE_URL = process.env.VUE_APP_URL;

export default {
  data() {
    return {
      favorites: [],
      addFavoriteForm: {
        title: "",
        description: "",
        metaData: "",
        categoryId: "",
        rank: ""
      },
      editFavoriteForm: {
        id: "",
        title: "",
        description: "",
        metaData: "",
        categoryId: "",
        rank: ""
      },
      addCategoryForm: {
        type: ""
      },
      message: "",
      variant: "",
      showMessage: false,
      categories: [],
      errors: {},
      token: localStorage.getItem("token"),
      username: localStorage.getItem("user"),
      addFavoriteModal: false,
      addFavoriteModalMessage: false,
      editFavoriteModal: false,
    };
  },
  components: {
    alert: Alert
  },
  methods: {
    getFavorite() {
      const path = `${BASE_URL}/favorites`;
      var headers = {
        Authorization: `Bearer ${this.token}`
      };
      axios
        .get(path, { headers })
        .then(response => {
          this.favorites = response.data.data;
        })
        .catch(error => {
          this.message = error.response.data.message;
          this.showMessage = true;
          this.variant = "warning";
        });
    },

    getCategories() {
      const path = `${BASE_URL}/categories`;
      axios
        .get(path)
        .then(response => {
          this.categories = response.data.data;
        })
        .catch(error => {
          this.message = error.response.data.message;
          this.showMessage = true;
          this.variant = "warning";
        });
    },

    addCategory(payload) {
      const path = `${BASE_URL}/categories`;
      var headers = {
        Authorization: `Bearer ${this.token}`
      };
      axios
        .post(path, payload, { headers })
        .then(response => {
          this.addFavoriteModalMessage = true;
          this.message = response.data.message;
          this.variant = "success";
          this.$refs.addCategoryModal.hide();
          this.getCategories();
        })
        .catch(error => {
          this.message = error.response.data.message;
          this.addFavoriteModalMessage = true;
          this.variant = "warning";
          this.$refs.addCategoryModal.hide();
        });
    },

    addFavorite(payload) {
      if (payload.title.trim() === "") {
        this.message = "Title Field Cannot be empty";
        this.addFavoriteModalMessage = true;
        this.variant = "danger";
        return;
      }
      if (payload.description && payload.description.length < 10) {
        this.message = "Description must be at least 10 characters";
        this.addFavoriteModalMessage = true;
        this.variant = "danger";
        return;
      }
      const path = `${BASE_URL}/favorites`;
      let headers = {
        Authorization: `Bearer ${this.token}`
      };
      axios
        .post(path, payload, { headers: headers })
        .then(response => {
         Swal.fire({
            position: "top-end",
            type: "success",
            title: response.data.message,
            showConfirmButton: false,
            timer: 1500
          });
          this.addFavoriteModal = false;
          this.getFavorite();
          this.initForm();

        })
        .catch(error => {
          error = error.response.data.errors;
          let newObj = Object.values(error);
          this.message = newObj[0][0];
          this.addFavoriteModalMessage = true;
          this.variant = "warning";
        });
    },

    editFavorite(favorite) {
      this.editFavoriteForm = favorite;
    },
    updateFavorite(payload, favorite_id) {
      var headers = {
        Authorization: `Bearer ${this.token}`
      };
      if (payload.description && payload.description.length < 10) {
        this.message = "Description must be at least 10 characters";
        this.showMessage = true;
        this.variant = "danger";
        return;
      }
      const path = `${BASE_URL}/favorites/${favorite_id}`;
      axios
        .patch(path, payload, { headers })
        .then(response => {
          Swal.fire({
            position: "top-end",
            type: "success",
            title: response.data.message,
            showConfirmButton: false,
            timer: 1500
          });
          this.editFavoriteModal = false;
          this.getFavorite();
          this.showMessage = true;
          this.message = response.data.message;
          this.variant = "success";
          this.initForm();

        })
        .catch(error => {
          // eslint-disable-next-line
          this.message = error.response.data.message;
          this.showMessage = true;
          this.variant = "warning";
          this.getFavorite();
        });
    },

    initForm() {
      (this.addFavoriteForm.title = ""),
        (this.addFavoriteForm.description = ""),
        (this.addFavoriteForm.category = ""),
        (this.addFavoriteForm.metaData = ""),
        (this.editFavoriteForm.title = ""),
        (this.editFavoriteForm.description = ""),
        (this.editFavoriteForm.category = ""),
        (this.editFavoriteForm.metaData = ""),
        (this.addCategoryForm.type = "");
    },

    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        title: this.addFavoriteForm.title,
        description: this.addFavoriteForm.description,
        categoryId: this.addFavoriteForm.categoryId,
        metaData: this.addFavoriteForm.metaData,
        rank: this.addFavoriteForm.rank
      };
      this.addFavorite(payload);
    },

    onSubmitUpdate(evt) {
      evt.preventDefault();
      const payload = {
        title: this.editFavoriteForm.title,
        description: this.editFavoriteForm.description,
        categoryId: this.editFavoriteForm.categoryId,
        metaData: this.editFavoriteForm.metaData,
        rank: this.editFavoriteForm.rank
      };
      this.updateFavorite(payload, this.editFavoriteForm.id);
    },

    onResetUpdate(evt) {
      evt.preventDefault();
      this.editFavoriteModal = false;
      this.initForm();
      this.getFavorite();
    },

    deleteFavorite(favorite_id) {
      const path = `${BASE_URL}/favorites/${favorite_id}`;
      var headers = {
        Authorization: `Bearer ${this.token}`
      };
      axios
        .delete(path, { headers })
        .then(response => {
          if (response.data.status == "success") {
            Swal.fire("Deleted!", "Favorite has been deleted.", "success");
            this.getFavorite();
            this.variant = "success";
            this.message = response.data.message;
            this.showMessage = true;
          }
        })
        .catch(error => {
          // eslint-disable-next-line
          this.message = error.response.data.message;
          this.showMessage = true;
          this.variant = "warning";
          this.getFavorite();
        });
    },
    onDeleteFavorite(favorite) {
      Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
      }).then(result => {
        if (result.value) {
          this.deleteFavorite(favorite.id);
        }
      });
    },

    onSubmitCategory(evt) {
      evt.preventDefault();
      this.$refs.addCategoryModal.hide();
      const payload = {
        type: this.addCategoryForm.type
      };
      this.addCategory(payload);
      this.initForm();
    },
    formatDate(date) {
      return moment(String(date)).format("hh:mm a MM/D/YY");
    },
    addMetadata(key, value) {
      let newMetaData = {};
      newMetaData[key] = value;
      return newMetaData;
    }
  },
  watch: {
    addFavoriteModal (value) {
      if (!value) this.addFavoriteModalMessage = false;
    },
    editFavoriteModal (value) {
      if (!value) this.showMessage = false;
    },
  },
  created() {
    this.getFavorite();
    this.getCategories();
  },
  updated() {}
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
.meta-data-form {
  display: flex;
  justify-content: space-between;
}
.meta-data-form input {
  width: 48%;
}
</style>
