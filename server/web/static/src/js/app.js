import base from './base'
import Vue from 'vue';
import VueRouter from 'vue-router';
import axios from 'axios';

import App from './pages/App.vue';

const routes = [
    { path: '/', component: App },
]

const router = new VueRouter({ routes })

Vue.use(VueRouter);

const app = new Vue({ router }).$mount('#app')
