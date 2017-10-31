<template>

<div>
    <nav-bar></nav-bar>
    <users-table></users-table>
</div>

</template>

<script>
    import NavBar from '../components/NavBar.vue';
    import UsersTable from '../components/UsersTable.vue';
    
    export default {
        components: {
           NavBar,
           UsersTable,
        }
    };
</script>