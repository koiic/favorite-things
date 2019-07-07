<template>
<div class="hello">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="/">Favority <span class="sr-only">(current)</span></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <!-- <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li> -->
        <li class="nav-item">
          <!-- <a class="nav-link" href="#">View</a> -->
          <router-link v-if="auth" :to="{ name: 'Favorite' }">Dashboard</router-link>

        </li>
        <li class="nav-item">
          <!-- <a class="nav-link" href="#">Dashboard</a> -->
          <router-link v-if="auth" :to="{ name: 'FavoriteCard' }">Favorite</router-link>

        </li>

      </ul>
       <li class="nav-item">
       <router-link v-if="auth" :to="{ name: 'Audit' }">View Logs</router-link>

      </li>

      <li class="nav-item">
        <button type="button" v-if="!auth" class="btn btn-success btn-sm" v-b-modal.login-modal>Login</button>
        <button type="button" v-if="auth"  @click="logOut()" class="btn btn-success btn-sm">Logout</button>
      </li>

       <li class="nav-item">
        <button type="button" v-if="!auth" class="btn btn-success btn-sm" v-b-modal.signup-modal>SignUp</button>
        <h5 v-if='auth'>{{username.split(' ')[0]}}</h5>
      </li>

    </div>
    <b-modal ref="addLoginModal" id="login-modal" title="User Authentication" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-email-group" label="Email:" label-for="form-email-input">
          <b-form-input id="form-email-input" type="text" v-model="loginForm.email" required placeholder="Enter email">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-password-group" label="Password:" label-for="form-password-input">
          <b-form-input id="form-password-input" type="password" v-model="loginForm.password" required placeholder="Enter Password">
          </b-form-input>
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="success">Login</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="addSignupModal" id="signup-modal" title="User Registration" hide-footer>
      <b-form @submit="onSubmitRegister" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group" label="FullName:" label-for="form-name-input">
          <b-form-input id="form-name-input" type="text" v-model="signupForm.name" required placeholder="Enter Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-email-group" label="Email:" label-for="form-email-input">
          <b-form-input id="form-email-input" type="text" v-model="signupForm.email" required placeholder="Enter email">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-password-group" label="Password:" label-for="form-password-input">
          <b-form-input id="form-password-input" type="password" v-model="signupForm.password" required placeholder="Enter Password">
          </b-form-input>
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="primary">SignUp</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </nav>
    <alert :variant="variant"  :message="message" v-if="showMessage"></alert>

</div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import Swal from 'sweetalert2'
export default {
  name: 'Index',
  props: {
    msg: String,
  },
  data() {
    return {
      loginForm: {
        name: '',
        email: '',
      },
      signupForm: {
        name: '',
        email: '',
        password: '',
      },
      auth: false,
      message: '',
      variant:"",
      showMessage: false,
      username: ''
    };
  },
  components: {
    alert: Alert,
  },
  methods: {

    authenticate(payload) {
      const path = 'http://127.0.0.1:5000/api/v1/auth/login';
      axios.post(path, payload).then((response) => {
        Swal.fire({
          position: 'top-end',
          type: 'success',
          title: response.data.message,
          showConfirmButton: false,
          timer: 1500
        });
        var token = response.data.data.token;
        var user = response.data.data.user.name;
        localStorage.setItem('token', token);
        localStorage.setItem('user', user);
        this.auth = true;
        this.$router.push({
          name: "Favorite"
        })

      })
      .catch((error) => {
        console.log('----', error.response.data.message);
        this.showMessage = true
        this.message = error.response.data.message
        this.variant= "danger"

      })

    },
     register(payload) {
      const path = 'http://127.0.0.1:5000/api/v1/auth/register';
      axios.post(path, payload).then((response) => {
          Swal.fire({
          position: 'top-end',
          type: 'success',
          title: response.data.message,
          showConfirmButton: false,
          timer: 1500
        });
          var token = response.data.data.token;
          var user = response.data.data.user.name;
          localStorage.setItem('token', token);
          localStorage.setItem('user', user);
          this.auth = true;
          this.$router.replace(this.$route.query.redirect || {
            name: "Favorite"
          })

        })
        .catch((error) => {
          console.log('======', error)
          this.showMessage = true
          this.variant="danger"
          this.message = error.response.data.message
        })

    },
    initForm() {
      this.loginForm.password = '',
        this.loginForm.email = '',
        this.signupForm.name = '',
        this.signupForm.email = '',
        this.signupForm.password = ''
    },

    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addLoginModal.hide();
      const payload = {
        email: this.loginForm.email,
        password: this.loginForm.password,
      };
      this.authenticate(payload);
      this.initForm();
    },

    onSubmitRegister(evt) {
      evt.preventDefault();
      this.$refs.addSignupModal.hide();
      const payload = {
        email: this.signupForm.email,
        password: this.signupForm.password,
        name: this.signupForm.name
      };
      this.register(payload);
      this.initForm();
    },

    onReset(evt) {
      evt.preventDefault();
      this.$refs.addLoginModal.hide();
      this.initForm();
    },
    checkCurrentLogin() {
      if (localStorage.token) {
        this.auth = true;
        this.username = localStorage.getItem('user')
      }
      else {
         this.$router.push('/?redirect=' + this.$route.path)
      }


    },
    logOut() {
      delete localStorage.token;
      delete localStorage.user;
      this.auth = false;
      Swal.fire({
          position: 'top-end',
          type: 'warning',
          title: 'you have been logged out successfully',
          showConfirmButton: false,
          timer: 1500
        });
      this.$router.replace(this.$route.query.redirect || {
        name: 'index'
      })
    }

  },
  created() {
    this.checkCurrentLogin()
  },
  updated() {
    console.log('I entered updateddddd');
    if (!localStorage.token && this.$route.path !== '/') {
      this.$router.push('/?redirect=' + this.$route.path)
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
