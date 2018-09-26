import BritecoreLayout from '../components/Britecore/Layout/BritecoreLayout.vue'
// GeneralViews
import NotFound from '../components/GeneralViews/NotFoundPage.vue'

// Admin pages
import UserProfile from 'src/components/Britecore/Views/UserProfile.vue'
import Notifications from 'src/components/Britecore/Views/Notifications.vue'
import Overview from 'src/components/Britecore/Views/Contracts/Contracts/MyContractsList.vue'
import Partners from 'src/components/Britecore/Views/Partners/Partners/PartnersList.vue'
import Icons from 'src/components/Britecore/Views/Icons.vue'
import Maps from 'src/components/Britecore/Views/Maps.vue'
import Typography from 'src/components/Britecore/Views/Typography.vue'
import TableList from 'src/components/Britecore/Views/TableList.vue'

const routes = [
  {
    path: '/',
    component: BritecoreLayout,
    redirect: '/admin/contracts'
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
        path: 'notifications',
        name: 'notifications',
        component: Notifications
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
      },
      {
        path: 'maps',
        name: 'maps',
        component: Maps
      },
      {
        path: 'typography',
        name: 'typography',
        component: Typography
      },
      {
        path: 'table-list',
        name: 'table-list',
        component: TableList
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
