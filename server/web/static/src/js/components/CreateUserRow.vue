<template>
    <tr>
        <!-- Can't think a fucking workaround for this yet -->
        <td v-if="isCreateMode" class="table-input-cell">
            <input type="text" name="first_name" placeholder="First name"
                v-model="first_name">
        </td>
        <td v-if="isCreateMode" class="table-input-cell">
            <input type="text" name="last_name" placeholder="Last name"
                v-model="last_name">
        </td>
        <td v-if="isCreateMode" class="table-input-cell">
            <input type="text" name="username" placeholder="Username" required
                v-model="username">
        </td>
        <td v-if="isCreateMode" class="table-input-cell">
            <input type="email" name="email" placeholder="Email" required
                v-model="email">
        </td>
        <td v-if="isCreateMode">
            <input type="checkbox" class="table-input" name="status" checked="checked"
                v-model="status">
        </td>
        <td v-if="isCreateMode" style="white-space:nowrap">
            <button class="table-button"
                v-on:click="create">Save</button>
            <button class="table-button" v-on:click="toggleCreateMode">Cancel</button>
        </td>

        <td colspan="6" class="text-center" v-on:click="toggleCreateMode"
            v-if="!isCreateMode">
            <small class="text-muted">+ Create New</small>
        </td>
    </tr>
</template>
<script>
    import { mapGetters } from 'vuex'
    import axios from 'axios'

    export default {
        data: () => {
            return {
                first_name: '',
                last_name: '',
                username: '',
                email: '',
                status: '',
            }
        },
        getters: {
            ...mapGetters({
                isCreateMode: 'isCreateMode'
            })
        },
        methods: {
            toggleCreateMode() {
                this.$store.commit('toggleUserCreateMode')
            },
            create() {
                this.$store.commit('toggleUsersTableLoading')
                axios.post('/api/users', this.data)
                    .then(response => {
                        this.$store.commit('getUsers')
                        this.$store.commit('toggleUsersTableLoading')
                    })
            }
        }
    }
</script>