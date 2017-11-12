const state = {
    usersTable: {
        data: [],
        isCreateMode: false,
    }
}

const mutations = {
    receiveUsers (state, users) {
        state.usersTable.data = users
    },
    toggleUserCreateMode (state) {
        state.usersTable.isCreateMode = !state.usersTable.isCreateMode
    },
}

export default {
    state,
    mutations,
}
