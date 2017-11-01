<template>
    <table class="table table-condensed table-dark table-hover">
        <thead>
            <th>Name</th>
            <th>Username</th>
            <th>Email</th>
            <th>Status</th>
            <th></th>
        </thead>
        <tbody>
            <tr v-for="user in this.$store.state.users"
                v-bind:class="{ 'text-secondary': !user.is_active }">
                <td>{{ user.first_name + ' ' + user.last_name}}</td> 
                <td>{{ user.username }}</td>
                <td>{{ user.email }}</td>
                <td>
                    {{ user.is_active ? 'Active' : 'Inactive' }}
                </td>
                <td>-</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
    import axios from 'axios';

    export default {
        methods: {
            get() {
                axios.get('/api/users')
                    .then(response => {
                        this.$store.commit('receiveUsers', response.data.results)
                    })
            }
        },
        beforeMount() {
            this.get();
        }
    };
</script>