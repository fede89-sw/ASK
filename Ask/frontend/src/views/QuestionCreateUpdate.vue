<template>
    <div class="row container">
        <div class="col-12">
            <h1 class="my-3">Aggiungi una Domanda!</h1>
            <form @submit.prevent="addQuestion">
                <textarea
                    v-model="newQuestion"
                    class="form-control"
                    rows="3"
                    placeholder="Aggiungi una domanda"
                ></textarea>
                <button
                    type="submit"
                    class="btn btn-success mt-2"
                >Aggiungi Domanda</button>
            </form>
            <p class="error mt-2">{{ error }}</p>
        </div>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
    name: "QuestionCU",
    props: {
        slug: {
            type: String,
            required: false
        },
        previousQuestion: {
            type: String,
            required: false
        }
    },
    data(){
        return {
            newQuestion: this.previousQuestion || null,
            error: null
        }
    },
    async beforeRouteEnter (to, from, next) {
        if(to.params.slug) {
            let endpoint = `/api/questions/${to.params.slug}/`;
            await apiService(endpoint)
                    .then( data => {
                        to.params.previousQuestion = data.content;
                    })
        }
        return next();
    },
    methods: {
        setTitle() {
            document.title = 'Ask!' + " - " + 'Question Editor';
        },
        addQuestion() {
            if(this.newQuestion){
                if (this.newQuestion.length <= 240){
                    let endpoint = "/api/questions/";
                    let method = "POST"
                    if(this.slug){
                        method = "PUT";
                        endpoint = `/api/questions/${this.slug}/`
                    }
                    apiService(endpoint, method, { content: this.newQuestion })
                        .then( data => {
                            this.$router.push({
                                name: "question",
                                params: { slug: data.slug }
                            })
                        })
                    if(this.error){
                        this.error = null;
                    }
                }
                else {
                    this.error = "Non puoi superare i 240 caratteri!"
                }
            } else {
                this.error = "Non puoi lasciare il campo testuale vuoto!";
            }
        }
    },
    created() {
        this.setTitle();
    }
}
</script>

<style>
.error{
    font-weight: bold;
    color: red;
}
</style>