<template>
    <div class="home mt-3">

        <div v-if="notFoundComputed" class="container">
            <h1 class="notFound">404 - DOMANDA NON TROVATA</h1>
        </div>

        <div v-else class="container">               
            <h1>{{ question.content }}</h1>
            <p class="text-muted mb-0">Domanda aggiunta da: <strong class="author">{{question.author}}</strong></p>
            <p class="text-muted mb-0">{{ question.created_at }}</p>
            <div v-if="getLoggedUser" class="question-edit my-2">
                <router-link
                    :to="{ name: 'question-cu', params: { slug: slug } }"
                    class="btn btn-sm btn-outline-secondary mr-1"
                >Modifica</router-link>
                <button
                    @click="deleteQuestion"
                    class="btn btn-sm btn-outline-danger"
                >Cancella</button>
            </div>
            <hr>
            <div v-if="userHasAnswered">
                <p class="text-success" style="font-weight: bold;">Hai già risposto a questa domanda!</p>
            </div>
            <div v-else-if="showForm">
                <form @submit.prevent="submitAnswer">
                    <textarea
                        v-model="newAnswer"
                        rows="3"
                        class="form-control"
                        placeholder="Rispondi alla domanda"
                    ></textarea>
                    <button
                        type="submit"
                        class="btn btn-success mt-2"
                    >Pubblica Risposta</button>
                </form>
                <p class="error mt-2">{{ error }}</p>
            </div>
            <div v-else>
                <button
                    @click="showForm = true"
                    class="btn btn-sm btn-success"
                >Rispondi</button>
            </div>
            <hr>

            <div v-for="answer in answers" :key="answer.pk">
                <Answer
                    :answer=answer
                    :slug=slug
                    @delete-answer="deleteAnswer"
                />
            </div>

            <button
                v-if="next"
                @click="getAnswers"
                class="btn btn-sm btn-outline-success"
            >Carica Ancora</button>
            <p v-show="isLoading" class="mt-2">...loading...</p>
        </div>

    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import Answer from "@/components/Answer.vue";

export default {
    name: "Question",
    props: {
        slug: {
            type: String, 
            required: true
        }
    },
    components: {
        Answer
    },
    data() {
        return {
            question: {},
            answers: [],
            next: null,
            isLoading: false,
            userHasAnswered: false,
            showForm: false,
            newAnswer: null,
            error: null        }
    },
    computed: {
        getLoggedUser() {
            // torna 'true' o 'false' se l'utente loggato è l'autore della domanda
            return this.question.author === window.localStorage.getItem("username");
        },
        notFoundComputed() {
            // torna 'undefined' se non è presente 'detail' nell'oggetto question, 
            // ovvero se è stata trovata o meno la domanda dalla REST API
            return this.question["detail"];
        }
    },
    methods: {
        setTitle(title) {
            document.title = 'Ask!' + " - " + title;
        },
        singleQuestion() {
            let endpoint = `/api/questions/${this.slug}/`;
            apiService(endpoint)
                .then( data => {
                    this.question = data;
                    this.userHasAnswered = data.user_has_answered;
                    this.setTitle(data.content);
                })
        },
        getAnswers() {
            let endpoint = `/api/questions/${this.slug}/answers/`;
            if(this.next){
                endpoint = this.next
            }
            this.isLoading = true;
            apiService(endpoint)
                .then( data => {
                    this.answers.push(...data.results);
                    this.next = data.next;
                    this.isLoading = false;
                })
        },
        submitAnswer() {
            if(this.newAnswer) {
                let endpoint = `/api/questions/${this.slug}/answer/`
                apiService(endpoint, "POST", { content: this.newAnswer })
                    .then( data => {
                        this.answers.unshift(data)
                    })
                    if(this.error){
                        this.error = null;
                    }
                    this.showForm = false;
                    this.userHasAnswered = true;
                    this.newAnswer = null;
            }else{
                this.error = "Non puoi lasciare il campo di testo vuoto!"
            }
        },
        deleteQuestion() {
            let endpoint = `/api/questions/${this.slug}/`;
            apiService(endpoint, "DELETE")
                .then( () => {
                    this.$router.push("/");
                })
        },
        deleteAnswer(answer) {
            let endpoint = `/api/answers/${answer.id}/`;
            apiService(endpoint, "DELETE")
                .then( () => {
                    this.answers.splice(this.answers.indexOf(answer), 1);
                })
            this.userHasAnswered = false;
        }
    },
    created() {
        this.singleQuestion();
        this.getAnswers();
    }
}
</script>

<style>

</style>