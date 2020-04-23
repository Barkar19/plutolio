import Vue from 'vue'
import VueRouter from 'vue-router'
// import Vuex from 'vuex'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

import Home from './views/Home.vue'
import Reports from './views/Reports.vue'
import Transactions from './views/Transactions.vue'
import Currencies from './views/Currencies.vue'
import Settings from './views/Settings.vue'

Vue.use(VueRouter)
// Vue.use(Vuex)

Vue.config.productionTip = false

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/',            component: Home, name:'home' },
    { path:"/reports",      component: Reports },
    { path:"/transactions", component: Transactions },
    { path:"/currencies",   component: Currencies },
    { path:"/settings",     component: Settings },
  ]
})

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
