<template>
<div class="nav">
  <nav class="navbar is-info" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
    <a href="/" class="navbar-item is-size-4 white">StudyNet</a>

    <div class="navbar-menu" id="navbar-item">
      <div class="navbar-start">
        <a href="#" class="navbar-item">Home</a>
        <a href="#" class="navbar-item">About</a>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a href="#" class="button is-primary"><strong>Sign up</strong></a>
            <a href="#" class="button is-light">Log in</a>
          </div>
        </div>
      </div>
    </div>

  </nav>
</div>

  <router-view/>

  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2021</p>
  </footer>
</template>

<style lang="scss">
@import '../node_modules/bulma';

.white{
  color: white !important;
}
</style>
