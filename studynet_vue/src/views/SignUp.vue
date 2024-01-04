<template>
    <div class="signup">
      <div class="hero is-info is-medium">
        <div class="hero-body has-text-centered">
          <h1 class="title">Sign up</h1>
  
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
                            <label for="">Repeat password</label>
                            <div class="control">
                                <input type="password" class="input">
                                
                            </div>
                        </div>

                        <div class="field">
                            <div class="control">
                                <div class="button is-dark">Sign up</div>
                            </div>
                        </div>

                        <hr>

                        Or <router-link to="/log-in">Click here</router-link> to log in!

                    </form>
                </div>
            </div>
        </div>
      </section>
  
    </div>
  </template>
  