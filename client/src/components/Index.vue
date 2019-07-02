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
                            <p class="text-format "> It's Personal, express yourself with pictures or word..<br> Ready to start writing? Sign up now!
                            </p>
                            <a href="signup.html "><button type="button " class="btn account__btn ">Get Started</button></a>
                        </div>
                    </div>
                </div>
                <!--end row-->
                <div class="row ">
                    <div class="column ">
                        <div class="flex ">
                            <h4>Digitize your private diary</h4>
                            <p class="text-format ">Keep a journal of your daily activities, your travel, exercise, diet, or thoughts and prayers.</p>
                            <a href="signup.html "><button type="button " class="btn account__btn "><i class="fa fa-dashcube "></i> Register Now!</button></a>
                        </div>
                    </div>
                    <div class="column ">
                        <img class="img__shelter " src="../assets/images/small.png">
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
                                <img class="img__shelter" src="../assets/images/prior.png">
                            </div>
                            <p class="text-format">Custom email reminders help you make sure you never forget to write.</p>
                        </div>
                        <!--end card-->
                    </div>
                    <div class="column">
                        <div class="card">
                            <div class="card__image">
                                <img class="img__shelter" src="../assets/images/book2.jpg">
                            </div>
                            <p class="text-format">Make each journal your own with custom covers, backgrounds, and fonts..</p>
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

};

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
