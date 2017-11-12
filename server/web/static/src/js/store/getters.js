// @TODO Refactor
const getUsers = state => state.users.data
const isCreateMode = state => state.users.isCreateMode

export default {
    getUsers,
    isCreateMode,
}
