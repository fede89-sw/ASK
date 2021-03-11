<template>
    <div class="single-answer">
        <p class="text-muted"><strong class="author">{{ answer.author }}</strong> ha risposto: {{ answer.created_at }}</p>
        <p>{{ answer.content }}</p>
        <div v-if="getLoggedUser" class="question-edit my-2">    
            <router-link
                :to="{ name: 'answer-edit', params: { id: answer.id, slug: slug } }"
                class="btn btn-sm btn-outline-secondary mr-1"
            >Modifica</router-link>
            <button
                @click="emitDeleteAnswer"
                class="btn btn-sm btn-outline-danger"
            >Cancella</button>
        </div>
        <div v-else class="like-button my-2">
            <button
                v-if="!userHasVoted"
                class="btn btn-sm btn-outline-danger"
                @click="addLike"
            ><strong>Like [{{ likesCount }}]</strong></button>
            <button
                v-else
                class="btn btn-sm btn-danger"
                @click="deleteLike"
            ><strong>Like [{{ likesCount }}]</strong></button>
        </div>
        <hr>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
    name: "Answer",
    props: {
        answer: {
            type: Object,
            required: true
        },
        slug: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            userHasVoted: this.answer.user_has_voted,
            likesCount: this.answer.likes_count
        }
    },
    computed: {
        getLoggedUser() {
            // torna 'true' o 'false' se l'utente loggato è l'autore della rispota
            return this.answer.author === window.localStorage.getItem("username");
        }
    },
    methods: {
        emitDeleteAnswer() {
            this.$emit('delete-answer', this.answer);
        },
        addLike() {
            let endopoint = `/api/answers/${this.answer.id}/like/`;
            apiService(endopoint, "POST")
            this.userHasVoted = true;
            this.likesCount += 1;
        },
        deleteLike() {
            let endopoint = `/api/answers/${this.answer.id}/like/`;
            apiService(endopoint, "DELETE")
            this.userHasVoted = false;
            this.likesCount -= 1; 
        }
    }
}
  
</script>
