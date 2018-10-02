import BritecoreLayout from '../components/Britecore/Layout/BritecoreLayout.vue'
// GeneralViews
import NotFound from '../components/GeneralViews/NotFoundPage.vue'
import Login from '../components/Britecore/Views/Login.vue'
import Register from '../components/Britecore/Views/Register.vue'
import UserProfile from '../components/Britecore/Views/UserProfile.vue'

// BriteCore pages
import Partners from '../components/Britecore/Views/Partners/Partners/PartnersList.vue'
import NewPartner from '../components/Britecore/Views/Partners/Partners/NewPartner.vue'
import PartnerMembers from '../components/Britecore/Views/Partners/PartnerMembers/PartnerMembersList.vue'
import NewPartnerMember from '../components/Britecore/Views/Partners/PartnerMembers/NewPartnerMember.vue'
import PartnerTypes from '../components/Britecore/Views/Partners/PartnerTypes/PartnerTypesList.vue'
import NewPartnerType from '../components/Britecore/Views/Partners/PartnerTypes/NewPartnerType.vue'

import Contracts from '../components/Britecore/Views/Contracts/Contracts/MyContractsList.vue'
import NewContract from '../components/Britecore/Views/Contracts/Contracts/NewContract.vue'
import ContractsDefinitions from '../components/Britecore/Views/Contracts/ContractDefinitions/ContractDefinitionsList.vue'
import NewContractDefinition from '../components/Britecore/Views/Contracts/ContractDefinitions/NewContractDefinition.vue'
import ContractsDocuments from '../components/Britecore/Views/Contracts/ContractDocuments/ContractDocumentsList.vue'
import NewContractDocument from '../components/Britecore/Views/Contracts/ContractDocuments/NewContractDocument.vue'
import ContractsExpenses from '../components/Britecore/Views/Contracts/ContractExpenses/ContractExpensesList.vue'
import NewContractExpense from '../components/Britecore/Views/Contracts/ContractExpenses/NewContractExpense.vue'


const routes = [
  { 
    path: '/', 
    redirect: '/insurance',
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
    path: '/insurance',
    component: BritecoreLayout,
    redirect: '/insurance/contracts',
    children: [
      
	    {
        path: 'stats',
        name: 'User Profile',
        component: UserProfile
      },  
      {
        path: 'contracts',
        name: 'Contracts',
        component: Contracts
      },   
      {
        path: 'newcontract',
        name: 'New Contract',
        component: NewContract
      }, 
      {
        path: 'contractsexpenses',
        name: 'Contracts Expenses',
        component: ContractsExpenses
      },  
      {
        path: 'newcontractexpense',
        name: 'New Contract Expense',
        component: NewContractExpense
      }, 
      {
        path: 'contractsdefinitions',
        name: 'Contracts Definitions',
        component: ContractsDefinitions
      }, 
      {
        path: 'newcontractdefinition',
        name: 'Contract Definition',
        component: NewContractDefinition
      }, 
      {
        path: 'contractsdocuments',
        name: 'Contracts Documents',
        component: ContractsDocuments
      }, 
      {
        path: 'newcontractdocument',
        name: 'New Contract Document',
        component: NewContractDocument
      },
      {
        path: 'partners',
        name: 'Partners',
        component: Partners
      },
      {
        path: 'newpartner',
        name: 'New Partner',
        component: NewPartner
      },
      {
        path: 'partnermembers',
        name: 'Partner Members',
        component: PartnerMembers
      },
      {
        path: 'newpartnermember',
        name: 'New Partner Member',
        component: NewPartnerMember
      },
      {
        path: 'partnertypes',
        name: 'Partner Types',
        component: PartnerTypes
      },
      {
        path: 'newpartnertype',
        name: 'New Partner Type',
        component: NewPartnerType
      },
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
