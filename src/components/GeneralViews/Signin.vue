<template>
<section id="login">
  <div class="container">
    <div class="row  row-eq-height">
        <div class="col-md-3">
        </div>
      <div class="col-md-6">
        <h2 class="other f400 ">Please Login</h2>
        <br>
<br>

        <form name="form" class="form space30" (ngSubmit)="f.form.valid && signin()" #f="ngForm" novalidate>
          <div class="form-group">
            <label for="email">Username or Email Address</label>
            <fg-input class="form-control" type="text"
                      label="Username"
                      :disabled="true"
                      placeholder="Enter username"
                      v-model="user.username">
            </fg-input>
          </div>
          <div class="form-group space50">
            <label for="pwd">Password (case sensitive)</label>
            <fg-input class="form-control" type="text"
                      label="Password"
                      :disabled="true"
                      placeholder="Enter password"
                      v-model="user.password">
            </fg-input>

          <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="userLogin">
            Add Partner
          </button>
          
<br>
<br>
<br>
<br>
          <div class="row line1 space40">
            <div class="col-md-6">
              <button type="button" class="btn btn-default white-btn btn-block" routerLink="/forgot">Forgot your password?</button>
            </div>
            <div class="col-md-6">
              <button type="button" class="btn btn-default white-btn btn-block" routerLink="/signup">Click here to register as a new user</button>
            </div>
          </div>
        </form>
      </div>
      <div class="col-md-3">
        </div>

    </div>
  </div>
</section>
</template>





<script>
import auth from '@/store/auth.module'
export default {
  data() {
    return {
      user: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    userLogin() {
        auth.actions.REGISTER(this.user);
        alert("Your data: " + JSON.stringify(this.user));
    }
  }
};
</script>
<style>
</style>
