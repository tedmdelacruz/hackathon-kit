<template>

<div class="site-wrapper">

    <div class="site-wrapper-inner">

        <div class="cover-container">
            <guest-nav></guest-nav>

            <div class="inner cover">
                <h1 class="cover-heading">Login</h1>
                <form action="post">
                    <div class="form-group">
                        <input type="text" class="form-control" id="signup-username" placeholder="Username">
                    </div>
                    <div class="form-group">
                        <input type="password" class="form-control" id="signup-password" placeholder="Password">
                    </div>
                    <div class="form-group">
                        <button class="btn btn-lg btn-primary">Submit</button>
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

    export default {
        data() {
            return {
                username: '',
                password: ''
            }
        },
        components: {
            GuestNav,
            CustomFooter
        }
    }
</script>
