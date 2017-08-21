<template>

<div class="site-wrapper">

    <div class="site-wrapper-inner">

        <div class="cover-container">
            <guest-nav></guest-nav>

            <div class="inner cover">
                <h1 class="cover-heading">Login</h1>
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
        components: {
            GuestNav,
            CustomFooter
        }
    }
</script>
