<template>
    <tr>
        <!-- Can't think a fucking workaround for this yet -->
        <td v-if="this.$store.state.usersTable.isCreateMode" class="table-input-cell">
            <input type="text" name="first_name" placeholder="First name">
        </td>
        <td v-if="this.$store.state.usersTable.isCreateMode" class="table-input-cell">
            <input type="text" name="last_name" placeholder="Last name">
        </td>
        <td v-if="this.$store.state.usersTable.isCreateMode" class="table-input-cell">
            <input type="text" name="username" placeholder="Username" required>
        </td>
        <td v-if="this.$store.state.usersTable.isCreateMode" class="table-input-cell">
            <input type="email" name="email" placeholder="Email" required>
        </td>
        <td v-if="this.$store.state.usersTable.isCreateMode">
            <input type="checkbox" class="table-input" name="status" checked="checked">
        </td>
        <td v-if="this.$store.state.usersTable.isCreateMode" style="white-space:nowrap">
            <button class="table-button">Save</button>
            <button class="table-button" v-on:click="toggleCreateMode">Cancel</button>
        </td>

        <td colspan="6" class="text-center" v-on:click="toggleCreateMode"
            v-if="!this.$store.state.usersTable.isCreateMode">
            <small class="text-muted">+ Create New</small>
        </td>
    </tr>
</template>
<script>
    export default {
        methods: {
            toggleCreateMode() {
                this.$store.commit('toggleUserCreateMode');
            }
        }
    };
</script>