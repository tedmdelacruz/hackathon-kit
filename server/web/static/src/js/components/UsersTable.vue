<template>
    <div>
        <table class="table table-condensed table-dark table-hover mb-0">
            <thead>
                <th>First name</th>
                <th>Last name</th>
                <th>Username</th>
                <th>Email</th>
                <th>Status</th>
                <th></th>
            </thead>
            <tbody>
                <tr v-for="user in users"
                    v-bind:class="{ 'text-secondary': !user.is_active }">
                    <td>{{ user.first_name }}</td> 
                    <td>{{ user.last_name }}</td> 
                    <td>{{ user.username }}</td>
                    <td>{{ user.email }}</td>
                    <td>
                        {{ user.is_active ? 'Active' : 'Inactive' }}
                    </td>
                    <td></td>
                </tr>
                <create-user-row></create-user-row>
            </tbody>
        </table>
    </div>
</template>

<script>
    import axios from 'axios'
    import { mapGetters } from 'vuex'
    import CreateUserRow from './CreateUserRow.vue'

    export default {
        computed: {
            ...mapGetters({
                users: 'getUsers'
            })
        },
        components: {
            CreateUserRow
        },
        methods: {
            get() {
                axios.get('/api/users')
                    .then(response => {
                        this.$store.commit('receiveUsers', response.data.results)
                    })
            }
        },
        beforeMount() {
            this.get()
        }
    }
</script>