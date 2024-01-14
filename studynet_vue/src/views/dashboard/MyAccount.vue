<template>
    <div class="about">
      <div class="hero is-info is-medium">
        <div class="hero-body has-text-centered">
          <h1 class="title">My account</h1>
  
  
        </div>
      </div>
  
      <section class="section">
        <div class="cloumns is-multiline">
          <div class="column is-12">
            <h2 class="subtitle is-size-3"> Your active courses</h2>

          </div>

          <div 
              class="column is-4"
              v-for="course in courses"
              v-bind:key="course.id"
          >
            <CourseItem :course="course" />
          </div>
        </div>

        <hr>
        <button @click="logout()" class="button is-danger">Log out</button>
      </section>
  
    </div>
  </template>
  

  <script>
import axios from 'axios'

import CourseItem from '@/components/CourseItem.vue'

export default {
    data() {
      return {
        courses: []
      }
    },
    components: {
      CourseItem,
    },
    mounted() {
      axios
          .get('activities/get_active_courses/')
          .then(response=> {
            console.log(response.data)
            
            this.courses = response.data
          })
    },
    methods: {
        logout() {
            console.log('logout')

            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}
</script>