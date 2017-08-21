import 'jquery';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap-grid.min.css';
import Vue from 'vue';
import VueRouter from 'vue-router';
import axios from 'axios';

import Home from './pages/Home.vue';
import Signup from './pages/Signup.vue';
import Login from './pages/Login.vue';

const routes = [
    { path: '/', component: Home },
    { path: '/signup', component: Signup },
    { path: '/login', component: Login },
]

const router = new VueRouter({ routes })

Vue.use(VueRouter);

const app = new Vue({ router }).$mount('#app')
