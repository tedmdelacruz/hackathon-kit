<template>
    <div class="site-wrapper">

        <div class="site-wrapper-inner">

            <div class="cover-container">
                <guest-nav></guest-nav>

                <div class="inner cover">
                    <h1 class="cover-heading">Prototype Kit</h1>
                    <p class="lead">This is a starter kit prototyping web applications, APIs, and mobile app ideas.</p>
                    <p class="lead">
                        <router-link to="/login" class="btn btn-lg btn-primary">Login</router-link>
                        <router-link to="/signup" class="btn btn-lg btn-secondary">Signup</router-link>
                    </p>
                </div>

                <div class="mastfoot">
                    <div class="inner">
                        <p><a href="https://protokit.tedmdelacruz.com">Prototype Kit</a> by <a href="https://github.com/tedmdelacruz">Ted Mathew dela Cruz</a>.</p>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
    import GuestNav from '../components/common/GuestNav.vue';

    export default {
        components: {
            GuestNav
        }
    }
</script>