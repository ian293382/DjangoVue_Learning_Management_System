<template>
    <div class="courses">
      <div class="hero is-info is-medium">
        <div class="hero-body has-text-centered">
          <h1 class="title">{{ course.title }}</h1>
        </div>
      </div>
      <section class="section">
        <div class="container">
         <div class="columns content">
            <div class="column is-2">
                <h2>Table of contents</h2>

                <ul>
                    <li><a href="#">Introduction</a></li>
                    <li><a href="#">Get started</a></li>
                    <li><a href="#">Part I</a></li>
                    <li><a href="#">Part II</a></li>
                    <li><a href="#">Summary</a></li>
                </ul>
            </div>
            <div class="column is-10">
                <h2>Introduction</h2>

                {{ course.long_description }}
            </div>
         </div>
        </div>
      </section>
    </div>
  </template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            course: []
        }
    },

    mounted() {
        console.log('mounted')

        const slug = this.$route.params.slug

        axios
            .get(`/courses/${slug}`)
            .then(response => {
                console.log(response.data)
              
                this.course = response.data
            })
    }
}

</script>