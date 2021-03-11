<template>
    <div class="row container">
        <div class="col-12">
            <h1 class="my-3">Modifica la tua Risposta!</h1>
            <form @submit.prevent="updateAnswer">
                <textarea
                    v-model="newAnswer"
                    class="form-control"
                    rows="3"
                    placeholder="Modifica la tua risposta"
                ></textarea>
                <button
                    type="submit"
                    class="btn btn-success mt-2"
                >Modifca Risposta</button>
            </form>
            <p class="error mt-2">{{ error }}</p>
        </div>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
    name: "AnswerEdit",
    props: {
        id: {
            type: Number,
            required: true
        },
        previousAnswer: {
            type: String,
            required: true
        },
        slug: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            newAnswer: this.previousAnswer,
            error: null
        }
    },
    async beforeRouteEnter(to, from, next){
        // prima che venga caricata la 'route', prendo il contenuto dell'answer e la visualizzo nella textarea
        let endpoint = `/api/answers/${to.params.id}/`;
        await apiService(endpoint)
            .then( data => {
                to.params.previousAnswer = data.content;
            })
        return next();
    },
    methods: {
        setTitle() {
            document.title = 'Ask!' + " - " + 'Answer Editor';
        },
        updateAnswer() {
            if(this.newAnswer != ""){
                let endpoint = `/api/answers/${this.id}/`;
                apiService(endpoint, "PUT", { content: this.newAnswer })
                    .then( () => {
                        this.$router.push({
                            name: 'question',
                            params: { slug: this.slug }
                        })
                    })
            }else {
                this.error = "Non puoi lasciare il campo testuale vuoto!";
            }

        }
    },
    created() {
        this.setTitle();
    }
}
</script>
