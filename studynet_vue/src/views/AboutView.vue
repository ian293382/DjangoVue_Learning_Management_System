<template>
  <div class="about">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">About</h1>


      </div>
    </div>

    <section class="section">
      This is an about page
    </section>

  </div>
</template>

<script>
export default {
  mounted() {
    console.log ('mounted')
    document.title = 'About | StudyNet'
  }
}
</script>
