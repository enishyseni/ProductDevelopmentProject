import Sidebar from './SideBar.vue'

const SidebarStore = {
  showSidebar: false,
  sidebarLinks: [    
    {
      name: 'Partners',
      icon: 'ti-user',
      path: '/insurance/partners'
    },
    {
      name: 'Partner Members',
      icon: 'ti-user',
      path: '/insurance/partnermembers'
    },
    {
      name: 'New Partner',
      icon: 'ti-user',
      path: '/insurance/newpartner'
    },
    {
      name: 'Partner Types',
      icon: 'ti-user',
      path: '/insurance/partnertypes'
    },
    {
      name: 'New Partner Type',
      icon: 'ti-user',
      path: '/insurance/newpartnertype'
    },
    {
      name: 'Contracts',
      icon: 'ti-panel',
      path: '/insurance/contracts'
    },
    {
      path: '/insurance/newcontract',
      icon: 'ti-panel',
      name: 'New Contract'
    }, 
    {
      path: '/insurance/contractsexpenses',
      icon: 'ti-panel',
      name: 'Contracts Expenses'
    },  
    {
      path: '/insurance/newcontractexpense',
      icon: 'ti-panel',
      name: 'New Contract Expense'
    }, 
    {
      path: '/insurance/contractsdefinitions',
      icon: 'ti-panel',
      name: 'Contracts Definitions'
    }, 
    {
      path: '/insurance/newcontractdefinition',
      icon: 'ti-panel',
      name: 'New Contract Definition'
    }, 
    {
      path: '/insurance/contractsdocuments',
      icon: 'ti-panel',
      name: 'Contracts Documents'
    }, 
    {
      path: '/insurance/newcontractdocument',
      icon: 'ti-panel',
      name: 'New Contract Document'
    },
    {
      name: 'User Profile',
      icon: 'ti-user',
      path: '/insurance/stats'
    },
  ],
  displaySidebar (value) {
    this.showSidebar = value
  }
}

const SidebarPlugin = {

  install (Vue) {
    Vue.mixin({
      data () {
        return {
          sidebarStore: SidebarStore
        }
      }
    })

    Object.defineProperty(Vue.prototype, '$sidebar', {
      get () {
        return this.$root.sidebarStore
      }
    })
    Vue.component('side-bar', Sidebar)
  }
}

export default SidebarPlugin
