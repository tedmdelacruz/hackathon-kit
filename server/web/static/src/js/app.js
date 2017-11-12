import base from './base'
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import router from './router'
import store from './store'
import App from './pages/App.vue'

document.getElementById('app').style.display = 'block'
const app = new Vue(Vue.util.extend({ router, store }, App)).$mount('#app')
