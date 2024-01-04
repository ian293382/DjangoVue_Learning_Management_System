<template>
  <div class="nav">
    <Nav/>
  </div>

  <router-view/>

  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2021</p>
  </footer>
</template>

<script>
import Nav from '@/components/Nav';

export default {
  name: 'App',
  components: {
    Nav,
  }
}

</script>

<style lang="scss">
@import '../node_modules/bulma';

.white{
  color: white !important;
}
</style>
