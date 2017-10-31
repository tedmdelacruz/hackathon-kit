import base from './base'
import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import axios from 'axios';

import App from './pages/App.vue';

const routes = [
    { path: '/', component: App },
];

Vue.use(VueRouter);
const router = new VueRouter({ routes });

Vue.use(Vuex);
const store = new Vuex.Store({
    state: {
        users: []
    },
    mutations: {
        receiveUsers (state, users) {
            state.users = users;
        },
    }
});

document.getElementById('app').style.display = 'block';
const app = new Vue(Vue.util.extend({ router, store }, App)).$mount('#app');
