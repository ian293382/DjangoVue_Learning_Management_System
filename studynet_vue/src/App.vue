<template>
  <div class="nav">
    <Nav/>
  </div>

  <router-view/>

  <Footer/>
  
</template>

<script>
import Nav from '@/components/Nav';
import Footer from '@/components/Footer';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    Nav,
    Footer
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.user.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}

</script>

<style lang="scss">
@import '../node_modules/bulma';

.white{
  color: white !important;
}
</style>
