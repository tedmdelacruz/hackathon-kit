<template>
    <table class="table table-condensed table-hover">
        <thead>
            <th>Username</th>
            <th>Email</th>
            <th></th>
        </thead>
        <tbody>
            <tr v-for="user in this.$store.state.users">
                <td>{{ user.username }}</td>
                <td>{{ user.email }}</td>
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