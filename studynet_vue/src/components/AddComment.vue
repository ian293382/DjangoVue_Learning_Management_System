<template>
    <form v-on:submit.prevent="submitComment()">
        <div class="field">
            <label class="label">Name</label>
            <div class="control">
                <input type="text" class="input" v-model="comment.name">
            </div>
        </div>

        <div class="field">
            <label class="label">Content</label>
            <div class="control">
                <textarea class="textarea" v-model="comment.content"></textarea>
            </div>
        </div>

        <div 
            class="notification is-danger"
            v-for="error in errors"
            v-bind:key="error"
        >
            {{ error }}
        </div>

        <div class="field">
            <div class="control">
                <button class="button is-link">Submit</button>
            </div>
        </div>
    </form>

</template>

<script>
import axios from 'axios';

export default {
    props: [
        'course', 'activeLesson',
    ],
    data() {
        return {
            comment: {
                name: '',
                content: '',
            },
            errors: []
        }
    },
    methods: {
        submitComment() {
            console.log('submitComment')

            this.errors = []

            if (this.comment.name === '') {
                this.errors.push('The name must be filled out')
            }

            if (this.comment.content === '') {
                this.errors.push('The content must be filled out')
            }

            if (!this.errors.length) {
                axios // this.$route.params.slug 當前網址去做讀取 ex . Programming-course-one 後面的是使用者負責點擊 Lesson 所以在pops activeLesson就做好了
                    .post(`/courses/${this.$route.params.slug}/${this.activeLesson.slug}/`, this.comment)
                    .then(response => {
                        this.comment.name = ''
                        this.comment.content = ''
                        // 觸發一個名為 submitComment 的自訂事件，同時將伺服器回應的評論數據（response.data）傳遞給父元件 
                        this.$emit('submitComment', response.data)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        },
    }
}
</script>