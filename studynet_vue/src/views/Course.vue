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
                    <li
                        v-for="lesson in lessons"
                        v-bind:key="lesson.id">
                        <a href="#">{{ lesson.title }}</a>
                    </li>
                   
                </ul>
            </div>
            <div class="column is-10">
                <template v-if="$store.state.user.isAuthenticated">
                    <h2>Introduction</h2>
        
                    {{ course.long_description }}   
                </template>
                <template v-else>
                    <h2>Restricted access</h2>

                    <p>You need to have an account to continue!</p>
                </template>

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
            course: {},
            lessons: []
        }
    },

    mounted() {
        console.log('mounted')

        const slug = this.$route.params.slug

        axios
            .get(`/courses/${slug}`)
            .then(response => {
                console.log(response.data)
              
                this.course = response.data.course
                this.lessons = response.data.lessons
            })
    }
}

</script>