<template>
  <v-form>
    <v-container>
      <v-layout row wrap>
        <v-flex xs12>
          <v-text-field v-model="username" label="Username"></v-text-field>
        </v-flex>
        <v-flex xs12>
          <v-text-field v-model="email" label="Email"></v-text-field>
        </v-flex>
        <v-flex xs12>
          <v-text-field
            v-model="password"
            label="Password"
            :append-icon="showPassword ? 'visibility' : 'visibility_off'"
            :type="showPassword ? 'text' : 'password'"
            @click:append="showPassword = !showPassword"
          ></v-text-field>
        </v-flex>

        <v-flex xs12>
          <span class="caption">{{ text.caption }}</span>
        </v-flex>
        <v-flex xs12>
          <v-btn @click="submit" depressed block color="primary">{{ text.button}}</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-form>
</template>

<script>
import axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "RegistrationForm",
  data: () => ({
    username: "",
    email: "",
    password: "",
    showPassword: false,
    error: "",
    text: {
      caption:
        "By creating an account you agree to our Terms of Service and Privacy Policy",
      button: "Register"
    }
  }),
  methods: {
    ...mapActions("user", ["login"]),
    submit() {
      axios({
        method: "post",
        url: `${process.env.VUE_APP_API_URL}/players`,
        data: {
          username: this.username,
          email: this.email,
          password: this.password
        }
      })
        .then(data => {
          console.log(data);
          const loginPayload = {
            token: data.data.token,
            username: data.data.user.username
          };
          this.login(loginPayload).then(() => {
            this.$emit("submitted");
          });
        })
        .catch(err => {
          this.error = err;
        });
    }
  }
};
</script>
