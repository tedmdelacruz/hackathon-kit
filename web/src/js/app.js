import 'jquery';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap-grid.min.css';
import Vue from 'vue';
import axios from 'axios';

let app = new Vue({
    el: '#app',
    data: {
        users: []
    },
    mounted() {
        var self = this;
        axios.get('http://api.localtest.me:8000/users/')
            .then(response => {
                self.users = response.data.results;
            });
    }
});
