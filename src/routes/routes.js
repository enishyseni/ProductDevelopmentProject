import BritecoreLayout from '../components/Britecore/Layout/BritecoreLayout.vue'
// GeneralViews
import NotFound from '../components/GeneralViews/NotFoundPage.vue'
import Login from '../Views/Login.vue'
import Register from '../Views/Register.vue'

// Admin pages
import UserProfile from '../components/Britecore/Views/UserProfile.vue'
import Partners from '../components/Britecore/Views/Partners/Partners/PartnersList.vue'
import Contracts from '../components/Britecore/Views/Contracts/Contracts/MyContractsList.vue'



const routes = [
  { 
    path: '/', 
    redirect: '/admin',
  },
  { 
    path: '/login', 
    name: 'Login',
    component: Login,
    meta: { 
      guest: true
    }
  },
  { 
    path: '/register',      
    name: 'Register',
    component: Register,
    meta: { 
      guest: true
    }
   },
  {
    path: '/admin',
    component: BritecoreLayout,
    redirect: '/admin/contracts',
    children: [
      
	    {
        path: 'stats',
        name: 'stats',
        component: UserProfile
      },  
      {
        path: 'contracts',
        name: 'contracts',
        component: Contracts
      },   
      {
        path: 'partners',
        name: 'partners',
        component: Partners
      }
    ]
  },
  { path: '*', component: NotFound }
]

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Britecore/Views/' + name + '.vue');
   return res;
};**/

export default routes
