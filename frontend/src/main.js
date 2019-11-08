import Vue from 'vue'
import store from '@/store'
import router from '@/router'


import '@/services/api'

import { EventBus } from '@/services/EventBus'





import App from '@/App.vue'
import './registerServiceWorker'

Vue.config.productionTip = false






import '@/assets/scss/tailwind.css'


import '@/assets/scss/app.scss'

window.EventBus = EventBus

router.beforeEach((to, from, next) => {
  if (to.meta.auth && !store.getters['UserModule/token']) {
    // Redirect home
    next({
      name: 'home'
    })
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  
  render: h => h(App)
}).$mount('#app')
