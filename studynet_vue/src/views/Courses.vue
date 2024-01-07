<template>
    <div class="courses">
      <div class="hero is-info is-medium">
        <div class="hero-body has-text-centered">
          <h1 class="title">Course</h1>
        </div>
      </div>
      <section class="section">
        <div class="container">
          <div class="columns">
            <div class="column is-2">
              <aside class="menu">
                <p class="menu-label">Categories</p>
                <ul class="menu-list">
                  <li><a href="" class="is-active">All courses</a></li>
                  <li><a href="">Programming</a></li>
                  <li><a href="">Design</a></li>
                  <li><a href="">UX</a></li>
                </ul>
              </aside>
            </div>
  
            <div class="column is-10">
              <div class="columns is-multiline">
                <!-- 排列圖片從這個block開始 -->
                <div class="column is-4"
                     v-for="course in courses"
                     v-bind:key="courses.id"
                >

                  <div class="card">
                    <div class="card-image">
                      <figure class="image is-4by3">
                        <img src="http://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
                      </figure>
                    </div>
  
                    <div class="card-content">
                      <div class="media">
                        <div class="media-content">
                          <p class="is-size-5">{{ course.title }}</p>
                        </div>
                      </div>
  
                      <div class="content">
                        <p>{{ course.short_description }}</p>
                      <router-link :to="{name: 'Course', params: {slug: course.slug}}">More</router-link>

                      </div>
                    </div>
                  </div>
                </div>
         
  
                <div class="column is-12">
                    <nav class="pagination">
                        <a href="" class="pagination-previous">Previous</a>
                        <a href="" class="pagination-next">Next</a>

                        <ul class="pagination-list">
                            <li>
                                <a href="" class="pagination-link is-current">1</a>
                            </li>
                            <li>
                                <a href="" class="pagination-link">2</a>
                            </li>
                            <li>
                                <a href="" class="pagination-link">3</a>
                            </li>
                        </ul>
                    </nav>
                </div>
  
              </div>
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
            courses: []
        }
    },

    mounted() {
        console.log('mounted')
        axios
            .get('/courses/')
            .then(response => {
                console.log(response.data)
              
                this.courses = response.data
            })
    }
}

</script>