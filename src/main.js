import Vue from 'vue';
import VueRouter from 'vue-router';
import Vuex from 'vuex';
import App from './App';

import router from './routes';

Vue.use(VueRouter);
Vue.use(Vuex);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router,
});

// new Vue({
//   router,
// }).$mount('#app');
