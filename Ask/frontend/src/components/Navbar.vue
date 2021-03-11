<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my_nav">
        <div class="container">
            <router-link
                class="navbar-brand"
                to="/"
            ><strong>ASK</strong></router-link>

            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <router-link
                            class="btn btn-success"
                            to="/"
                        >Home</router-link>
                    </li>
                    <li class="nav-item mx-2">
                        <router-link
                            class="btn btn-danger"
                            to="/ask"
                        >Aggiungi Domanda</router-link>
                    </li>
                    <li class="nav-item">
                        <a class="btn btn-outline-secondary" href="/accounts/logout/">Logout</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "Navbar"
}
</script>

<style>
.btn:focus{
    box-shadow: none !important;
}
.my_nav{
    border-bottom: 1px solid #DDD;
}
.navbar-brand:hover{
    color: #DC3545 !important;
}
</style>