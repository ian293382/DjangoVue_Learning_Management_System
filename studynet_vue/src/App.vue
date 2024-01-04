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

export default {
  name: 'App',
  components: {
    Nav,
    Footer
  }
}

</script>

<style lang="scss">
@import '../node_modules/bulma';

.white{
  color: white !important;
}
</style>
