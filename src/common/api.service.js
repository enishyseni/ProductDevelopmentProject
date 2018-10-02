import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import JwtService from '@/common/jwt.service'
import { API_URL } from '@/common/config'

const ApiService = {
  init () {
    Vue.use(VueAxios, axios)
    Vue.axios.defaults.baseURL = API_URL
  },

  setHeader () {
    Vue.axios.defaults.headers.common['Authorization'] = `JWT ${JwtService.getToken()}`
  },

  query (resource, params = '') {
    return Vue.axios
      .get(`${resource}/`, params)
      .catch((error) => {
        throw new Error(`[RWV] ApiService ${error}`)
      })
  },

  get (resource, params = '') {
    return Vue.axios
      .get(`${resource}/${params}`)
      .catch((error) => {
        throw new Error(`[RWV] ApiService ${error}`)
      })
  },

  post (resource, params) {
    return Vue.axios.post(`${resource}/`, params)
  },

  update (resource, slug, params) {
    return Vue.axios.put(`${resource}/${slug}`, params)
  },

  put (resource, params) {
    return Vue.axios
      .put(`${resource}/`, params)
  },

  delete (resource, id) {
    return Vue.axios.post(`${resource}/`, id)
  }
}

export default ApiService







export const PartnerService = {
  query (model, params) {
    return ApiService.query(model, { queryfields: params })
  },
  get (model, id) {
    return ApiService.get(model, id)
  },
  create (model, params) {
    return ApiService.post(model, {partner: params})
  },
  update (model, params) {
    return ApiService.update(model, {partner: params})
  },
  delete (model, id) {
    return ApiService.delete(model, id)
  }
}

