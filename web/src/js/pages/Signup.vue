<template>

    <div class="site-wrapper">

        <div class="site-wrapper-inner">

            <div class="cover-container">
                <guest-nav></guest-nav>

                <div class="inner cover">
                    <h1 class="cover-heading">Signup</h1>
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
