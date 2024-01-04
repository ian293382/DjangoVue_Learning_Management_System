<template>
    <div class="signup">
      <div class="hero is-info is-medium">
        <div class="hero-body has-text-centered">
          <h1 class="title">Log In</h1>
  
        </div>
      </div>
  
      <section class="section">
        <div class="container">
            <div class="columns">
                <div class="column is-4 is-offset-4">
                    <form action="">
                        <div class="field">
                            <label for="">Email</label>
                            <div class="control">
                                <input type="email" class="input">

                            </div>
                        </div>

                        <div class="field">
                            <label for="">Password</label>
                            <div class="control">
                                <input type="password" class="input">
                                
                            </div>
                        </div>


                        <div class="field">
                            <div class="control">
                                <div class="button is-dark">Log in</div>
                            </div>
                        </div>

                        <hr>

                        Not a member? <router-link to="/sign-up">Click here to sign up!</router-link>

                    </form>
                </div>
            </div>
        </div>
      </section>
  
    </div>
  </template>
  