<template>
  <div class="home mt-3">
    <div class="container">
      <div v-for="question in questions" :key="question.pk">
        
          <p class="text-muted mb-0">Domanda di <strong class="author">{{ question.author }}</strong></p>

          <h2>
            <router-link
              :to="{ name: 'question', params: { slug: question.slug } }"
              class="question-link"
            >{{ question.content }}</router-link>
          </h2>

          <p class="text-muted">Risposte: {{ question.answer_count }}</p>

          <hr>

      </div>
      <button
        v-if="next"
        @click="getQuestions"
        class="btn btn-sm btn-outline-success"
      >Carica Ancora</button>
      <p v-show="isLoading" class="mt-2">...loading...</p>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Home",
  data() {
    return {
      questions: [],
      next: null,
      isLoading: false
    }
  },
  methods: {
    setTitle() {
      document.title = 'Ask!' + " - " + 'Homepage';
    },
    getQuestions() {
      let endpoint = "/api/questions/"
      if(this.next){
        endpoint = this.next
      }
      this.isLoading = true;
      apiService(endpoint)
        .then( data => {
          this.questions.push(...data.results)
          this.next = data.next
          this.isLoading = false;
        })
    }
  },
  created() {
    this.getQuestions();
    this.setTitle();
  }
};
</script>

<style>
.author{
  color: #DC3545;
}
.question-link{
  color: black;
}
.question-link:hover{
  text-decoration: none;
  color: #6C657C;
}
</style>