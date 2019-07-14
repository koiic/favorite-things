  <template>
    <div class="hello">
         <section class="py-5">
            <div class="shelter">
                <h1 class="text-center app-color">Go ahead, take a peek</h1>
                <div class="row">
                    <div class="column">
                        <img class="img__shelter" src="../assets/images/address_book.png">
                    </div>
                    <div class=" column ">
                        <div class="flex ">
                            <p class="text-format "> It's Personal, prioritize your hobbies..<br> Ready to pen down your favorite things? Sign up now!
                            </p>
                            <button type="button" v-if="!auth" class="btn btn-success btn-sm" v-b-modal.login-modal>Get Started</button>
                        </div>
                    </div>
                </div>
                <!--end row-->
                <div class="row ">
                    <div class="column ">
                        <div class="flex ">
                            <h4>Digitize your hobbies and things you cherished</h4>
                            <p class="text-format ">Keep a daily journal of your favorite things .</p>
                                <button type="button" v-if="!auth" class="btn btn-success btn-sm" v-b-modal.signup-modal>Register Now</button>
                        </div>
                    </div>
                    <div class="column ">
                        <img class="img__shelter " src="../assets/images/designer.png">
                    </div>
                </div>
                <!--end row-->
            </div>
        </section>
        <section class="py-5">
            <div class="shelter">
                <h2 class="text-center pb-1 app-color">What we Offer!</h2>
                <div class="row">
                    <div class="column">
                        <div class="card">
                            <div class="card__image">
                                <img class="img__shelter" src="../assets/images/pen-icon.png">
                            </div>
                            <p class="text-format">Designed to focus on privacy, your entries are totally private by default!.</p>
                        </div>
                        <!--end card-->
                    </div>
                    <div class="column">
                        <div class="card">
                            <div class="card__image">
                                <img class="img__shelter" src="../assets/images/small.png">
                            </div>
                            <p class="text-format">Custom email reminders help you make sure you never forget to write.</p>
                        </div>
                        <!--end card-->
                    </div>
                    <div class="column">
                        <div class="card">
                            <div class="card__image">
                                <img class="img__shelter" src="../assets/images/prior.png">
                            </div>
                            <p class="text-format">Ability to rank/prioritize favorite things</p>
                        </div>
                        <!--end card-->
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    data() {
        return {
            auth: false,
            username: ''
        }
    },
    created() {
        if (localStorage.token) {
        this.auth = true;
        this.username = localStorage.getItem('user')
      }
      else {
        this.auth = false;
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

.py-5 {
    padding: 5rem 0rem;
}

.shelter {
    width: 100%;
    padding: 0 15px;
    margin-right: auto;
    margin-left: auto;
}

.row {
    display: flex;
    flex-wrap: wrap;

}

.column {
    flex: 1;
    margin-right: 20px;

}


.flex {
    height: 100% !important;
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;
    align-self: center;
    flex-direction: column;
}

.column:last-child {
    margin-right: 0;
}


.text-format {
    color: #3c3c3c;
    line-height: 1.8;
    font-weight: 100;
}


*,
 ::after,
 ::before {
    box-sizing: border-box;
}

</style>
