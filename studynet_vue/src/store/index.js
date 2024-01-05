import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      token: '',
      isAuthenticated: falsex``
    }
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStoreage.getItem('token')) {
        state.user.token = localStoreage.getItem('token')
        state.user.isAuthenticated = true
      } else {
        state.user.token = ''
        state.user.isAuthenticated = false
      }
    },
    setToken(state, token) {
      state.user.token = token 
      state.user.isAuthenticated = true
    }
  },
  actions: {
  },
  modules: {
  }
})
