<template>
    <nav class="navbar is-info" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
      
        <router-link to="/" class="navbar-item is-size-4 white">StudyNet</router-link>

        <div class="navbar-menu" id="navbar-item">
            <div class="navbar-start">
                <router-link to="/" class="navbar-item">Home</router-link>
                <router-link to="/about" class="navbar-item">About</router-link>
                <router-link to="/courses" class="navbar-item">Courses</router-link>
            </div>

        <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                    <template  v-if="$store.state.user.isAuthenticated">
                        <router-link to="/dashboard/create-course" class="button is-primary">Create course</router-link>
                        <router-link to="/dashboard/my-account" class="button is-info">My account</router-link>
                    </template>
                    <template v-else>
                        <a href="/sign-up" class="button is-primary"><strong>Sign up</strong></a>
                        <a href="/log-in" class="button is-light">Log in</a>
                    </template>
                </div>
            </div>
        </div>
        </div>

  </nav>
</template>