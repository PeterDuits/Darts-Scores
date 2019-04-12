<template>
  <v-form>
    <v-container>
      <v-layout row wrap>
        <v-flex xs12>
          <v-text-field v-model="email" label="email"></v-text-field>
        </v-flex>
        <v-flex xs12>
          <v-text-field v-model="password" type="password" label="password"></v-text-field>
        </v-flex>
        <v-flex xs12>
          <v-btn @click="submit" color="primary" depressed large block>Login</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-form>
</template>

<script>
import axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "LoginForm",
  data: () => ({
    email: "",
    password: ""
  }),
  methods: {
    ...mapActions("user", ["login"]),
    submit() {
      const vm = this;
      axios({
        method: "post",
        url: `${process.env.VUE_APP_API_URL}/auth`,
        data: {
          email: this.email,
          password: this.password
        }
      }).then(user => {
        this.login({
          username: user.data.user.username,
          token: user.data.token
        }).then(() => {
          vm.$router.push({ name: "Feed" });
        });
      });
    }
  }
};
</script>

<style>
</style>
