import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Question from "@/views/Question.vue";
import QuestionCU from "@/views/QuestionCreateUpdate.vue";
import AnswerEdit from "@/views/AnswerEdit.vue";
import NotFound from "@/views/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/question/:slug",
    name: "question",
    component: Question,
    props: true
  },
  {
    path: "/ask/:slug?",
    name: "question-cu",
    component: QuestionCU,
    props: true
  },
  {
    path: "/answer/:id",
    name: "answer-edit",
    component: AnswerEdit,
    props: true
  },
  {
    path: "*",
    name: "not-found",
    component: NotFound
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;