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
                    <CourseItem :course="course"/>
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
import CourseItem from '@/components/CourseItem.vue';
import axios from 'axios';

export default {
    data() {
        return {
            courses: [],
            categories: [],
            activeCategory: null,
        };
    },
    components: {
        CourseItem 
    },
    async mounted() {
        console.log('mounted');

        await axios
                .get('/courses/get_categories/')
                .then(response => {
                    console.log(response.data);

                })

        await axios
                .get('/courses/')
                .then(response => {
                console.log(response.data);
                this.courses = response.data;
        });
    },
    
}

</script>