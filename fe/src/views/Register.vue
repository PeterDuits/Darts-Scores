<template>
  <v-container text-xs-center text-lg-left>
    <v-layout row wrap fill-height>
      <v-flex xs12>
        <h1>Create account</h1>
      </v-flex>
      <v-flex xs12>
        <RegisterForm @submitted="nextStep"/>
      </v-flex>
      <v-flex xs12>
        <v-layout row wrap>
          <v-flex xs6>
            <v-btn @click="login" color="primary" small>Login</v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import RegisterForm from "@/components/register/RegisterForm.vue";
import { mapActions } from "vuex";

export default {
  name: "RegisterPage",

  methods: {
    ...mapActions(["login"]),
    nextStep() {
      this.$router.push({ name: "Feed" });
    },
    loginAsGuest() {
      this.login("guest").then(() => {
        this.nextStep();
      });
    },
    login() {
      this.$router.push({ name: "Login" });
    }
  },
  components: {
    RegisterForm
  }
};
</script>

<style lang="scss" scoped>
</style>
