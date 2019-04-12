import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
      meta: {
        hideToolbar: true
      }
    },
    {
      path: "/register",
      name: "register",
      component: () => import("./views/Register.vue")
    },
    {
      path: "/login",
      name: "Login",
      component: () => import("./views/Login.vue")
    },
    {
      path: "/feed",
      name: "Feed",
      component: () => import("./views/Feed.vue")
    },
    {
      path: "/find-players",
      name: "FindPlayers",
      component: () => import("./views/FindPlayers.vue")
    },
    {
      path: "/setup",
      name: "Setup",
      component: () => import("./views/Setup.vue")
    },
    {
      path: "/coinflip",
      name: "CoinFlip",
      component: () => import("./views/CoinFlip.vue")
    },
    {
      path: "/game",
      name: "Game",
      component: () => import("./views/Game.vue"),
      meta: {
        hideToolbar: true
      }
    }
  ]
});
