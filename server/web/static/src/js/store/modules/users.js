const state = {
    data: [],
    isCreateMode: false,
}

const getters = {
    getUsers: state => state.users.data,
    isCreateMode: state => state.users.isCreateMode,
}

const mutations = {
    receiveUsers (state, users) {
        state.data = users
    },
    toggleUserCreateMode (state) {
        state.isCreateMode = !state.usersTable.isCreateMode
    },
}

export default {
    state,
    getters,
    mutations,
}
