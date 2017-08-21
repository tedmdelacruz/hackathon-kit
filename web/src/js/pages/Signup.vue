<template>

<div class="site-wrapper">

    <div class="site-wrapper-inner">

        <div class="cover-container">
            <guest-nav></guest-nav>

            <div class="inner cover">
                <h1 class="cover-heading">Create an account</h1>
                <form action="post" v-on:submit="signup()" onsubmit="return false">
                    <div class="form-group">
                        <input type="text" class="form-control" id="signup-name" placeholder="Name"
                            v-model="name">
                    </div>
                    <div class="form-group">
                        <input type="email" class="form-control" id="signup-email" placeholder="Email"
                            v-model="email">
                    </div>
                    <div class="form-group">
                        <input type="text" class="form-control" id="signup-username" placeholder="Username"
                            v-model="username">
                    </div>
                    <div class="form-group">
                        <input type="password" class="form-control" id="signup-password" placeholder="Password"
                            v-model="password">
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-lg btn-primary">Submit</button>
                    </div>
                </form>
            </div>

            <custom-footer></custom-footer>
        </div>

    </div>
</div>

</template>

<script>
    import GuestNav from '../components/common/GuestNav.vue';
    import CustomFooter from '../components/common/CustomFooter.vue';
    import axios from 'axios';

    import constants from '../constants';

    export default {
        data() {
            return {
                name: '',
                email: '',
                username: '',
                password: ''
            }
        },
        components: {
            GuestNav,
            CustomFooter
        },
        methods: {
            signup() {
                const data = {
                    name: this.name,
                    email: this.email,
                    username: this.username,
                    password: this.password
                }

                const baseUrl = constants.api.baseUrl;

                // @TODO Handle signup errors
                axios.post(baseUrl + '/users/', data)
                    .then(response => {
                        // @TODO Handle successful signup
                    })
            }
        }
    }
</script>
