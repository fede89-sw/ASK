import { CSRF_TOKEN } from "./csrf_token.js";

function getJson(response) {
    /* torna il json del response di fattch; torna '' se lo status
        è 204 NO_CONTENT, altrimenti torna il json */

    if(response.status === 204) return '';
    return response.json();
}

function apiService(endpoint, method, data){
    /* funzione base per ogni tipo di richiesta alla REST API; */

    const config = {
        method: method || "GET",
        body: data !== undefined ? JSON.stringify(data) : null,
        headers: {
            "content-type": "application/json",
            "X-CSRFToken": CSRF_TOKEN
        }
    }
    return fetch(endpoint, config)
        .then(getJson)
        .catch(error => {console.log(error)})
}

export { apiService }