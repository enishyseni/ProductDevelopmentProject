import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './routes/routes'

import store from '@/store'
import { CHECK_AUTH } from '@/store/actions.type'

Vue.use(VueRouter)

// configure router
const router = new VueRouter({
    routes: routes, // short for routes: routes
    linkActiveClass: 'active'
  })

//const router = new VueRouter()

//router.map(routes)


router.beforeEach(
    (to, from, next) => {
        return Promise
          .all([store.dispatch(CHECK_AUTH)])
          .then(next)
    }
  )

// export the router instance
export default router