<template>
  <v-container text-xs-center text-lg-left>
    <v-layout row wrap fill-height>
      <v-flex xs12>
        <h1>Login</h1>
      </v-flex>
      <v-flex xs12>
        <login-form></login-form>
      </v-flex>
      <v-flex xs12>
        <v-btn flat color="primary" small>Login as ipad</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import LoginForm from "@/components/login/LoginForm.vue";

export default {
  name: "Login",

  components: { LoginForm }
};
</script>
