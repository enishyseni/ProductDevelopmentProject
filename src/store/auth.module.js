import ApiService from '@/common/api.service'
import JwtService from '@/common/jwt.service'
import { LOGIN, LOGOUT, REGISTER, CHECK_AUTH, UPDATE_USER } from './actions.type'
import { SET_AUTH, PURGE_AUTH, SET_ERROR } from './mutations.type'
import router from '../router'

const state = {
  errors: null,
  user: {},
  isAuthenticated: !!JwtService.getToken()
}

const getters = {
  currentUser (state) {
    return state.user
  },
  isAuthenticated (state) {
    return state.isAuthenticated
  }
}

const actions = {
  [LOGIN] (context, credentials) {
    return new Promise((resolve) => {
      ApiService
        .post('api-token-auth/', {username: credentials.username, password: credentials.password})
        .then(({data}) => {
          context.commit(SET_AUTH, data.token)
          resolve(data)
        })
        .catch(({response}) => {
          context.commit(SET_ERROR, response.data.errors)
        })
    })
  },
  [LOGOUT] (context) {
    context.commit(PURGE_AUTH)
  },
  [REGISTER] (context, model) {
    return new Promise((resolve, reject) => {
      ApiService
        .post('users/register/', {username: model.username, email: model.email, password: model.password})
        .then(({data}) => {
          //context.commit(SET_AUTH, data.user)
          context.commit(LOGIN, data)
          resolve(data)
        })
        .catch(({response}) => {
          context.commit(SET_ERROR, response.data.errors)
        })
    })
  },
  [CHECK_AUTH] (context) {
    if (JwtService.getToken()) {
      ApiService.setHeader()
      ApiService
        .post('api-token-verify/', {token: JwtService.getToken()})
        .then(({data}) => {
          context.commit(SET_AUTH, data.token)
        })
        .catch(({response}) => {
          context.commit(SET_ERROR, response.data.errors)
          router.push({ name: 'Login' })
        })
    } else {
      context.commit(PURGE_AUTH)
      //Router.push({ name: 'Login' })
    }
  },
  [UPDATE_USER] (context, payload) {
    const {email, username, password, image, bio} = payload
    const user = {
      email,
      username,
      bio,
      image
    }
    if (password) {
      user.password = password
    }

    return ApiService
      .put('user', user)
      .then(({data}) => {
        context.commit(SET_AUTH, data.user)
        return data
      })
  }
}

const mutations = {
  [SET_ERROR] (state, error) {
    state.errors = error
  },
  [SET_AUTH] (state, token) {
    state.isAuthenticated = true
    state.user = {}
    state.errors = {}
    JwtService.saveToken(token)
  },
  [PURGE_AUTH] (state) {
    state.isAuthenticated = false
    state.user = {}
    state.errors = {}
    JwtService.destroyToken()
  }
}

export default {
  state,
  actions,
  mutations,
  getters
}
